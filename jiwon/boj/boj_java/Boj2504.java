package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Boj2504 {

    private static void solution(String line) {
        int result = 0;
        int num = 1;
        Deque<Character> deque = new ArrayDeque<>();
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == '[') {
                num *= 3;
                deque.add(c);
            } else if (c == '(') {
                num *= 2;
                deque.add(c);
            } else if (c == ']') {
                if (deque.isEmpty() || deque.getLast() != '[') {
                    System.out.println(0);
                    return;
                }
                result += line.charAt(i - 1) == '[' ? num : 0;
                deque.pollLast();
                num = num / 3;
            } else if (c == ')') {
                if (deque.isEmpty() || deque.getLast() != '(') {
                    System.out.println(0);
                    return;
                }
                result += line.charAt(i - 1) == '(' ? num : 0;
                deque.pollLast();
                num = num / 2;
            }
        }
        if (deque.isEmpty()) {
            System.out.println(result);
        } else {
            System.out.println(0);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        solution(line);
    }
}
