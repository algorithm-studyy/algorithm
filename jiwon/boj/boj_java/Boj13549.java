package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 수빈 : N, 동생: K X - 1, X + 1 -> 1s 2 * x -> 0s
 * <p>
 * ===
 * <p>
 * 갔던 위치라도 위치가 작으면 갱신하고 큐에 넣기 현 위치 < 0 이면 탐색 X
 */

public class Boj13549 {

    static int n;
    static int k;
    static Map<Integer, Integer> trace = new HashMap<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        bfs();
//        for (Entry<Integer, Integer> integerIntegerEntry : trace.entrySet()) {
//            System.out.println(integerIntegerEntry);
//        }
    }

    public static void bfs() {
        Deque<Point> points = new ArrayDeque<>();
        points.add(new Point(n, 0));
        trace.put(n, 0);
        int limit = n + k;
        while (!points.isEmpty()) {
            Point point = points.pollFirst();
            int x = point.getX();
            int p = point.getP();

            if (x < -1 || x > limit) {
                continue;
            } else if (x == k) {
                System.out.println(p);
                return;
            }
            if (!trace.containsKey(2 * x) ||
                (trace.containsKey(2 * x) && trace.get(2 * x) > p)) {
                processQueue(2 * x, p, points);
            }
            if (!trace.containsKey(x - 1) ||
                (trace.containsKey(x - 1) && trace.get(x - 1) > p)) {
                processQueue(x - 1, p + 1, points);
            }
            if (!trace.containsKey(x + 1) ||
                (trace.containsKey(x + 1) && trace.get(x + 1) > p)) {
                processQueue(x + 1, p + 1, points);
            }


        }
    }

    private static void processQueue(int x, int p, Deque<Point> points) {
        trace.put(x, p);
        points.add(new Point(x, p));
    }

    static class Point {

        int x = 0;
        int p = 0;

        public Point(int x, int p) {
            this.x = x;
            this.p = p;
        }

        public int getX() {
            return x;
        }

        public void setX(int x) {
            this.x = x;
        }

        public int getP() {
            return p;
        }

        public void setP(int p) {
            this.p = p;
        }
    }
}
