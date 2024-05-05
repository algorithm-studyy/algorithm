package boj_java;

import java.util.Arrays;

public class Budget {

    public static void main(String[] args) throws Exception {
        System.out.println(solution(new int[]{1, 3, 2, 5, 4}, 9));
    }

    public static int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for (int i : d) {
            if (budget >= i) {
                budget -= i;
                answer++;
            } else {
                break;
            }
        }
        return answer;
    }
}
