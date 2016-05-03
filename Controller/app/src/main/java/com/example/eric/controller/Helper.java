package com.example.eric.controller;

import android.app.Application;
import android.bluetooth.BluetoothDevice;

/**
 * Created by Eric on 4/27/2016.
 */
public class Helper extends Application{
    public MainActivity.ConnectedThread connTh;
    public BluetoothDevice btooth;
    public void setConnect(MainActivity.ConnectedThread ct){
        this.connTh = ct;
    }
    public MainActivity.ConnectedThread getConnect(){
        return connTh;
    }

    public void setDevice(BluetoothDevice bt){
        this.btooth = bt;
    }

    public BluetoothDevice getDevice(){
        return btooth;
    }
}
