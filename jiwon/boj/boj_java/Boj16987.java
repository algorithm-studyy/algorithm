package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj16987 {

    private static int n;
    private static Egg[] eggs;
    private static int result = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        eggs = new Egg[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int durability = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            eggs[i] = new Egg(weight, durability);
        }

        backtracking(0, 0);
        System.out.println(result);
    }

    private static void backtracking(int start, int count) {
        result = Math.max(count, result);
        if (start == n) {
            return;
        }
        Egg current = eggs[start];
        if (current.getDurability() <= 0) {
            backtracking(start + 1, count);
            return;
        }
        for (int i = 0; i < n; i++) {
            if (start == i || eggs[i].getDurability() <= 0) {
                continue;
            }
            current.setDurability(current.getDurability() - eggs[i].getWeight());
            eggs[i].setDurability(eggs[i].getDurability() - current.getWeight());
            backtracking(start + 1, count + addIfCrashed(current, eggs[i]));
            current.setDurability(current.getDurability() + eggs[i].getWeight());
            eggs[i].setDurability(eggs[i].getDurability() + current.getWeight());
        }
    }

    private static int addIfCrashed(Egg egg1, Egg egg2) {
        int adder = 0;
        if (egg1.getDurability() <= 0) {
            adder++;
        }
        if (egg2.getDurability() <= 0) {
            adder++;
        }

        return adder;
    }

    static class Egg {

        private final int weight;
        private int durability;

        public Egg(int weight, int durability) {
            this.weight = weight;
            this.durability = durability;
        }

        public void setDurability(int durability) {
            this.durability = durability;
        }

        public int getWeight() {
            return weight;
        }

        public int getDurability() {
            return durability;
        }
    }
}
