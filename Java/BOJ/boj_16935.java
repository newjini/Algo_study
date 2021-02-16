package com.ssafy.hw;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_16935 {
	static int[][] arr;

	public static void main(String[] args) throws IOException { // 배열 돌리기3
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken()); // 행
		int M = Integer.parseInt(st.nextToken()); // 열
		int R = Integer.parseInt(st.nextToken()); // 연산 횟수
		arr = new int[N][M]; // 배열 값
		int[][] tarr = new int[N][M]; // 회전하기 전 원래 배열 넣은 임시 배열
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		st = new StringTokenizer(br.readLine());
		for (int c = 0; c < R; c++) {
			int type = Integer.parseInt(st.nextToken()); // 연산 타입 번호
			int garo = arr.length;
			int sero = arr[0].length;
			switch (type) {
			case 1: // 상하 반전
				for (int i = 0; i < garo / 2; i++) {
					for (int j = 0; j < sero; j++) {
						int temp = arr[i][j];
						arr[i][j] = arr[garo - 1 - i][j];
						arr[garo - 1 - i][j] = temp;
					}
				}
				break;
			case 2: // 좌우 반전
				for (int i = 0; i < garo; i++) {
					for (int j = 0; j < sero / 2; j++) {
						int temp = arr[i][j];
						arr[i][j] = arr[i][sero - 1 - j];
						arr[i][sero - 1 - j] = temp;
					}
				}
				break;
			case 3: // 오른쪽으로 90도 회전
				int[][] rarr = new int[sero][garo];
				for (int i = 0; i < sero; i++) {
					for (int j = 0; j < garo; j++) {
						rarr[i][j] = arr[garo - j - 1][i];
					}
				}
				arr = new int[sero][garo];
				for (int i = 0; i < sero; i++) {
					for (int j = 0; j < garo; j++) {
						arr[i][j] = rarr[i][j];
					}
				}
				break;
			case 4: // 왼쪽으로 90도 회전
				rarr = new int[sero][garo];
				for (int i = 0; i < sero; i++) {
					for (int j = 0; j < garo; j++) {
						rarr[i][j] = arr[j][sero - i - 1];
					}
				}
				arr = new int[sero][garo];
				for (int i = 0; i < sero; i++) {
					for (int j = 0; j < garo; j++) {
						arr[i][j] = rarr[i][j];
					}
				}
				break;
			case 5: // 1번 그룹 ->2번, 2번->3번, 3번->4번, 4번->1번
				int hn = garo / 2; // 행의 절반
				int hm = sero / 2; // 열의 절반
				tarr = new int[garo][sero];		// 회전하기 전 원래 배열 넣어놓은 임시 배열
				for (int i = 0; i < garo; i++) {
					for (int j = 0; j < sero; j++) {
						tarr[i][j] = arr[i][j];
					}
				}
				for (int i = 0; i < garo; i++) {
					for (int j = 0; j < sero; j++) {
						if (i < hn && j < hm) { // 1번  그룹
							arr[i][j + hm] = tarr[i][j];
						} else if (i < hn && j >= hm) { // 2번 그룹
							arr[i + hn][j] = tarr[i][j];
						} else if (i >= hn && j >= hm) { // 3번 그룹
							arr[i][j - hm] = tarr[i][j];
						} else if (i >= hn && j < hm) { // 4번 그룹
							arr[i - hn][j] = tarr[i][j];
						}
					}
				}

				break;
			case 6:
				hn = garo / 2; // 행의 절반
				hm = sero / 2; // 열의 절반
				tarr = new int[garo][sero];
				for (int i = 0; i < garo; i++) {
					for (int j = 0; j < sero; j++) {
						tarr[i][j] = arr[i][j];
					}
				}
				for (int i = 0; i < garo; i++) {
					for (int j = 0; j < sero; j++) {
						if (i < hn && j < hm) {
							arr[i + hn][j] = tarr[i][j];
						} else if (i < hn && j >= hm) {
							arr[i][j - hm] = tarr[i][j];
						} else if (i >= hn && j >= hm) {
							arr[i - hn][j] = tarr[i][j];
						} else if (i >= hn && j < hm) {
							arr[i][j + hm] = tarr[i][j];
						}
					}
				}

				break;
			}

		}
		for (int b = 0; b < arr.length; b++) {
			for (int bb = 0; bb < arr[0].length; bb++) {
				System.out.print(arr[b][bb] + " ");
			}
			System.out.println();
		}

	}

}
