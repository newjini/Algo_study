package BFS;
import java.util.LinkedList;
import java.util.Queue;

public class prog_카카오프렌즈컬러링북 {

	public static void main(String[] args) {

	}

}


class Solution {
    
    static boolean[][] visited;
    static int[] dy = { -1, 0, 0, 1};
    static int[] dx = {0, -1, 1, 0};
    static int M;
    static int N;
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        visited = new boolean[m][n];
        M = m;
        N = n;
        int cnt = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(picture[i][j] != 0 && !visited[i][j]){
                    numberOfArea++;
                    int ans = BFS(i,j, picture);
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, ans);
                }        
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    public int BFS(int y, int x, int[][] picture){
        int cnt = 1;
        visited[y][x] = true;
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(new Point(y,x));
        while(!queue.isEmpty()){
            Point p = queue.poll();
            int nowy = p.y;
            int nowx = p.x;
            for(int k=0;k<4;k++){
                int nexty = nowy + dy[k];
                int nextx = nowx + dx[k];
                if(nexty >=0 && nexty < M && nextx >= 0 && nextx < N){
                    if(!visited[nexty][nextx] && picture[nexty][nextx] == picture[nowy][nowx]){
                        queue.offer(new Point(nexty, nextx));
                        visited[nexty][nextx] = true;
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
}
class Point{
    int y;
    int x;
    public Point(int y, int x) {
        this.y = y;
        this.x = x;
    }
}