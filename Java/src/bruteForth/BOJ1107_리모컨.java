package bruteForth;

import java.io.*;
import java.util.*;

public class BOJ1107_리모컨 {

    private static String N;
    private static String first = "100";
    private static boolean[] nums;

    static int solve() {
        int cnt = 0;

        if(first.equals(N)){
            return cnt;
        }
        int cal = 0;
        int min = Math.abs(Integer.parseInt(first) - Integer.parseInt(N));

        for (int i = 0; i < 10000000; i++) {
            boolean check = false;
            String now = Integer.toString(i);
            int leng = now.length();
            for (int j = 0; j < leng; j++) {
                if(nums[now.charAt(j) - '0']){
                    check = true;
                    break;
                }
            }
            if(!check){
                cal = Math.abs(i - Integer.parseInt(N)) + Integer.toString(i).length();
                min = Math.min(min, cal);
            }
        }
        cnt = min;
        return cnt;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = br.readLine();
        nums = new boolean[10];
        int no = Integer.parseInt(br.readLine());
        if(no != 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < no; i++) {
                nums[Integer.parseInt(st.nextToken())] = true;
            }
        }
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