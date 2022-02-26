package com.ssafy.class6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class swea_1228 { // 암호문 1
	static int[] arr; 

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int t = 1; t <= 10; t++) {
			int n = Integer.parseInt(br.readLine()); // 원본 암호문의 길이
			LinkedList<Integer> list = new LinkedList<Integer>();
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");

			for (int i = 0; i < n; i++) {
				list.add(Integer.parseInt(st.nextToken())); // 원본 암호문
			}
			int m = Integer.parseInt(br.readLine()); // 명령어의 개수
			st = new StringTokenizer(br.readLine(), "I ");
			while (st.hasMoreTokens()) {
				int idx = Integer.parseInt(st.nextToken()); // 명령어가 붙여질 인덱스
				int leng = Integer.parseInt(st.nextToken());
				arr = new int[leng]; // 명령어 배열 생성
				for (int i = 0; i < leng; i++) {
					arr[i] = Integer.parseInt(st.nextToken()); // 배열 입력받고
				}
				for (int i = leng - 1; i >= 0; i--) {
					list.add(idx, arr[i]); // 뒤에꺼부터 붙이기 ( 순서대로 되기 위함 )
				}
			}
			System.out.print("#"+t+" ");
			for (int i = 0; i < 10; i++) {
				System.out.print(list.get(i) + " ");
			}
			System.out.println();
		}
	}
}
