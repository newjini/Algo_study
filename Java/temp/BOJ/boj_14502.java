package box_0326;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_14502 { // BOJ 14502 : 연구소

	static int N, M; // n : 가로, m : 세로
	static int cnt = Integer.MAX_VALUE;  // 최소로 퍼진 바이러스 개수
	static int[][] arr;  // 연구소 배열
	static int[][] original; // 연구소 원래 배열 ( 매번 벽 세울때마다 갱신해줘야함 )
	static Point[] point; // 벽 세울 수 있는 좌표 저장

	// 3개의 벽 좌표 조합으로 뽑기
	static boolean[] isSelected;
	static int[] numbers;
	static int idx;
	
	// BFS 할 때
	static int[] dy = { -1, 0, 0, 1};
	static int[] dx = {0, -1, 1, 0};
	static boolean[][] visited;
	static Queue<Point> q = new LinkedList<Point>();
	static ArrayList<Point> virus;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		original = new int[N][M];
		point = new Point[N*M];
		virus = new ArrayList<Point>();
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				original[i][j] = arr[i][j];
				if(arr[i][j] == 0) { // 벽 세울 수 있는 위치 저장
					point[idx++] = new Point(i,j);
				}
				else if(arr[i][j] == 2) { 
					q.offer(new Point(i,j)); // 큐에 바이러스 위치 저장
					virus.add(new Point(i,j)); // 바이러스 위치 저장
				}
			}
		}
		
		// 벽 3개 고르기
		int start = 0, count = 0;
		isSelected = new boolean[N*M];
		numbers = new int[N*M];
		pickWall(count, start);
		
		System.out.println(idx - 3 - cnt); // 최대 안전영역 : 0 개수 - 세운 벽 개수(3개) - 퍼진바이러스개수
		
	}


	private static void pickWall(int count, int start) {
		// 기저조건
		if(count == 3) {
			for(int i=0;i<3;i++) {
				Point p = point[numbers[i]];
				arr[p.x][p.y] = 1; // 벽 세우고 안전영역 탐색하기
			}
			
			// 초기화 해주기
			for(int i=0; i<virus.size(); i++) {
				q.offer(virus.get(i)); // 매번 BFS 하기 전 큐 상태 초기화 ( 기존 바이러스 위치만 들어있는 )
			}
			
			visited = new boolean[N][M];
			cnt = Math.min(cnt, BFS()); // 제일 쪼끔 퍼진 바이러스 갯수
			
			for(int i=0;i<N;i++) {
				for(int j=0;j<M;j++) {
					arr[i][j] = original[i][j]; // 매번 벽 3개 세우기 전으로 돌아가기
				}
			}
			return;
		}
		
		for(int i=start; i<idx; i++) {
			
			isSelected[i] = true;
			numbers[count] = i;
			pickWall(count+1, start+1);
			isSelected[i] = false;
			
			
		}
		
	}

	private static int BFS() {
		int res = 0;		// 쪼끔 퍼진 바이러스 찾기 위한 count
		
		while(!q.isEmpty()) {
			Point now = q.poll();
			int nowy = now.x;
			int nowx = now.y;
			for(int i=0;i<4;i++) {
				int ny = nowy+dy[i];
				int nx = nowx+dx[i];
				if(ny >=0 && ny < N && nx >=0 && nx < M) {
					if(!visited[ny][nx] && arr[ny][nx] == 0) {
						visited[ny][nx] = true;
						arr[ny][nx] = 2;
						q.offer(new Point(ny,nx));
						res++;
					}
				}
			}
		}
		return res;
		
		
	}

}

// class Point{
//	int x, y;
//
//	public Point(int x, int y) {
//		super();
//		this.x = x;
//		this.y = y;
//	}
//
//	
//}