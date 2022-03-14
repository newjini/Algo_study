package implementation;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class BOJ1051_숫자정사각형 {
    static int N, M;
    static int mini;
    static int[][] arr;

    static int solve() {
        /*
        fori (mini-- >0 ) 으로 도는데,
        arr[i][j] 를 기준으로
        0,0   0,2
        2,0   2,2
        arr[i+mini][j] (좌하)
        arr[i][j+mini] (우상)
        arr[i+mini][j+mini] (우하)
        값이 다 같다면 끝.
        아니면 다음으로 넘어가
        mini값 줄이기
        경계범위 확인 필요
         */
        for (int k = mini-1; k > 0; k--) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int now = arr[i][j];
                    if(i+k >= N || j+k >= M)
                        continue;
                    if(now == arr[i][j+k] && now == arr[i+k][j] && now == arr[i+k][j+k]){
                        return (int)Math.pow(k+1, 2);
                    }
                }
            }
        }
        return 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        mini = Math.min(N, M);
        int answer = 1;
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j) - '0';
            }
        }

        answer = solve();
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