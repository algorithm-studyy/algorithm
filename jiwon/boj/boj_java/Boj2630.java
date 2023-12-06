package boj_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Boj2630 {

    private static int n;
    private static int[][] paper;
    private static int[] result = new int[2];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        paper = new int[n][n];
        initData(br);
        recursive(0, 0, n);
        System.out.printf("%d%n%d", result[0], result[1]);
    }

    private static void initData(BufferedReader br) {
        IntStream.range(0, n)
            .forEach(i -> {
                try {
                    paper[i] = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            });
    }

    private static void recursive(int row, int col, int end) {
        if (checkSame(row, col, end)) {
            result[paper[row][col]]++;
            return;
        }
        int rowLimit = row + end;
        int colLimit = col + end;
        end = end / 2;
        for (int i = row; i < rowLimit; i += end) {
            for (int j = col; j < colLimit; j += end) {
                recursive(i, j, end);
            }
        }
    }

    private static boolean checkSame(int row, int col, int end) {
        int rowLimit = row + end;
        int colLimit = col + end;
        for (int i = row; i < rowLimit; i++) {
            for (int j = col; j < colLimit; j++) {
                if (paper[i][j] != paper[row][col]) {
                    return false;
                }
            }
        }
        return true;
    }
}
