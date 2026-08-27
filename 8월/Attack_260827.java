class Attack_260827{
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int maxHealth = health;

        //공격 마지막 초까지 계산
        for(int i=0;i<attacks.length;i++){
            health -= attacks[i][1];
            // 캐릭터 죽음
            if(health<0){
                return -1;
            }
        //공격이 끝난 경우 for문 빠져나옴.
            if(i == attacks.length-1){
                break;
            }

        }
        return answer;
    }
}
