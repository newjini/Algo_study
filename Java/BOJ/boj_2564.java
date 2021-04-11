package box_0413;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2564 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int R = Integer.parseInt(st.nextToken()); // 가로 길이
		int C = Integer.parseInt(st.nextToken()); // 세로 길이
		int N = Integer.parseInt(br.readLine());	// 상점 갯수
		int map[][] = new int[N+1][2];
		int idx[] = new int[N+1];
		for(int i=0; i<N+1; i++) {
			st = new StringTokenizer(br.readLine()," ");
			map[i][0] = Integer.parseInt(st.nextToken());
			map[i][1] = Integer.parseInt(st.nextToken());
			
			if(map[i][0] == 1) { // 북쪽이면,
				idx[i] = map[i][1];
			}else if(map[i][0] == 2) { // 남쪽이면,
				idx[i] = R+C+(R-map[i][1]);
			}else if(map[i][0] == 3) { // 서쪽이면,
				idx[i] = R*2 + C + (C-map[i][1]);
			}else if(map[i][0] == 4) { // 동쪽이면,
				idx[i] = R + map[i][1];
			}
		}
		int res = 0;
		for(int i=0;i<N;i++) {
			int sum = Math.abs(idx[i] - idx[N]);
			res += Math.min(sum, R*2+C*2-sum);
		}
		System.out.println(res);

		
		
	}

}
