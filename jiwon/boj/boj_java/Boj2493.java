package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Boj2493 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        String[] answer = new String[n];
        Arrays.fill(answer, "0");
        Deque<Integer> stack = new ArrayDeque<>();
        Deque<Integer[]> pop = new ArrayDeque<>();
        while (st.hasMoreTokens()) {
            stack.add(Integer.valueOf(st.nextToken()));
        }
        
        while (!stack.isEmpty()) {
            int num = stack.pollLast();
            n--;
            pop.addLast(new Integer[]{num, n});
            while (!stack.isEmpty() && !pop.isEmpty() && (stack.getLast() >= pop.getLast()[0])) {
                answer[pop.pollLast()[1]] = String.valueOf(n);
            }
        }
        System.out.println(String.join(" ", answer));
    }
}
