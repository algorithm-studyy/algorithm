package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Boj1475 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[10];
        String s = br.readLine();
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - '0']++;
        }

        int max_val = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i != 6 && i != 9 && max_val < arr[i]) {
                max_val = arr[i];
            }
        }
        System.out.println(Math.max((arr[6] + arr[9] + 1) / 2, max_val));
    }
}
