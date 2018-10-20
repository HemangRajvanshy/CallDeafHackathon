package com.example.jowu.textui;

import android.support.constraint.ConstraintSet;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.Button;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.RelativeLayout;
import android.widget.RelativeLayout.LayoutParams;
import android.graphics.Color;


public class TextUI extends AppCompatActivity {
    private String senderName;

    public TextUI() {
        senderName = "Bob Ross";
    }

    public TextUI(String name) {
        senderName = name;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text_ui);

        receiveMessage("Hello. This is Bob Ross. Welcome to my art video guide.");

        final Button button = findViewById(R.id.button);
        final EditText editText = findViewById(R.id.editText);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                //display text underneath previous message (like texts)
                //Log.d(editText.getText().toString(), "hi");
                sendMessage(editText.getText().toString());
                editText.setText("");
                //editText.setText("Hello there");
            }


        });
    }

    private void sendMessage(String message) {
        //final LinearLayout layout = findViewById(R.id.layout);
        //setContentView(layout);
       // layout.setOrientation(LinearLayout.VERTICAL);
        //TextView textView = new TextView(this);
        //textView.setText(message);
        //layout.addView(textView);

        ConstraintSet cs = new ConstraintSet();

        LinearLayout ll = (LinearLayout) findViewById(R.id.ll);
        //TextView username =  findViewById(R.id.rightText);
        TextView username = new TextView(getApplicationContext());
        TextView tv = new TextView(getApplicationContext());
        TextView space = new TextView(getApplicationContext());
        RelativeLayout.LayoutParams lp = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, // Width of TextView
                LayoutParams.WRAP_CONTENT); // Height of TextView

        lp.addRule(RelativeLayout.ALIGN_PARENT_END);

        tv.setLayoutParams(lp);
        tv.setMaxWidth(700);
        tv.setText(message);
        tv.setTextSize(18);

        //want the response to be aligned along the right side of the parent view

        username.setLayoutParams(lp);
        username.setText("Me");
        username.setTextSize(14);

        space.setLayoutParams(lp);
        space.setTextSize(10);


        tv.setPadding(20, 10, 20, 10);
        tv.setBackgroundColor(Color.parseColor("#3884ff"));
        tv.setTextColor(Color.parseColor("#ffffff"));

        username.setTextColor(Color.parseColor("#3884ff"));



        // Add newly created TextView to parent view group (RelativeLayout)
        ll.addView(space);
        ll.addView(username);
        ll.addView(tv);

    }

    public void receiveMessage(String message) {
        LinearLayout ll = (LinearLayout) findViewById(R.id.ll);
        TextView callername = new TextView(getApplicationContext());
        TextView tv = new TextView(getApplicationContext());
        TextView space = new TextView(getApplicationContext());
        LayoutParams lp = new RelativeLayout.LayoutParams(
                LayoutParams.WRAP_CONTENT, // Width of TextView
                LayoutParams.WRAP_CONTENT); // Height of TextView

        tv.setLayoutParams(lp);
        tv.setMaxWidth(700);
        tv.setText(message);
        tv.setTextSize(18);

        //lp.setMargins(0, 15, 0, 0);
        callername.setLayoutParams(lp);
        callername.setText(senderName);
        callername.setTextSize(14);

        space.setLayoutParams(lp);
        space.setTextSize(10);

        tv.setPadding(20, 10, 20, 10);
        tv.setBackgroundColor(Color.parseColor("#999999"));
        tv.setTextColor(Color.parseColor("#ffffff"));

        callername.setTextColor(Color.parseColor("#999999"));

        // Add newly created TextView to parent view group (RelativeLayout)
        ll.addView(space);
        ll.addView(callername);
        ll.addView(tv);
    }



}
