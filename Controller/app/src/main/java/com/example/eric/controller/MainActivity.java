package com.example.eric.controller;

import android.app.Activity;
import android.app.Application;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Message;
import android.os.Parcelable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;
import android.os.Handler;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.UUID;
import java.util.logging.LogRecord;

public class MainActivity extends Activity implements AdapterView.OnItemClickListener {

    ArrayAdapter<String> listAdapter;
    ListView listView;
    BluetoothAdapter btooth;
    Set<BluetoothDevice> devicesArray;
    ArrayList<String> pairedDevices;
    ArrayList<BluetoothDevice> devices;
    public static final UUID MY_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    IntentFilter filter;
    BroadcastReceiver receiver;
    public ConnectedThread cnnct;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
        if(btooth==null){
            Toast.makeText(getApplicationContext(), "No bluetooth detected", Toast.LENGTH_SHORT).show();
            finish();
        }
        else {
            if (!btooth.isEnabled()) {
                turnOnBluetooth();
            }
            getPairedDevices();
            startDiscovery();
        }
    }
    public void startDiscovery() {
        btooth.cancelDiscovery();
        btooth.startDiscovery();

    }
    private void turnOnBluetooth() {
        Intent intent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
        startActivityForResult(intent, 1);
    }
    private void getPairedDevices() {
        devicesArray = btooth.getBondedDevices();
        if(devicesArray.size()>0){
            for(BluetoothDevice device:devicesArray){
                pairedDevices.add(device.getName());

            }
        }
    }
    private void init() {
        listView=(ListView)findViewById(R.id.listView);
        listView.setOnItemClickListener(this);
        listAdapter= new ArrayAdapter<String>(this,R.layout.list_color,R.id.list_content);
        listView.setAdapter(listAdapter);
        btooth = BluetoothAdapter.getDefaultAdapter();
        pairedDevices = new ArrayList<String>();
        filter = new IntentFilter(BluetoothDevice.ACTION_FOUND);
        devices = new ArrayList<BluetoothDevice>();
        receiver = new BroadcastReceiver(){
            @Override
            public void onReceive(Context context, Intent intent) {
                String action = intent.getAction();

                if(BluetoothDevice.ACTION_FOUND.equals(action)){
                    BluetoothDevice device = intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);
                    devices.add(device);
                    String s = "";
                    for(int a = 0; a < pairedDevices.size(); a++){
                        if(device.getName() != null)
                            if(device.getName().equals(pairedDevices.get(a))){
                                s = "(Paired)";
                                break;
                            }
                    }

                    listAdapter.add(device.getName()+" "+s+" "+"\n"+device.getAddress());
                }

                else if(BluetoothAdapter.ACTION_DISCOVERY_STARTED.equals(action)){
                    // run some code
                }
                else if(BluetoothAdapter.ACTION_DISCOVERY_FINISHED.equals(action)){
                    // run some code



                }
                else if(BluetoothAdapter.ACTION_STATE_CHANGED.equals(action)){
                    if(btooth.getState() == btooth.STATE_OFF){
                        turnOnBluetooth();
                    }
                }

            }
        };
        registerReceiver(receiver, filter);
        filter = new IntentFilter(BluetoothAdapter.ACTION_DISCOVERY_STARTED);
        registerReceiver(receiver, filter);
        filter = new IntentFilter(BluetoothAdapter.ACTION_DISCOVERY_FINISHED);
        registerReceiver(receiver, filter);
        filter = new IntentFilter(BluetoothAdapter.ACTION_STATE_CHANGED);
        registerReceiver(receiver, filter);
    }


    @Override
    protected void onPause() {
        super.onPause();
        unregisterReceiver(receiver);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(resultCode == RESULT_CANCELED){
            Toast.makeText(getApplicationContext(), "Enable Bluetooth to continue", Toast.LENGTH_SHORT).show();
            finish();
        }
    }

    public void onItemClick(AdapterView<?> arg0, View arg1, int arg2, long arg3) {

        if(btooth.isDiscovering()){
            btooth.cancelDiscovery();
        }
        if(listAdapter.getItem(arg2).contains("Paired")){
            boolean connected = false;
            BluetoothDevice selectedDevice = devices.get(arg2);
            BluetoothConnector connect = new BluetoothConnector(selectedDevice, true, null);
            try {
                connect.connect();
                connected = true;
            } catch (IOException e) {
                e.printStackTrace();
            }
            if(connected){
                cnnct = new ConnectedThread(connect.bluetoothSocket);
                ((Helper)this.getApplication()).setConnect(cnnct);
                Intent intent = new Intent(this, ControllerActivity.class);
                startActivity(intent);
            }
            else {
                Toast.makeText(getApplicationContext(), "Could not Connect!", Toast.LENGTH_SHORT).show();
            }
        }
        else{
            Toast.makeText(getApplicationContext(), "device is not paired", Toast.LENGTH_SHORT).show();
        }
    }

   public class ConnectedThread extends Thread {
        private final BluetoothConnector.BluetoothSocketWrapper mmSocket;
        private final InputStream mmInStream;
        private final OutputStream mmOutStream;

        public ConnectedThread(BluetoothConnector.BluetoothSocketWrapper socket) {
            mmSocket = socket;
            InputStream tmpIn = null;
            OutputStream tmpOut = null;

            try {
                tmpIn = socket.getInputStream();
                tmpOut = socket.getOutputStream();
            } catch (IOException e) { }

            mmInStream = tmpIn;
            mmOutStream = tmpOut;
        }

        public void run() {
            byte[] buffer;  // buffer store for the stream
            int bytes; // bytes returned from read()

            // Keep listening to the InputStream until an exception occurs
            while (true) {
                try {
                    // Read from the InputStream
                    buffer = new byte[1024];
                    bytes = mmInStream.read(buffer);
                    // Send the obtained bytes to the UI activity
                    //mHandler.obtainMessage(MESSAGE_READ, bytes, -1, buffer)
                      //      .sendToTarget();

                } catch (IOException e) {
                    break;
                }
            }
        }

        /* Call this from the main activity to send data to the remote device */
        public void write(byte[] bytes) {
            try {
                mmOutStream.write(bytes);
            } catch (IOException e) { }
        }

        /* Call this from the main activity to shutdown the connection */
        public void cancel() {
            try {
                mmSocket.close();
            } catch (IOException e) { }
        }
    }

    public static class BluetoothConnector {

        public BluetoothSocketWrapper bluetoothSocket;
        private BluetoothDevice device;
        private BluetoothAdapter adapter;
        private boolean secure;
        private List<UUID> uuidCandidates;
        private int candidate;

        /**
         * @param device the device
         * @param secure if connection should be done via a secure socket
       //  * @param adapt cancel discovery
         * @param uuidCandidates a list of UUIDs. if null or empty, the Serial PP id is used
         */
        public BluetoothConnector(BluetoothDevice device, boolean secure, /*BluetoothAdapter adapt,*/ List<UUID> uuidCandidates) {
            this.device = device;
            this.secure = secure;
            //this.adapter = adapt;
            this.uuidCandidates = uuidCandidates;

            if (this.uuidCandidates == null || this.uuidCandidates.isEmpty()) {
                this.uuidCandidates = new ArrayList<UUID>();
                this.uuidCandidates.add(UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"));
            }
        }

        public BluetoothSocketWrapper connect() throws IOException {
            boolean success = false;
            while (selectSocket()) {
                //adapter.cancelDiscovery();
                try {
                    bluetoothSocket.connect();
                    success = true;
                    break;
                } catch (IOException e) {
                    //try the fallback
                    try {
                        bluetoothSocket = new FallbackBluetoothSocket(bluetoothSocket.getUnderlyingSocket());
                        Thread.sleep(500);
                        bluetoothSocket.connect();
                        success = true;
                        break;
                    } catch (FallbackException e1) {
                        Log.w("BT", "Could not initialize FallbackBluetoothSocket classes.", e);
                    } catch (InterruptedException e1) {
                        Log.w("BT", e1.getMessage(), e1);
                    } catch (IOException e1) {
                        Log.w("BT", "Fallback failed. Cancelling.", e1);
                    }
                }
            }

            if (!success) {
                throw new IOException("Could not connect to device: "+ device.getAddress());
            }

            return bluetoothSocket;
        }

        private boolean selectSocket() throws IOException {
            if (candidate >= uuidCandidates.size()) {
                return false;
            }

            BluetoothSocket tmp;
            UUID uuid = uuidCandidates.get(candidate++);

            Log.i("BT", "Attempting to connect to Protocol: "+ uuid);
            if (secure) {
                tmp = device.createRfcommSocketToServiceRecord(uuid);
            } else {
                tmp = device.createInsecureRfcommSocketToServiceRecord(uuid);
            }
            bluetoothSocket = new NativeBluetoothSocket(tmp);

            return true;
        }

        public interface BluetoothSocketWrapper {

            InputStream getInputStream() throws IOException;

            OutputStream getOutputStream() throws IOException;

            String getRemoteDeviceName();

            void connect() throws IOException;

            String getRemoteDeviceAddress();

            void close() throws IOException;

            BluetoothSocket getUnderlyingSocket();

        }


        public static class NativeBluetoothSocket implements BluetoothSocketWrapper {

            private BluetoothSocket socket;

            public NativeBluetoothSocket(BluetoothSocket tmp) {
                this.socket = tmp;
            }

            @Override
            public InputStream getInputStream() throws IOException {
                return socket.getInputStream();
            }

            @Override
            public OutputStream getOutputStream() throws IOException {
                return socket.getOutputStream();
            }

            @Override
            public String getRemoteDeviceName() {
                return socket.getRemoteDevice().getName();
            }

            @Override
            public void connect() throws IOException {
                socket.connect();
            }

            @Override
            public String getRemoteDeviceAddress() {
                return socket.getRemoteDevice().getAddress();
            }

            @Override
            public void close() throws IOException {
                socket.close();
            }

            @Override
            public BluetoothSocket getUnderlyingSocket() {
                return socket;
            }

        }

        public class FallbackBluetoothSocket extends NativeBluetoothSocket {

            private BluetoothSocket fallbackSocket;

            public FallbackBluetoothSocket(BluetoothSocket tmp) throws FallbackException {
                super(tmp);
                try
                {
                    Class<?> clazz = tmp.getRemoteDevice().getClass();
                    Class<?>[] paramTypes = new Class<?>[] {Integer.TYPE};
                    Method m = clazz.getMethod("createRfcommSocket", paramTypes);
                    Object[] params = new Object[] {Integer.valueOf(1)};
                    fallbackSocket = (BluetoothSocket) m.invoke(tmp.getRemoteDevice(), params);
                }
                catch (Exception e)
                {
                    throw new FallbackException(e);
                }
            }

            @Override
            public InputStream getInputStream() throws IOException {
                return fallbackSocket.getInputStream();
            }

            @Override
            public OutputStream getOutputStream() throws IOException {
                return fallbackSocket.getOutputStream();
            }


            @Override
            public void connect() throws IOException {
                fallbackSocket.connect();
            }


            @Override
            public void close() throws IOException {
                fallbackSocket.close();
            }

        }

        public static class FallbackException extends Exception {

            /**
             *
             */
            private static final long serialVersionUID = 1L;

            public FallbackException(Exception e) {
                super(e);
            }

        }
    }
}

