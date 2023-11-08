package boj_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Boj1012 {

    private static int m;
    private static int n;
    private static int k;
    private static int[][] board;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            solution(br);
        }
    }

    public static void solution(BufferedReader br) throws IOException {
        setBoard(br);
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 1) {
                    board[i][j] = 2;
                    count++;
                    bfs(j, i);
                }
            }
        }
        System.out.println(count);
    }

    private static void bfs(int x, int y) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] coordinate = queue.pollFirst();
            int tx = coordinate[0];
            int ty = coordinate[1];
            for (int i = 0; i < 4; i++) {
                int nx = tx + dx[i];
                int ny = ty + dy[i];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || board[ny][nx] != 1) {
                    continue;
                }
                board[ny][nx] = 2;
                queue.add(new int[]{nx, ny});
            }
        }
    }

    private static void setBoard(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        for (int i = 0; i < k; i++) {
            StringTokenizer coordinate = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(coordinate.nextToken());
            int y = Integer.parseInt(coordinate.nextToken());
            board[y][x] = 1;
        }
    }
}
