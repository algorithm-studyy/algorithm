package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj1780 {

    static int n;
    static int[][] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] result = recursive(0, 0, n);
        for (int i : result) {
            System.out.println(i);
        }
    }

    static boolean checkSame(int row, int col, int end) {
        int rowEnd = row + end;
        int colEnd = col + end;
        int compare = arr[row][col];
        for (int i = row; i < rowEnd; i++) {
            for (int j = col; j < colEnd; j++) {
                if (compare != arr[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    static int[] recursive(int row, int col, int end) {
        int[] result = new int[3];
        if (checkSame(row, col, end)) {
            result[arr[row][col] + 1]++;
            return result;
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int newEnd = end / 3;
                int[] adder = recursive(row + i * newEnd, col + j * newEnd, newEnd);
                sum(result, adder);
            }
        }
        return result;
    }

    static void sum(int[] base, int[] adder) {
        for (int i = 0; i < base.length; i++) {
            base[i] += adder[i];
        }
    }
}
