package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Boj15664 {

    private static int n;
    private static int m;
    private static int[] input;
    private static int[] result;
    private static Set<String> set = new HashSet<>();
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        input = new int[n];
        result = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(input);
        backtracking(0, 0);
        System.out.print(sb.toString().trim());
    }

    private static void backtracking(int depth, int start) {
        if (depth == m) {
            String resultString = getResultStringJoin();
            if (!set.contains(resultString)) {
                set.add(resultString);
                sb.append(resultString).append("\n");
            }
            return;
        }
        for (int i = start; i < n; i++) {
            result[depth] = input[i];
            backtracking(depth + 1, i + 1);
        }
    }

    private static String getResultStringJoin() {
        return String.join(" ", Arrays.stream(result)
            .mapToObj(String::valueOf)
            .toArray(String[]::new));
    }

}
