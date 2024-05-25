package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Boj14888 {

    private static int[] array;
    private static int[] op;
    private static int limit;
    private static int max = Integer.MIN_VALUE;
    private static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        array = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        op = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        limit = Arrays.stream(op).sum();
        dfs(0, array[0]);
        System.out.println(max);
        System.out.print(min);
    }

    private static void dfs(int depth, int value) {
        if (depth == limit) {
            max = Math.max(max, value);
            min = Math.min(min, value);
            return;
        }
        for (int i = 0; i < op.length; i++) {
            if (op[i] > 0) {
                op[i] -= 1;
                dfs(depth + 1, calculate(i, value, array[depth + 1]));
                op[i] += 1;
            }
        }
    }

    private static int calculate(int index, int a, int b) {
        switch (index) {
            case 0:
                return a + b;
            case 1:
                return a - b;
            case 2:
                return a * b;
            default:
                return a / b;
        }
    }
}
