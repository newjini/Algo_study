

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_15961 { // 회전초밥
	
	static int N, d, k, c;
	static int[] arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken()); // 접시 수
		d = Integer.parseInt(st.nextToken()); // 초밥 가짓 수
		k = Integer.parseInt(st.nextToken()); // 연속해서 먹는 접시 수
		c = Integer.parseInt(st.nextToken()); // 쿠폰 번호
		
		arr = new int[N];
		
		int sushi = 0;
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			
		}
		int[] count = new int[d+1];
		sushi++; // 전체 초밥 가짓수 세는거
		int res = 0;
		boolean first = true;
		count[c]++; // 이미 먹은 쿠폰 번호 초밥
		// 연속해서 먹을 수 있는 초밥 찾기
		for(int i=0; i<N;i++) {
			// 처음에만 들어오기
			if(first == true) {
				first = false;
				for(int j=i; j<k;j++) {
					int idx = arr[j];
					if(count[idx] == 0) {
						sushi++;
					}
					count[idx]++;
				}
			}
			else {
				// 첫번째 빼고 가짓수 세기
				int front = arr[((i+N)%N)-1];
				if(count[front] == 1) { // 초밥 종류 한 개 삭제
					sushi--;
				}	
				count[front]--;
				
				// 마지막 껴주고 가짓수 세기
				int tail = arr[(i+k-1+N)%N];
				if(count[tail] == 0) { // 없던 초밥 종류라면 가짓수 추가
					sushi++;
				}
				count[tail]++;
			}
			res = Math.max(res, sushi);
		}
		
		System.out.println(res);
	}

}
