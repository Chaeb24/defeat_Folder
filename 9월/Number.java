import java.util.Arrays;
import java.util.Stack;

class Solution {
    public int[] solution(int[] numbers) {
        int [] answer = new int[numbers.length]; //numbers 배열 길이 만큼 똑같이 만들기

        Stack<Integer>stack = new Stack<>(); // 인덱스 저장용 스택
        Arrays.fill(answer,-1); //-1로 다 채우기

        for(int i=0;i<numbers.length;i++){
            while(!stack.isEmpty()&&numbers[stack.peek()] < numbers[i]){
                int index = stack.pop();
                answer[index] = numbers[i];
            }
            stack.push(i);
        }
    
        return answer;
    }
}