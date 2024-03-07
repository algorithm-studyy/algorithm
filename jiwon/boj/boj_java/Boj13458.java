package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Boj13458 {

    // 풀이
    // 각 시험장 개수 +
    // 나눠떨어지면 + 1 안해도 되는데. 이걸 판단하는 방법
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long result = 0;
        long n = Long.parseLong(br.readLine());
        List<Long> arr = Arrays.stream(br.readLine().split(" "))
            .map(Long::parseLong).collect(Collectors.toList());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());
        for (Long i : arr) {
            Long m = Math.max(i - b, 0) / c;
            Long r = (long) ((i - b) % c > 0 ? 1 : 0);
            result += m + r;
        }
        System.out.println(result + n);
    }
}

// 5 10 30 235 1 23 24 101
// 1, 1, 8, 75, 1, 6, 6, 28
// 126
// 131