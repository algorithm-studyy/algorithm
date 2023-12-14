package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Boj15663 {

    private static int n;
    private static int m;
    private static int[] arr;
    private static int[] result;
    private static Map<Integer, Integer> map = new HashMap<>();
    private static Set<String> set = new HashSet<>();
    private static StringBuilder resultString = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        result = new int[m];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }
        Arrays.sort(arr);
        recursive(0);
        System.out.print(resultString.toString());
    }

    private static void recursive(int depth) {
        if (depth == m) {
            String resultStr = makeKey();
            if (!checkDuplicate(resultStr)) {
                resultString.append(resultStr).append("\n");
                set.add(resultStr);
            }
            return;
        }
        for (int i = 0; i < n; i++) {
            if (map.get(arr[i]) > 0) {
                map.put(arr[i], map.get(arr[i]) - 1);
                result[depth] = arr[i];
                recursive(depth + 1);
                map.put(arr[i], map.get(arr[i]) + 1);
            }
        }
    }

    private static boolean checkDuplicate(String str) {
        return set.contains(str);
    }

    private static String makeKey() {
        String[] str = Arrays.stream(result).mapToObj(String::valueOf).toArray(String[]::new);
        return String.join(" ", str);
    }

}
