package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Boj15665 {

    private static int n;
    private static int m;
    private static int[] arr;
    private static int[] result;
    private static final StringBuilder sb = new StringBuilder();
    private static final Set<String> set = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        result = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        backtracking(0);
        System.out.print(sb.toString().trim());
    }

    private static void backtracking(int depth) {
        if (depth == m) {
            String key = String.join(" ", Arrays
                .stream(result)
                .mapToObj(String::valueOf)
                .toArray(String[]::new));
            if (!set.contains(key)) {
                sb.append(key).append("\n");
                set.add(key);
            }
            return;
        }
        for (int i = 0; i < n; i++) {
            result[depth] = arr[i];
            backtracking(depth + 1);
        }
    }
}
