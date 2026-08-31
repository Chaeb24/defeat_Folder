import java.util.HashMap;
import java.util.Map;

public class Clothes_260831 {
    public int solution(String[][] clothes) {
        int answer = 1; //개수 카운트하기

        Map<String,Integer> map = new HashMap<>();
        for(int i=0 ; i<clothes.length;i++){ //종류별로 옷이 몇개인가?
            map.put(clothes[i][1],map.getOrDefault(clothes[i][1],0)+1);
        }

        for(String key: map.keySet()){
            answer *= map.get(key)+1; //안 입는 경우
        }

        answer -= 1; // 아무것도 안 입는 경우는 빼준다.
        return answer;
    }
}
