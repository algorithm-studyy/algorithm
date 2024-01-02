package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import org.jetbrains.annotations.NotNull;

public class Boj1941 {

    private static final char[][] board = new char[5][5];
    private static int result = 0;
    private static final Set<String> resultRoutes = new HashSet<>();
    private static final int[] dx = {0, 0, -1, 1};
    private static final int[] dy = {-1, 1, 0, 0};
    private static final boolean[][] visit = new boolean[5][5];
    private static final Route[] routes = new Route[7];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 5; i++) {
            board[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                visit[i][j] = true;
                routes[0] = new Route(i, j);
                backtracking(1, addIfEqualY(0, i, j), i, j);
                visit[i][j] = false;
            }
        }
        System.out.println(result);
    }

    private static void backtracking(int depth, int count, int x, int y) {
        if (count >= 4) {
            for (Route route : routes) {
                if (route == null) {
                    break;
                }
                System.out.println(route.x + " " + route.y + " " + board[route.x][route.y]);
            }
            System.out.println("-----------------------------------------------");
            return;
        }
        if (depth == 7) {
            String route = getRouteString();
            if (!resultRoutes.contains(route)) {
                result += 1;
                resultRoutes.add(route);
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) {
                return;
            }
            if (!visit[nx][ny]) {
                routes[depth] = new Route(nx, ny);
                visit[nx][ny] = true;
                backtracking(depth + 1, addIfEqualY(count, nx, ny), nx, ny);
                visit[nx][ny] = false;
            }
        }
    }

    @NotNull
    private static String getRouteString() {
        int[] changedRoute = new int[7];
        for (int i = 0; i < routes.length; i++) {
            changedRoute[i] = routes[i].getX() * 5 + routes[i].getY();
        }
        Arrays.sort(changedRoute);

        return String.join(" ", Arrays.stream(changedRoute)
            .mapToObj(String::valueOf)
            .toArray(String[]::new)
        );
    }

    private static int addIfEqualY(int count, int x, int y) {
        return board[x][y] == 'Y' ? count + 1 : count;
    }

    private static class Route {

        private final int x;
        private final int y;

        public Route(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }
}
