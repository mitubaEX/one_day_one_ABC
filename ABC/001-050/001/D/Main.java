import java.io.*;
import java.util.*;

class Time{
    int before, after;
    public Time(int before, int after){
        this.before = before;
        this.after = after;
    }
}

class Main {
    public String normarize(int s){
        String str = String.valueOf(s);
        String ans = "";

        for(int i = 0;i < 4 - str.length(); i++){
            ans += "0";
        }
        return ans + str;
    }

    public void run() throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Time> list = new ArrayList<>();
        List<Time> ansList = new ArrayList<>();


        for(int i = 0; i < n; i++){
            String[] args = sc.next().split("-");
            if(Integer.parseInt(args[1]) % 5 == 0){
                list.add(new Time(Integer.parseInt(args[0].substring(0,1)) * 60 + Integer.parseInt(args[0].substring(2,3)) - Integer.parseInt(args[0]) % 5, Integer.parseInt(args[1].substring(0,1)) * 60 + Integer.parseInt(args[1].substring(2,3))));
            }else{
                list.add(new Time(Integer.parseInt(args[0].substring(0,1)) * 60 + Integer.parseInt(args[0].substring(2,3)) - Integer.parseInt(args[0]) % 5, Integer.parseInt(args[1].substring(0,1)) * 60 + Integer.parseInt(args[1].substring(2,3)) + (5 - Integer.parseInt(args[1]) % 5)));
            }
        }



        list.sort((a, b) -> a.before - b.before);
        ansList.add(list.get(0));
        for (Time time: list.subList(1, list.size())){
            boolean flag = true;
            for(Time t: ansList){

                // いまリストに入っているやつ
                if(t.after <= time.after && t.after >= time.before){
                    ansList.set(ansList.indexOf(t), new Time(t.before, time.after));
                    flag = false;
                } else if(t.before == time.before && t.after == time.after){
                    flag = false;
                } else if(t.before <= time.before && t.after >= time.after){
                    flag = false;
                }
            }
            if(flag){
                ansList.add(time);
            }
        }
        for(Time time: ansList){
            System.out.println(normarize(time.before / 60 * 100 + time.before % 60) + "-" + normarize(time.after / 60 * 100 + time.after % 60));
        }
    }

    public static void main(String... args) throws Exception{
        new Main().run();
    }
}
