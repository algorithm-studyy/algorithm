package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Boj2501 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] array = IntStream.rangeClosed(1, n)
            .filter(i -> n % i == 0)
            .toArray();
        if (k > array.length) {
            System.out.println(0);
        } else {
            System.out.println(array[k - 1]);
        }
    }
}
