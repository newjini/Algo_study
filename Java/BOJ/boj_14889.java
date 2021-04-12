package com.ssafy.hw;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_14889_2 { // 스타트와 링크

	static int N;
	static int[][] matrix;
	static int[] idxStart; // 스타트팀 인덱스
	static int[] idxLink; // 링크팀 인덱스

	static boolean[] isSelected; // idxStart 아닌 것이 idxLink
	static int[] idx = new int[2];
	
	static int leng;
	static int starts, links; // 시너지 합
	static int res;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		matrix = new int[N][N];
		leng = N / 2;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		idxStart = new int[leng];
		isSelected = new boolean[N];
		res = Integer.MAX_VALUE;
		combi(0, 0); // cnt : 0, start : 0
		System.out.println(res);
	}

	private static void combi(int cnt, int start) {
		// 기저조건
		if (cnt == leng) {
			starts = 0;
			links = 0;
			int idx = 0;
			idxLink = new int[leng];
			for (int i = 0; i < N; i++) {
				if (!isSelected[i]) {
					idxLink[idx++] = i;
				}
			}
			pickPosition(0, 0);

			res = Math.min(res, Math.abs(starts - links));

			return;
		}

		for (int i = start; i < N; i++) {

			idxStart[cnt] = i;
			isSelected[i] = true;
			combi(cnt + 1, i + 1);
			isSelected[i] = false;

		}
	}

	private static void pickPosition(int cnt, int start) {

		if (cnt == 2) {
			int i = 0, j = 1;
			i = idx[0];
			j = idx[1];
			starts += matrix[idxStart[i]][idxStart[j]] + matrix[idxStart[j]][idxStart[i]];
			links += matrix[idxLink[i]][idxLink[j]] + matrix[idxLink[j]][idxLink[i]];
			return;
		}

		for (int i = start; i < leng; i++) {

			idx[cnt] = i;
			pickPosition(cnt + 1, i + 1);
		}
	}

}
