class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;

        for (int i = 0; i < schedules.length; i++) {
        
            int promised = schedules[i] + 10;
            int hour = promised / 100;
            int minute = promised % 100;
            
            if (minute >= 60) {
                hour++;
                minute -= 60;
            }
            promised = hour * 100 + minute;

            // 이 직원이 조건을 만족했는지 나타내는 플래그 변수
            boolean isSuccess = true;

            for (int j = 0; j < timelogs[i].length; j++) {
                int currentDay = (startday - 1 + j) % 7 + 1;

                if (currentDay == 6 || currentDay == 7) {
                    continue;
                }

                if (timelogs[i][j] > promised) {
                    isSuccess = false;
                    break; 
                }
            }

            if (isSuccess) {
                answer++;
            }
        }

        return answer;
    }
}