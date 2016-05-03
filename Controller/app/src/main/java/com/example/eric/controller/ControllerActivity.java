package com.example.eric.controller;

import android.app.Activity;
import android.app.Application;
import android.bluetooth.BluetoothDevice;
import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class ControllerActivity extends Activity {
    //private Application
    ImageButton up;
    ImageButton down;
    ImageButton right;
    ImageButton left;
    Button pauseButton;
    MainActivity myApp;
    MainActivity.ConnectedThread cnnct;
    BluetoothDevice dev;
    boolean pause = false;
   // @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_controller);
        Toast.makeText(getApplicationContext(), "Successfully Connected!", Toast.LENGTH_SHORT).show();
        up = (ImageButton)findViewById(R.id.imageButton);
        down = (ImageButton)findViewById(R.id.imageButton4);
        right = (ImageButton)findViewById(R.id.imageButton3);
        left = (ImageButton)findViewById(R.id.imageButton2);
        pauseButton = (Button)findViewById(R.id.button);
        cnnct = ((Helper)this.getApplication()).getConnect();
        up.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String w = "w";
                cnnct.write(w.getBytes());
            }
        });
        down.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String s = "s";
                cnnct.write(s.getBytes());
            }
        });

        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String a = "a";
                cnnct.write(a.getBytes());
            }
        });

        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String d = "d";
                cnnct.write(d.getBytes());
            }
        });
    }
    public void pause(View v){
        if(pause) {
            String p = "p";
            cnnct.write(p.getBytes());
            pauseButton.setText("CONTINUE");
        }
        else{
            String c = "c";
            cnnct.write(c.getBytes());
            pauseButton.setText("PAUSE");
        }
        pause = !pause;
    }

    public void select(View v){
        String z = "z";
        cnnct.write(z.getBytes());
    }
}
