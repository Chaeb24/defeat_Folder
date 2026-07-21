import java.util.*;

class message {
    public int solution(String message, int[][] spoilers) {
        //스포일러 위치 표시
        boolean[] isSpoiler = new boolean[message.length()];

        //시작과 끝 인덱스 찾아서 true 표시
        for(int [] spoiler : spoilers){
            for(int i = spoiler[0];i<=spoiler[1];i++){
                isSpoiler[i] = true;
            }
        }

        Set<String> normalWords = new HashSet<>();
        List<String> spoilerWords = new ArrayList<>();

        int idx = 0;

        while(idx < message.length()){

            while(idx < message.length() && message.charAt(idx) == ' '){
                idx++;
            }

            if(idx >= message.length()) break;

            int start = idx;

            while(idx < message.length() && message.charAt(idx) != ' '){
                idx++;
            }

            int end = idx - 1;

            String word = message.substring(start,idx);

            boolean containsSpoiler = false;

            for(int i=start; i<=end; i++){
                if(isSpoiler[i]){
                    containsSpoiler = true;
                    break;
                }
            }

            if(containsSpoiler){
                spoilerWords.add(word);
            }else{
                normalWords.add(word);
            }
        }
        Set<String> importantWords = new HashSet<>();

        for(String word : spoilerWords){
            if(!normalWords.contains(word)){
                importantWords.add(word);
            }
        }
        return importantWords.size();
    }
}