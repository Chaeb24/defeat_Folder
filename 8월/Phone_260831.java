import java.util.Arrays;

public class Phone_260831 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;

        Arrays.sort(phone_book);

        for(int i=0;i< phone_book.length-1;i++) {
            String compare = phone_book[i];
            if(phone_book[i+1].startsWith(phone_book[i])){
                answer = false;
            }
        }

        return answer;
    }
}
