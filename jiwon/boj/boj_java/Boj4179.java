package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Boj4179 {

    private static char[][] board;
    private static int r;
    private static int c;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    static class Coordinate {

        private int x;
        private int y;
        private char type;

        public Coordinate(int x, int y, char type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public char getType() {
            return type;
        }
    }

    public static Coordinate findStart() {
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 'J') {
                    return new Coordinate(i, j, 'J');
                }
            }
        }
        return null;
    }

    public static List<Coordinate> findFires() {
        List<Coordinate> fires = new ArrayList<>();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'F') {
                    fires.add(new Coordinate(i, j, 'F'));
                }
            }
        }
        return fires;
    }

    public static void bfs(Deque<Coordinate> deque) {
        int[][] dist = new int[r][c];
        while (!deque.isEmpty()) {
            Coordinate coordinate = deque.pollFirst();
            int x = coordinate.getX();
            int y = coordinate.getY();
            char type = coordinate.getType();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= r || ny < 0 || ny >= c) {
                    if (type == 'J') {
                        System.out.println(dist[x][y] + 1);
                        return;
                    }
                    continue;
                }
                if (board[nx][ny] == 'F' || board[nx][ny] == '#' || dist[nx][ny] != 0) {
                    continue;
                }
                if (type == 'J') {
                    dist[nx][ny] = dist[x][y] + 1;
                } else {
                    board[nx][ny] = 'F';
                }
                deque.add(new Coordinate(nx, ny, type));
            }
        }
        System.out.println("IMPOSSIBLE");
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
            }
        }
        Coordinate start = findStart();
        List<Coordinate> fires = findFires();
        Deque<Coordinate> deque = new ArrayDeque<>(fires);
        deque.add(start);
        bfs(deque);
    }

}
