package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj1244 {

    private static int n;
    private static int[] sw;
    private static final StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        sw = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            turn(s, p);
        }
        print();
        System.out.println(sb);
    }

    private static void turn(int s, int p) {
        if (s == 1) {
            int idx = p;
            while (idx < n) {
                sw[idx] = processing(idx);
                idx += p;
            }
        } else {
            int left = p - 1;
            int right = p + 1;
            while (left >= 0 && right < n && sw[left] == sw[right]) {
                left--;
                right++;
            }
            int start = p - 1;
            while (start > left) {
                sw[start] = processing(start);
                start--;
            }
            start = p + 1;
            while (start < right) {
                sw[start] = processing(start);
                start++;
            }
        }
    }

    private static int processing(int idx) {
        return (sw[idx] + 1) % 2;
    }

    private static void print() {
        int start = 0;
        while (true) {
            int end = start + 20;
            for (int i = start; i < end; i++) {
                if (i < n) {
                    sb.append(sw[i]).append(" ");
                } else {
                    return;
                }
            }
            start += 20;
            sb.append("\n");
        }
    }
}
