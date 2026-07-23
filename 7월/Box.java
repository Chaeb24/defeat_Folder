class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0; //꺼내려는 상자의 개수
        int row = (num-1) / w; //꺼내려는 상자의 행
        int wid = w-1; //가로 인덱스
        int col = 0;
        
        //행이 짝수야
        if(row%2==0){
            col = (num-1) % w;
        }else{ //홀수 행이면
            col = wid - (num-1) % w;
        }

        int h = (n % w == 0) ? (n / w) : (n / w + 1); //층이 어디까지 쌓이는지

        for(;row < h; row++){
            int abovebox = 0;
            if(row % 2 == 0){
                abovebox = col + (row * w);
            }else{
                abovebox = (wid-col) + (row * w);
            }
            if(abovebox < n){
            answer ++;
            }
        }
        
        return answer;
    }
}