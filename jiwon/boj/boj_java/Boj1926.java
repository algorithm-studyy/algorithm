package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;
import java.util.Map.Entry;
import java.util.StringTokenizer;

public class Boj1926 {

    private static String[][] board;
    private static boolean[][] visit;
    private static int result = 0;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {1, -1, 0, 0};
    private static int n;
    private static int m;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int count = 0;
        board = new String[n][m];
        visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().split(" ");
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && board[i][j].equals("1")) {
                    count++;
                    visit[i][j] = true;
                    bfs(i, j);
                }
            }
        }
        System.out.println(count + "\n" + result);
    }

    private static void bfs(int x, int y) {
        Deque<Map.Entry<Integer, Integer>> q = new ArrayDeque<>();
        int num = 0;
        q.add(new SimpleEntry<>(x, y));
        while (!q.isEmpty()) {
            Entry<Integer, Integer> xy = q.pollFirst();
            num++;
            for (int i = 0; i < 4; i++) {
                int nx = xy.getKey() + dx[i];
                int ny = xy.getValue() + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                if (visit[nx][ny] || board[nx][ny].equals("0")) {
                    continue;
                }
                visit[nx][ny] = true;
                q.add(new SimpleEntry<>(nx, ny));
            }
        }
        result = Math.max(result, num);
    }
}
