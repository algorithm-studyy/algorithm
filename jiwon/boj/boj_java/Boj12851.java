package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Boj12851 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Value start = new Value(Long.parseLong(st.nextToken()), 0);
        Deque<Value> queue = new ArrayDeque<>();
        int[] time = new int[100001];
        queue.addLast(start);
        long target = Long.parseLong(st.nextToken());

        if (start.getValue() >= target) {
            System.out.println(start.getValue() - target + "\n1");
            return;
        }

        long minValue = Long.MAX_VALUE;
        long count = 0;

        while (!queue.isEmpty()) {
            Value current = queue.removeFirst();
            long value = current.getValue();
            long valueCount = current.getCount();

            if (minValue < valueCount) {
                break;
            }
            if (target == value) {
                minValue = valueCount;
                count++;
                continue;
            }

            long[] nextValues = new long[]{value + 1, value - 1, value * 2};
            for (long next : nextValues) {
                if (next >= 0 && next <= 100_000 && (time[(int) next] == 0
                    || time[(int) next] == time[(int) value] + 1)) {
                    queue.add(new Value(next, valueCount + 1));
                    time[(int) next] = time[(int) value] + 1;
                }
            }
        }

        System.out.println(minValue);
        System.out.print(count);
    }

    private static class Value {

        private long value;
        private long count;

        public Value(long value, long count) {
            this.value = value;
            this.count = count;
        }

        public long getValue() {
            return value;
        }

        public long getCount() {
            return count;
        }

        @Override
        public String toString() {
            return "Value{" +
                "value=" + value +
                ", count=" + count +
                '}';
        }
    }
}
