package boj_java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


// 짝수 : n // 2
// 홀수 : n // 2 + 1
public class Boj2018 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int count = 1;
        int start = 1;
        int end = 1;
        long num = 1;
        while (end != n) {
            if (num > n) {
                num -= start;
                start += 1;
            } else if (num < n) {
                end += 1;
                num += end;
            } else {
                count += 1;
                end += 1;
                num += end;
            }
        }
        bw.write(String.valueOf(count));
        bw.flush();
    }
}
