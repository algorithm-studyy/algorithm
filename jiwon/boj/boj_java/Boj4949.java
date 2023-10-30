package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Boj4949 {

    public static void checkBalance(String line) {
        Deque<String> deque = new ArrayDeque<>();
        for (String s : line.split("")) {
            if ("([".contains(s)) {
                deque.add(s);
            } else if (s.equals("]")) {
                if (deque.isEmpty() || !deque.getLast().equals("[")) {
                    System.out.println("no");
                    return;
                }
                deque.pollLast();
            } else if (s.equals(")")) {
                if (deque.isEmpty() || !deque.getLast().equals("(")) {
                    System.out.println("no");
                    return;
                }
                deque.pollLast();
            }
        }
        if (deque.isEmpty()) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }

    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while (true) {
            line = br.readLine().stripTrailing();
            if (line.equals(".")) {
                break;
            }
            checkBalance(line);
        }
    }
}
