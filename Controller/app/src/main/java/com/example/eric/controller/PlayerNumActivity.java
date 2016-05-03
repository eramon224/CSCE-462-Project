package com.example.eric.controller;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class PlayerNumActivity extends AppCompatActivity {

    MainActivity.ConnectedThread cnnct;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player_num);
        cnnct = ((Helper)this.getApplication()).getConnect();
    }
    public void player1(View v){
        String num = "1";
        cnnct.write(num.getBytes());
        Intent intent = new Intent (this, ControllerActivity.class);
        startActivity(intent);
    }

    public void player2(View v){
        String num = "2";
        cnnct.write(num.getBytes());
        Intent intent = new Intent (this, ControllerActivity.class);
        startActivity(intent);
    }
}
