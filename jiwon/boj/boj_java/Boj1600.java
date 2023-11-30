package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Boj1600 {

    static int k;
    static int w;
    static int h;
    static int[][] board;
    static int[][] horse = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {2, 1}, {2, -1}, {1, 2}, {1, -2}};
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        board = new int[h][w];

        for (int i = 0; i < h; i++) {
            board[i] = Stream.of(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        }
        System.out.println(bfs());
    }

    public static int bfs() {
        Deque<Point> points = new ArrayDeque<>();
        points.add(new Point(0, 0, k, 0));
        int[][] dist = new int[h][w];
        while (!points.isEmpty()) {
            Point point = points.pollFirst();
            int x = point.getX();
            int y = point.getY();
            int k = point.getK();
            int cnt = point.getCnt();

            if (x == h - 1 && y == w - 1) {
                return cnt;
            }

            if (k > 0) {
                for (int i = 0; i < 8; i++) {
                    int nx = x + horse[i][0];
                    int ny = y + horse[i][1];

                    if (canNotGo(dist, nx, ny)) {
                        continue;
                    }
                    dist[nx][ny] = cnt + 1;
                    points.add(new Point(nx, ny, k - 1, cnt + 1));
                }
            } else {
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (canNotGo(dist, nx, ny)) {
                        continue;
                    }
                    dist[nx][ny] = cnt + 1;
                    points.add(new Point(nx, ny, k, cnt + 1));
                }
            }
        }
        return -1;
    }

    private static boolean canNotGo(int[][] dist, int nx, int ny) {
        if (nx >= h || nx < 0 || ny >= w || ny < 0 || board[nx][ny] == 1 || dist[nx][ny] != 0) {
            return true;
        }
        return false;
    }

    static class Point {

        int x;
        int y;
        int k;
        int cnt;

        public Point(int x, int y, int k, int cnt) {
            this.x = x;
            this.y = y;
            this.k = k;
            this.cnt = cnt;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getK() {
            return k;
        }

        public int getCnt() {
            return cnt;
        }
    }
}
