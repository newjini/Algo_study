import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj_7576 {

	static int[] dy = { -1, 0, 0, 1 };
	static int[] dx = { 0, -1, 1, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int M = Integer.parseInt(st.nextToken()); // 가로 길이 [열]
		int N = Integer.parseInt(st.nextToken()); // 세로 길이 [행]
		int[][] map = new int[N][M];
		boolean[][] visited = new boolean[N][M];

		int cnt = 0; // 맨처음에 주어진 익은 토마토 세기
		int empty = 0; // 없는 토마토 체크
		int result = Integer.MIN_VALUE;
		Queue<Point> queue = new LinkedList<Point>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1) { // 익은 토마토 만날때마다 큐에 넣어주기
					cnt++;
					queue.offer(new Point(i, j));
				} else if (map[i][j] == -1) { // 비어있는 거 세기
					empty++;
				}
			}
		}
		if (cnt == N * M - empty) { // 이미 토마토가 모두 익어있다면 0
			result = 0;
		}
		else {
			// BFS
			while (!queue.isEmpty()) {
				Point p = queue.poll();
				int nowy = p.y;
				int nowx = p.x;
				visited[nowy][nowx] = true;
				for (int i = 0; i < 4; i++) {
					int nexty = nowy + dy[i];
					int nextx = nowx + dx[i];
					if (nexty >= 0 && nexty < N && nextx >= 0 && nextx < M) {
						if (!visited[nexty][nextx] && map[nexty][nextx] == 0) { // 방문 X && 안익은 토마토라면,
							map[nexty][nextx] = map[nowy][nowx] + 1; // 익은 토마토 값 + 1
							queue.add(new Point(nexty, nextx));
						}
					}
				}
	
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 0) { // 아직도 익지 못한 토마토가 있다면,
					result = -1;
					break;
				}
				result = Math.max(result, map[i][j]-1); // 최소 일수 따져야해서 map[i][j]-1
				
			}
			if(result==-1) { // 못 익은거 있으면 나와라
				break;
			}
		}

		System.out.println(result);

	}

}

class Point {
	int y;
	int x;

	public Point(int y, int x) {
		this.y = y;
		this.x = x;
	}

}
