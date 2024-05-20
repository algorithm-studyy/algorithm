package boj_java;

import static java.lang.Math.min;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Boj12852 {

    private static int n;
    private static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n + 1];
        Arrays.fill(arr, Integer.MAX_VALUE);
        arr[n] = 0;
        for (int i = n; i > 0; i--) {
            if (i % 3 == 0) {
                arr[i / 3] = min(arr[i] + 1, arr[i / 3]);
            }
            if (i % 2 == 0) {
                arr[i / 2] = min(arr[i] + 1, arr[i / 2]);
            }
            arr[i - 1] = min(arr[i] + 1, arr[i - 1]);
        }
        System.out.println(arr[1]);
    }
}
