package implementation;

import java.io.*;
import java.util.*;

public class BOJ2504_괄호의값_W {
    // 잘못된 풀이였음

    static void solve(ArrayList<Character> str) {
        Stack<Character> st = new Stack<>();
        ArrayList<Character> arr = new ArrayList<>();

        for (int i = str.size() - 1; i >= 0; i--) {
            st.push(str.get(i));
        }
        while (st.size() > 1) {
            char now = st.pop();
            char next = st.peek();
            System.out.println("now " + now + " next " + next);
            if (now == '(' && next == ')') {
                st.pop();
                arr.add('2');
            } else if (now == '[' && next == ']') {
                st.pop();
                arr.add('3');
            } else if (Character.isDigit(now) && Character.isDigit(next)) {
                int num = Character.getNumericValue(now);
                int num2 = Character.getNumericValue(next);
                st.pop();
                arr.add(Character.forDigit(num+num2, 10));
            } else if (Character.isDigit(next)) {
                int num = Character.getNumericValue(next);
                st.pop(); // 숫자 빼기
                char next2 = st.peek();
                if (now == '(' && next2 == ')') {
                    st.pop();
                    num *= 2;
                    arr.add(Character.forDigit(num, 10));
                } else if (now == '[' && next2 == ']') {
                    st.pop();
                    num *= 3;
                    System.out.println(num);
                    arr.add(Character.forDigit(num, 10));
                } else if (Character.isDigit(next2)) {
                    int num2 = Character.getNumericValue(st.pop());
                    arr.add(now);
                    arr.add(Character.forDigit(num+num2, 10));
                } else {
                    arr.add(now);
                    arr.add(next);
                }
            } else {
                arr.add(now);
            }
        }
        for (int i = 0; i < st.size(); i++) {
            System.out.println("stack : "+st.get(i));
        }
        while(!st.isEmpty()){
            arr.add(st.pop());
        }
        for (int i = 0; i < arr.size(); i++) {
            System.out.print(arr.get(i) + " ");
        }
        System.out.println();
        if (arr.size() > 1) {

            solve(arr);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        ArrayList<Character> strArr = new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {
            strArr.add(str.charAt(i));
        }
        solve(strArr);
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