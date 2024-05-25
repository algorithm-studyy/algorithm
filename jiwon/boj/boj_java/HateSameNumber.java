package boj_java;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class HateSameNumber {

    public static void main(String[] args) throws Exception {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3})));
    }

    public static int[] solution(int[] arr) {
        Deque<Integer> answer = new ArrayDeque<>();

        for (int item : arr) {
            if (!answer.isEmpty() && answer.peekLast() == item) {
                continue;
            }
            answer.add(item);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
