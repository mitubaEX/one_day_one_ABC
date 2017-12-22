import java.io.*;
import java.util.*;
import java.math.BigDecimal;

class Main {
    public void run() throws Exception {
        Scanner sc = new Scanner(System.in);
        double kakudo = sc.nextInt() / 10.0;
        String ansKakudo = "";
        if(11.25 <= kakudo && kakudo < 33.75){
            ansKakudo = "NNE";
        } else if(33.75 <= kakudo && kakudo < 56.25){
            ansKakudo = "NE";
        } else if(56.25 <= kakudo && kakudo < 78.75){
            ansKakudo = "ENE";
        } else if(78.75 <= kakudo && kakudo < 101.25){
            ansKakudo = "E";
        } else if(101.25 <= kakudo && kakudo < 123.75){
            ansKakudo = "ESE";
        } else if(33.75 <= kakudo && kakudo < 146.25){
            ansKakudo = "SE";
        } else if(33.75 <= kakudo && kakudo < 168.75){
            ansKakudo = "SSE";
        } else if(33.75 <= kakudo && kakudo < 191.25){
            ansKakudo = "S";
        } else if(33.75 <= kakudo && kakudo < 213.75){
            ansKakudo = "SSW";
        } else if(33.75 <= kakudo && kakudo < 236.25){
            ansKakudo = "SW";
        } else if(33.75 <= kakudo && kakudo < 258.75){
            ansKakudo = "WSW";
        } else if(33.75 <= kakudo && kakudo < 281.25){
            ansKakudo = "W";
        } else if(33.75 <= kakudo && kakudo < 303.75){
            ansKakudo = "WNW";
        } else if(33.75 <= kakudo && kakudo < 326.25){
            ansKakudo = "NW";
        } else if(33.75 <= kakudo && kakudo < 348.75){
            ansKakudo = "NNW";
        }else{
            ansKakudo = "N";
        }

        double w = sc.nextInt() / 60.0;
        BigDecimal bd = new BigDecimal(String.valueOf(w));
        BigDecimal bd2 = bd.setScale(1, BigDecimal.ROUND_HALF_UP);  //小数第２位
        double ans = bd2.doubleValue();
        String ansString = "";

        if(0.0 <= ans && ans <= 0.2){
            ansString = "0";
        } else if(0.3 <= ans && ans <= 1.5){
            ansString = "1";
        } else if(1.6 <= ans && ans <= 3.3){
            ansString = "2";
        } else if(3.4 <= ans && ans <= 5.4){
            ansString = "3";
        } else if(5.5 <= ans && ans <= 7.9){
            ansString = "4";
        } else if(8.0 <= ans && ans <= 10.7){
            ansString = "5";
        } else if(10.8 <= ans && ans <= 13.8){
            ansString = "6";
        } else if(13.9 <= ans && ans <= 17.1){
            ansString = "7";
        } else if(17.2 <= ans && ans <= 20.7){
            ansString = "8";
        } else if(20.8 <= ans && ans <= 24.4){
            ansString = "9";
        } else if(24.5 <= ans && ans <= 28.4){
            ansString = "10";
        } else if(28.5 <= ans && ans <= 32.6){
            ansString = "11";
        } else if(32.7 <= ans){
            ansString = "12";
        }
        if(ansString.equals("0")){
            ansKakudo = "C";
        }
        System.out.println(ansKakudo +" " + ansString);
    }

    public static void main(String... args) throws Exception{
        new Main().run();
    }
}
