import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Runner_260828 {
    public String solution(String [] participant, String [] completion){
        String answer = "";

        Map<String,Integer> map = new HashMap<>(); //참여자명단, 참여자가 몇명인지 판단
        for(String player : participant)
            map.put(player, map.getOrDefault(player,0)+1); //참여자와 참여자 수를 기록
        for(String player: completion)
            map.put(player,map.get(player)-1); //참여자가 완주했다면 map에서 제거, 남은 참여자가 완주 못한 참여자임

        Iterator<Map.Entry<String,Integer>> iter = map.entrySet().iterator();

        while(iter.hasNext()){
            Map.Entry<String,Integer> entry = iter.next();

            if(entry.getValue() != 0){
                answer = entry.getKey();
                break;
            }
        }

        return answer;
    }
}
