package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj13335 {

    private static int n;
    private static int w;
    private static int l;
    private static TruckOnBridge[] trucks;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        trucks = new TruckOnBridge[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trucks[i] = new TruckOnBridge(Integer.parseInt(st.nextToken()), 0);
        }
        System.out.println(solution());
    }

    private static int solution() {
        int result = 0;
        int weight = 0;
        int start = 0;
        int end = 0;
        while (end < n) {
            if (result - trucks[end].getT() == w) {
                weight -= trucks[end].getW();
                end++;
            }
            if (start < n && weight + trucks[start].getW() <= l) {
                weight += trucks[start].getW();
                trucks[start] = new TruckOnBridge(trucks[start].getW(), result);
                start++;
            }

            result++;
        }
        return result;
    }

    static class TruckOnBridge {

        private int w;
        private int t;

        public TruckOnBridge(int w, int t) {
            this.w = w;
            this.t = t;
        }

        public int getW() {
            return w;
        }

        public int getT() {
            return t;
        }
    }
}
