package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Boj16953 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Value initValue = new Value(st.nextToken(), 1);
        Deque<Value> queue = new ArrayDeque<>();
        queue.addLast(initValue);
        String target = st.nextToken();

        while (!queue.isEmpty()) {
            Value value = queue.removeFirst();

            String value1 = value.getValue();
            int count = value.getCount();
            if (value1.equals(target)) {
                System.out.println(count);
                return;
            }

            if (Long.parseLong(value1) < Long.parseLong(target)) {
                queue.addLast(new Value(String.valueOf(Long.parseLong(value1) * 2),
                    count + 1));
                queue.addLast(new Value(value1 + 1, count + 1));
            }
        }

        System.out.println("-1");
    }

    private static class Value {

        private String value;
        private int count;

        public Value(String value, int count) {
            this.value = value;
            this.count = count;
        }

        public String getValue() {
            return value;
        }

        public int getCount() {
            return count;
        }
    }
}
