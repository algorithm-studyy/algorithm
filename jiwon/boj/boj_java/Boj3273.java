package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Boj3273 {

    public static void main(String[] args) throws Exception {
        int answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int x = Integer.parseInt(br.readLine());
        Map<Integer, Boolean> map = new HashMap<>();
        for (int i : arr) {
            if (x - i > 0 && map.containsKey(x - i)) {
                answer++;
            }
            map.put(i, true);
        }

        System.out.println(answer);
    }
}
