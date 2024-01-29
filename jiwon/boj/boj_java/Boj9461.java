package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Boj9461 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inputArr = new int[Integer.parseInt(br.readLine())];
        long[] arr = new long[105];
        for (int i = 0; i < inputArr.length; i++) {
            inputArr[i] = Integer.parseInt(br.readLine()) - 1;
        }

        int maxValue = Arrays.stream(inputArr).max().getAsInt();

        // dp[i] = dp[i - 2] + dp[i - 3]
        arr[0] = 1;
        arr[1] = 1;
        arr[2] = 1;
        for (int i = 3; i <= maxValue; i++) {
            arr[i] = arr[i - 2] + arr[i - 3];
        }

        for (int input : inputArr) {
            System.out.println(arr[input]);
        }
    }
}
