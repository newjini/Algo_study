package implementation;

import java.io.*;
import java.util.*;

public class BOJ3085_사탕게임 {
    static int N;
    static char[][] arr;
    static int[] dy = {0, 1};
    static int[] dx = {1, 0};
    static boolean[][] visited;


    static int solve(int a, int b) {
        int real = 0;

        for (int i = 0; i < 2; i++) {
            int nexty = a + dy[i];
            int nextx = b + dx[i];
            if (nexty < 0 || nexty >= N || nextx < 0 || nextx >= N)
                continue;
            if (arr[a][b] != arr[nexty][nextx] && !visited[nexty][nextx]) {
                // 1. swap
                swap(a, b, nexty, nextx);
                // 2. 가장 긴 부분 세기
                for (int aa = 0; aa < N; aa++) {
                    for (int bb = 0; bb < N; bb++) {
                        char start = arr[aa][bb];
                        int cntRow = 1;
                        int cntCol = 1;

                        for (int c = bb + 1; c < N; c++) {
                            if (start == arr[aa][c])
                                cntRow++;
                            else
                                break;
                        }
                        for (int c = aa + 1; c < N; c++) {
                            if (start == arr[c][bb])
                                cntCol++;
                            else
                                break;
                        }
                        real = Math.max(real, Math.max(cntRow, cntCol));
                    }
                }
                // 3. 원복 ( 다시 swap )
                swap(nexty, nextx, a, b);

                if (real == N)
                    return real;
            }
        }
        return real;
    }


    private static void swap(int y1, int x1, int y2, int x2) {
        char tmp = arr[y1][x1];
        arr[y1][x1] = arr[y2][x2];
        arr[y2][x2] = tmp;
    }

    public static void main(String[] args) throws IOException {
        // BufferedReader br = getBufferedReader();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new char[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited[i][j] = true;
                ans = Math.max(ans, solve(i, j));
                if (ans == N) {
                    System.out.println(ans);
                    return;
                }
            }
        }
        System.out.println(ans);

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