package implementation;

import java.io.*;
import java.util.*;

public class BOJ1966_프린터큐 {
    static int T;
    static int N, M;
    static LinkedList<Node> list;

    private static class Node {
        int priority;
        int idx;
        public Node(int priority, int idx) {
            this.priority = priority;
            this.idx = idx;
        }
    }

    static int solve() {
        int cnt = 0;
        while (list.size() > 0) {
            int max = 0;
            for (int i = 0; i < list.size(); i++) {
                max = Math.max(max, list.get(i).priority);
            }
            for (int i = 0; i < list.size(); i++) {
                Node now = list.remove();
                if(now.priority == max ){
                    cnt++;
                    if(now.idx == M){
                        return cnt;
                    }
                    break;
                }
                else{
                    list.add(now);
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            list = new LinkedList<>();

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int pri = Integer.parseInt(st.nextToken());
                list.add(new Node(pri, j));
            }
            System.out.println(solve());
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
