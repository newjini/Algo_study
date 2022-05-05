package bruteForth;

import java.io.*;
import java.util.*;

public class BOJ1107_리모컨 {

    private static String N;
    private static String now = "100";
    private static boolean[] nums;
    private static int cnt;


    static void solve() {
        int leng = N.length();
        if(now.equals(N)){
            cnt = 0;
            return;
        }
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < leng; i++) {
            int btn = N.charAt(i) - '0';
            if(!nums[btn]){
                sb.append(btn);
            }
            else{
                System.out.println(btn);
                int num1 = btn;
                int num2 = btn;

                while(num1 > 0) {
                    num1--;
                    if(!nums[num1]){
                        System.out.println("num1 : "+num1);
                        break;
                    }
                }
                while(num2 < 9){
                    num2++;
                    System.out.println("num2 : "+num2);
                    if(!nums[num2]) {
                        break;
                    }
                }
                if(num1 == 0){
                    sb.append(num2);
                }else if(num2 == 0){
                    sb.append(num1);
                }else{
                    sb.append(Math.min(num1, num2));
                }
            }
        }
        System.out.println(sb);
        cnt = sb.length() + Math.abs(Integer.parseInt(String.valueOf(sb)) - Integer.parseInt(N));

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
        solve();
        System.out.println(cnt);
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
