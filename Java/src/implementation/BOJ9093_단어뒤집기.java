package implementation;

import java.io.*;
import java.util.*;

public class BOJ9093_단어뒤집기 {

    static void solve() {

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] str = br.readLine().split(" ");
            int sleng = str.length;
            Stack<String> stack = new Stack();
            for (int j = 0; j < sleng; j++) {
                stack.add(str[j]);
            }
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < sleng; j++) {
                String s = str[j];
                int sl = s.length();
                for (int k = sl-1; k >= 0; k--) {
                    sb.append(s.charAt(k));
                }
                sb.append(" ");
            }
            System.out.println(sb);
        }
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
