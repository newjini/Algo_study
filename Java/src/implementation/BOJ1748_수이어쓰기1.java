package implementation;

import java.io.*;
import java.util.*;

public class BOJ1748_수이어쓰기1 {
    static int leng;
    static int N;

    static int solve() {
        int maxi = leng - 1;
        int cnt = 0;
        for(int i=0; i<maxi; i++){
            cnt += Math.pow(10, i) * 9 * (i+1);
        }
        cnt += (N - Math.pow(10, maxi) + 1) * leng;

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        leng = s.length();
        N = Integer.parseInt(s);
        System.out.println(solve());

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