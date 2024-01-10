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
        int[] dirs = new int[4];
        dirs[idx] = direction;

        int leftIdx = idx;
        int rightIdx = idx;
        while (leftIdx > 0) {
            if (wheels[leftIdx].get(6) != wheels[leftIdx - 1].get(2)) {
                dirs[leftIdx - 1] = -dirs[leftIdx];
                leftIdx--;
            } else {
                break;
            }
        }
        while (rightIdx < 3) {
            if (wheels[rightIdx].get(2) != wheels[rightIdx + 1].get(6)) {
                dirs[rightIdx + 1] = -dirs[rightIdx];
                rightIdx++;
            } else {
                break;
            }
        }

        for (int i = 0; i < dirs.length; i++) {
            rotate(i, dirs[i]);
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
