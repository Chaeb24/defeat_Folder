class Attack_260827{
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int maxHealth = health;

        //공격 마지막 초까지 계산
        for(int i=0;i<attacks.length;i++){
            health -= attacks[i][1];
            // 캐릭터 죽음
            if(health<=0){
                return -1;
            }
        //공격이 끝난 경우 for문 빠져나옴.
            if(i == attacks.length-1){
                break;
            }

            int cnt = 1;
            int time = attacks[i][0] + 1;

            while(time < attacks[i+1][0]){
                health += bandage[1];
                //특정 시간에 도달시, 풀 충전 됨.
                if(cnt == bandage[0]){
                    health += bandage[2];
                    cnt = 0; // 카운트 초기화
                }

                if(health>maxHealth){
                    health = maxHealth;
                }

                cnt++;
                time++;
            }

        }
        answer = health;
        return answer;
    }
}
