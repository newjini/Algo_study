package implementation;

import java.io.*;
import java.util.*;

public class BOJ17413_단어뒤집기2 {

    /* 스택 이용 */

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int leng = input.length();
        Stack<Character> st = new Stack<>();

        boolean check = false; // false: 반대로 , true: 그대로 출력
        StringBuffer res = new StringBuffer();
        for (int i = 0; i < leng; i++) {
            char c = input.charAt(i);
            if(c == '<'){
                check = true; // 태그 안에 도착!
                while(!st.isEmpty()){ // 뒤집을 단어가 존재한다면
                    res.append(st.pop());
                }
                res.append(c);
            }else if(c == ' '){
                if(!check){ // 태그 밖의 띄어쓰기에 도착했다면,
                    while(!st.isEmpty()){
                        res.append(st.pop());
                    }
                    res.append(c);
                }else{
                    st.add(c);
                    continue;
                }
            }else if(c == '>'){ // 태그 안의 단어는 그대로 출력
                StringBuffer sb = new StringBuffer();
                while(!st.isEmpty()){
                    sb.append(st.pop());
                }
                res.append(sb.reverse()+">");
                check = false;
            }else{
                st.add(c);
            }
        }
        while(!st.isEmpty()){ // 뒤집을 단어가 존재한다면
            res.append(st.pop());
        }
        System.out.println(res);
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