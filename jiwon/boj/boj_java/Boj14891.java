package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Boj14891 {

    private static LinkedList<Character>[] wheels = new LinkedList[4];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 4; i++) {
            wheels[i] = new LinkedList<>();
            for (char c : br.readLine().toCharArray()) {
                wheels[i].add(c);
            }
        }

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken()) - 1;
            int direction = Integer.parseInt(st.nextToken());
            rotateWheels(idx, direction);
        }
        System.out.println(getResult());
    }

    private static void rotateWheels(int idx, int direction) {
        int leftDir = 0;
        int rightDir = 0;

        if (idx == 1 || idx == 2) {
            if (wheels[idx - 1].get(2) != wheels[idx].get(6)) {
                leftDir = direction * -1;
            }
            if (wheels[idx + 1].get(6) != wheels[idx].get(2)) {
                rightDir = direction * -1;
            }
        } else if (idx == 0) {
            if (wheels[idx].get(2) != wheels[idx + 1].get(6)) {
                rightDir = direction * -1;
            }
        } else if (idx == 3) {
            if (wheels[idx].get(6) != wheels[idx - 1].get(2)) {
                leftDir = direction * -1;
            }
        }
        rotate(idx, direction);
        if (leftDir != 0) {
            rotateWheels(idx - 1, leftDir);
        }
        if (rightDir != 0) {
            rotate(idx + 1, rightDir);
        }
    }

    private static void rotate(int idx, int direction) {
        if (direction == 1) {
            Character removedItem = wheels[idx].pollLast();
            wheels[idx].addFirst(removedItem);
        } else if (direction == -1) {
            Character removedItem = wheels[idx].pollFirst();
            wheels[idx].addLast(removedItem);
        }
    }

    private static int getResult() {
        int result = 0;
        for (int i = 0; i < wheels.length; i++) {
            LinkedList<Character> wheel = wheels[i];
            result += Character.getNumericValue(wheel.get(0)) << i;
        }
        return result;
    }
}
