package implementation;

import java.io.*;
import java.util.*;

public class BOJ2108_통계학 {
    static int N;
    static int[] arr; // 중앙값, 범위 위한 배열
    static int[] arr2;
    //    static Map<Integer, Integer> arr2; // 최빈값 위한 배열
    static int sum;
    static int[] res;

    static void solve() {
        // 1. 산술평균 계산
        res[0] = (int) Math.round((double) sum / (double) N);
        // 2. 중앙값 계산
        Arrays.sort(arr);
        res[1] = arr[N / 2];
        // 3. 최빈값 계산
        ArrayList<Integer> nums = new ArrayList<>();
        int cnt = 0;
        int cnt2 = 0;
        int idx = 0;
        for (int i = 0; i < 8001; i++) {
            if (arr2[i] > cnt) {
                nums = new ArrayList<>();
                cnt = arr2[i];
                idx = i; // 최빈값이 유일할 경우 최종 최빈값
                nums.add(idx);
            }
            else if(arr2[i] == cnt) { // 최빈값이 여러개일 경우
                nums.add(i);
                cnt2 = cnt;
            }
        }
        if (cnt == cnt2) {
            Collections.sort(nums);
            res[2] = nums.get(1) - 4000;
        } else {
            res[2] = idx - 4000;
        }
        // 4. 범위 계산
        res[3] = arr[N - 1] - arr[0];

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        arr2 = new int[8001];

        res = new int[4];
        int num = 0;

        for (int i = 0; i < N; i++) {
            num = Integer.parseInt(br.readLine());
            arr[i] = num;
            arr2[num + 4000]++;
            sum += arr[i];
        }
        solve();
        for (int i = 0; i < res.length; i++) {
            System.out.println(res[i]);
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