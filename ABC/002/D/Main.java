import java.io.*;
import java.util.*;

class Main {
    int n;
    int[][] map;
    int count = 0;
    public void solve(int nowy, int[][] arriveMap, int nowCount){
        boolean flag = true;
        for(int i = 0; i < n; i++){
            if(map[nowy][i] == 1 && arriveMap[nowy][i] != 1 && arriveMap[i][nowy] != 1){
                flag = false;
                arriveMap[nowy][i] = 1;
                System.out.println(nowy + "," + i);
                solve(i, arriveMap, nowCount + 1);
            }
        }
        if(flag){
            count = Math.max(count, nowCount);
            System.out.println();
            return;
        }
    }

    public int[][] changeArray(int[][] array){
        int[][] tmp = new int[n][n];
        for(int i = 0;i < n; i++){
            for(int j = 0; j < n; j++){
                tmp[i][j] = array[i][j];
            }
        }
        return tmp;
    }

    public void run() throws Exception {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        map = new int[n][n];
        int m = sc.nextInt();
        for(int i = 0;i < m; i++){
            int a = sc.nextInt()-1;
            int b = sc.nextInt()-1;
            map[a][b] = 1;
            map[b][a] = 1;
        }
        for(int i = 0;i < n; i++){
            for(int j = 0; j < n; j++){
                if(map[i][j] == 1){
                    System.out.println(i + ":y");
                    int[][] tmp = new int[n][n];
                    tmp[i][j] = 1;
                    solve(i, changeArray(tmp), 0);
                }
            }
        }
        System.out.println(count);
    }

    public static void main(String... args) throws Exception{
        new Main().run();
    }
}
