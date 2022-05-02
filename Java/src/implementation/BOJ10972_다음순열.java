package implementation;
import java.io.*;
import java.util.*;

public class BOJ10972_다음순열 {

    private static int N;
    private static int[] arr;


    public static void main(String[] args) throws IOException {
        BufferedReader br = getBufferedReader();
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        arr = new int[N];
        int[] arr2 = new int[N];        // 이미 내림차순 정렬 돼 있는 지 판단
        int[] reverseArr = new int[N];  // 내림차순 정렬 된 배열
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            arr2[i] = arr[i];
        }
        int cnt = 0;
        Arrays.sort(arr2);
        int idx = 0;
        for (int i = N-1; i >= 0; i--) {
            reverseArr[idx++] = arr2[i];
        }
        if(Arrays.equals(arr,reverseArr)){    // 이미 내림차순 정렬 돼 있으면 -1
            System.out.println(-1);
        }
        else{
            np(arr);                    // 이전 순열 찾기 시작.
            for (int i = 0; i < N; i++) {
                System.out.print(arr[i]+" ");
            }
        }

    }

    // 다음 순열이 있으면 true, 없으면 false
    private static boolean np(int[] arr) {

        // #1. max값 찾기. max(==i)를 통해 교환 위치(i-1) 찾기
        int i = N - 1;
        while( i>0 && arr[i] <= arr[i-1]) i--;
        if(i==0) return false;

        // #2. i-1 위치 값과 교환할 큰 값(j) 찾기
        int j = N - 1;
        while(arr[j] <= arr[i-1]) j--;

        // #3. i-1과 j 위치 값 교환
        swap(arr, i-1, j);

        // #4. max부터 맨 뒤까지 정렬
        int k = N - 1;
        while(i<k) swap(arr, i++, k--);

        return true;
    }

    private static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
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