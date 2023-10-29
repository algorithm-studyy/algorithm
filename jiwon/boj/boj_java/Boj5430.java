package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Boj5430 {

    static StringBuffer print = new StringBuffer();

    public static String[] preprocessingCommand(String command) {
        return Stream.of(command)
            .map(s -> s.replaceAll("RR", ""))
            .collect(Collectors.joining()).split("");
    }

    public static Deque<Integer> preprocessingDeque(String arrString) {
        Deque<Integer> result = new ArrayDeque<>();
        String[] arr = arrString.substring(1, arrString.length() - 1).split(",");
        for (String s : arr) {
            result.add(Integer.valueOf(s));
        }
        return result;
    }

    public static void solution(Deque<Integer> deque, String[] command) {
        char direction = 'L';
        for (String s : command) {
            if (s.equals("R")) {
                direction = direction == 'L' ? 'R' : 'L';
            } else if (s.equals("D")) {
                if (deque.isEmpty()) {
                    print.append("error\n");
                    return;
                }
                if (direction == 'L') {
                    deque.pollFirst();
                } else {
                    deque.pollLast();
                }
            }
        }
        print.append("[");
        if (direction == 'R') {
            while (!deque.isEmpty()) {
                print.append(deque.pollLast());
                if (deque.isEmpty()) {
                    break;
                }
                print.append(",");
            }
        } else {
            while (!deque.isEmpty()) {
                print.append(deque.pollFirst());
                if (deque.isEmpty()) {
                    break;
                }
                print.append(",");
            }
        }
        print.append("]\n");
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        Deque<Integer> deque;
        for (int i = 0; i < t; i++) {
            String[] command = preprocessingCommand(br.readLine().strip());
            int n = Integer.parseInt(br.readLine().strip());
            String listStr = br.readLine().strip();
            if (listStr.equals("[]")) {
                deque = new ArrayDeque<>();
            } else {
                deque = preprocessingDeque(listStr);
            }
            solution(deque, command);
        }
        System.out.print(print);
    }
}
