import java.util.*;

class Park {

    static boolean isCheck(String[][] box, int x, int y, int size) {
        int n = box.length;    // 세로 길이
        int m = box[0].length; // 가로 길이

        // 1. 돗자리가 공원 범위를 벗어나는지 확인
        if (x + size > n || y + size > m) {
            return false;
        }

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (!"-1".equals(box[x + i][y + j])) { // 자리가 이미 차있음
                    return false;
                }
            }
        }
        return true;
    }

    public int solution(int[] mats, String[][] park) {
        int answer = -1;

        Arrays.sort(mats); // 돗자리를 작은 것부터 큰 것 순으로 정렬
        for(int i=0;i<park.length;i++){
            for(int j=0 ; j< park[0].length;j++){
                if ("-1".equals(park[i][j])) { // 현재 위치가 빈 공간일 때만
                    // 각 돗자리 크기에 대해 확인
                    for (int matSize : mats) {
                        if (isCheck(park,i, j, matSize)) {
                            answer = Math.max(answer, matSize); // 가장 큰 돗자리 크기를 저장
                        }
                    }
                }
            }
        }
        return answer;
    }
}
