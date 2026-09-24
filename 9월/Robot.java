import java.util.Queue;
import java.util.ArrayDeque;

class Solution {
    public int solution(String[] board) {
        int R = board.length;
        int C = board[0].length();
        
        boolean[][]visited = new boolean[R][C];
        Queue<int []> queue = new ArrayDeque<>();
        
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r].charAt(c) == 'R') {
                    queue.offer(new int[]{r, c, 0});
                    visited[r][c] = true; // 시작 위치 방문 처리
                    break;
                }
            }
        }
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        
        while(!queue.isEmpty()){
            int []curr = queue.poll();
            int x = curr[0];
            int y = curr[1];
            int count = curr[2];
            
            if (board[x].charAt(y) == 'G'){
                return count;
            }
            
            for(int i=0;i<4;i++){
                int nx = x;
                int ny = y;
                
                while(nx+ dx[i]>=0 && nx+dx[i] < R && ny+dy[i]>=0 && ny+dy[i]<C
                     && board[nx + dx[i]].charAt(ny + dy[i]) != 'D'){
                    nx += dx[i];
                    ny += dy[i];
                }
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, count + 1});
                }
            }
        }
        return -1;    
    }
}