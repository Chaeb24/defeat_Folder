class Solution {

    static boolean isCheck(String[][]park, int x, int y, int size){
    int n = park.length; //세로
    int m = park[0].length; //가로

    //돗자리가 경계를 넘는가?
    if(x + size > n || y + size > m){
        return false;
    }
    
    // 해당 영역에 돗자리를 깔아도 되는가 
    for(int i = 0; i< size;i++){
        for(int j = 0; j< size ;j++){
            if(!("-1").equals(park[x+i][y+j])){
                return false;
            }
        }
    }
    return true;
}


    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        int width = park.length;
        int height = park[0].length;
        return answer;
    }
}
