package implementation;

import java.io.*;
import java.util.*;

public class BOJ2504_괄호의값 {
    static String str;
    static int answer;

    static void solve() {
        int leng = str.length();
        int res = 0;
        int tmp = 1;
        boolean wrong = false;
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < leng; i++) {
            switch (str.charAt(i)) {
                case '(':
                    stack.push('(');
                    tmp *= 2;
                    break;
                case ')':
                    if (stack.isEmpty() || stack.peek() != '(') {
                        wrong = true;
                        break;
                    }
                    if (stack.peek() == '(') {
                        stack.pop();
                        if (i > 0 && str.charAt(i - 1) == '(') {
                            res += tmp;
                        }
                        tmp /= 2;
                        break;
                    }
                case '[':
                    stack.push('[');
                    tmp *= 3;
                    break;
                case ']':
                    if (stack.isEmpty() || stack.peek() != '[') {
                        wrong = true;
                        break;
                    }
                    if (stack.peek() == '[') {
                        stack.pop();
                        if (i > 0 && str.charAt(i - 1) == '[') {
                            res += tmp;
                        }
                        tmp /= 3;
                        break;
                    }
            }
        }
        if(wrong || !stack.isEmpty()){
            answer = 0;
        }else{
            answer = res;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        solve();
        System.out.println(answer);
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