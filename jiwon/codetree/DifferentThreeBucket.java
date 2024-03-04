import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Bucket[] buckets = new Bucket[3];
        for (int i = 0; i < 3; i++) {
            String[] inputs = br.readLine().split(" ");
            buckets[i] = new Bucket(Integer.parseInt(inputs[0]), Integer.parseInt(inputs[1]));
        }

        for (int i = 0; i < 100; i++) {
            int next = (i + 1) % 3;
            int j = i % 3;
            int pouringWater = Math.min(buckets[next].getSize(), buckets[j].getWater());
            buckets[next].pourWater(pouringWater);
            buckets[j].pouring(pouringWater);
        }

        for (Bucket bucket : buckets) {
            System.out.println(bucket.getWater());
        }
    }

    static class Bucket {

        private int size;
        private int water;

        Bucket(int size, int water) {
            this.size = size;
            this.water = water;
        }

        public void pourWater(int pouringWater) {
            this.water = (this.water + pouringWater) % (size + 1);
        }

        public void pouring(int pouringWater) {
            this.water = Math.max(this.water - pouringWater, 0);
        }

        public int getWater() {
            return this.water;
        }

        public int getSize() {
            return this.size;
        }
    }
}