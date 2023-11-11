package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Boj10026 {

    private static int n;
    private static String[] board;
    private static StringBuffer answer = new StringBuffer();
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new String[n];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().strip();
        }
        String[] boardRB = setBoardRB();
        solution(board);
        solution(boardRB);

        System.out.println(answer.toString().strip());
    }

    public static void solution(String[] b) {
        int count = 0;
        boolean[][] visit = new boolean[n][n];
        for (int i = 0; i < b.length; i++) {
            for (int j = 0; j < b[i].length(); j++) {
                if (!visit[i][j]) {
                    count += 1;
                    visit[i][j] = true;
                    bfs(i, j, visit, b[i].charAt(j), b);
                }
            }
        }
        answer.append(count);
        answer.append(" ");
    }

    public static String[] setBoardRB() {
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = board[i].replaceAll("G", "R");
        }
        return result;
    }

    public static void bfs(int x, int y, boolean[][] visit, char item, String[] b) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] coordinate = queue.pollFirst();
            int ax = coordinate[0];
            int ay = coordinate[1];

            for (int i = 0; i < 4; i++) {
                int nx = ax + dx[i];
                int ny = ay + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || visit[nx][ny]
                    || b[nx].charAt(ny) != item) {
                    continue;
                }
                visit[nx][ny] = true;
                queue.add(new int[]{nx, ny});
            }
        }
    }
}
