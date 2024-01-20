package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Boj11559 {

    private static char[][] board = new char[12][6];
    private static boolean[][] visit = initVisit();
    private static Queue<Point> points = new LinkedList<>();
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;

        for (int i = 0; i < 12; i++) {
            board[i] = br.readLine().toCharArray();
        }
        while (true) {
            visit = initVisit();
            puyo();
            if (points.isEmpty()) {
                break;
            }
            while (!points.isEmpty()) {
                Point point = points.poll();
                board[point.x][point.y] = '.';
            }
            down();
            result++;
        }
        System.out.println(result);
    }

    private static void puyo() {
        for (int i = 0; i < board.length; i++) {
            char[] chars = board[i];
            for (int j = 0; j < chars.length; j++) {
                if (!visit[i][j] && board[i][j] != '.') {
                    bfs(i, j);
                }
            }
        }
    }

    private static void bfs(int h, int w) {
        Queue<Point> queue = new LinkedList<>();
        Queue<Point> marking = new LinkedList<>();
        visit[h][w] = true;
        queue.add(new Point(h, w));
        int count = 0;
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            int x = point.x;
            int y = point.y;
            marking.add(point);
            count++;

            for (int i = 0; i < dx.length; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= 12 || ny < 0 || ny >= 6 || visit[nx][ny]
                    || board[nx][ny] == '.') {
                    continue;
                }
                if (board[h][w] != board[nx][ny]) {
                    continue;
                }
                visit[nx][ny] = true;
                queue.add(new Point(nx, ny));
            }
        }
        if (count >= 4) {
            points.addAll(marking);
        }
    }

    private static void down() {
        for (int i = 0; i < 6; i++) {
            for (int j = 11; j > 0; j--) {
                if (board[j][i] == '.') {
                    for (int k = j - 1; k >= 0; k--) {
                        if (board[k][i] != '.') {
                            board[j][i] = board[k][i];
                            board[k][i] = '.';
                            break;
                        }
                    }
                }
            }
        }
    }


    private static boolean[][] initVisit() {
        return new boolean[12][6];
    }

    static class Point {

        private final int x;
        private final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
