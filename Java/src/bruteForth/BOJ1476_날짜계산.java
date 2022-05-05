package bruteForth;

import java.io.*;
import java.util.*;

public class BOJ1476_날짜계산 {

    private static int E;
    private static int S;
    private static int M;


    static void solve() {
        int idx = 1;
        while(true){

            int calE = idx % 15;
            int calS = idx % 28;
            int calM = idx % 19;
            if(calE == 0)
                calE = 15;
            if(calS == 0)
                calS = 28;
            if(calM == 0)
                calM = 19;
            if(calE == E && calS == S && calM == M)
                break;
            idx++;
        }
        System.out.println(idx);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        E = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        solve();
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
