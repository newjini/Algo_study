package implementation;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class BOJ1244_스위치켜고끄기 {

    static int N;
    static int[] onoff;
    static int student;

    private static void swap(int k){
        switch(onoff[k]){
            case 0:
                onoff[k] = 1;
                break;
            case 1:
                onoff[k] = 0;
                break;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        onoff = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            onoff[i] = Integer.parseInt(st.nextToken());
        }
        student = Integer.parseInt(br.readLine());

        for (int i = 0; i < student; i++) {
            st = new StringTokenizer(br.readLine());
            int man = Integer.parseInt(st.nextToken()); // 성별
            int where = Integer.parseInt(st.nextToken()); // 스위치 번호
            if (man == 1) {       // 남자인 경우,
                for (int j = 1; j <= N; j++) {
                    if (j % where == 0) {
                        swap(j-1);
                    }
                }
            } else {           // 여자인 경우,
                int idx = 1;
                int cnt = 0;
                where -= 1;
                boolean change = false;
                while (where - idx >= 0 && where + idx < N) {
                    if (onoff[where - idx] == onoff[where + idx]) {
                        change = true;
                        idx++;
                        cnt++;
                    } else
                        break;
                }
                if (change) {
                    for (int j = where - cnt; j <= where + cnt; j++) {
                        if (j >= 0 && j < N) {
                            swap(j);
                        }
                    }
                }
                else{
                    swap(where);
                }
            }

        }

        for (int i = 0; i < N; i++) {
            if(i!= 0 && i % 20 == 0){
                System.out.println();
            }
            System.out.print(onoff[i]+" ");
        }
    }

    private static BufferedReader getBufferedReader() throws IOException {
        System.out.println("===== input =====");
        String fileName = "Java/input/input1.txt";
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        BufferedReader br2 = new BufferedReader(new FileReader(fileName));
        String s;
        while ((s = br2.readLine()) != null) {
            System.out.println(s);
        }
        System.out.println("===== output =====");
        return br;
    }
}