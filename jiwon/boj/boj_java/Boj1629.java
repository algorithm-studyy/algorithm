package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj1629 {

    static int a;
    static int b;
    static int c;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        System.out.println(recursive(a, b));

    }

    private static long recursive(long num, long e) {
        if (e == 1) {
            return num % c;
        }

        long result = recursive(num, e / 2);
        if (e % 2 == 1) {
            return result * result % c * a % c;
        }
        return result * result % c;
    }
}
