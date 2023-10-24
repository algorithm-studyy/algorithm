package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.ListIterator;

public class Boj5397 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < n; i++) {
            String[] stringArray = br.readLine().split("");
            LinkedList<String> linkedList = new LinkedList<>();
            ListIterator<String> list = linkedList.listIterator();
            for (String token : stringArray) {
                if (list.hasPrevious() && token.equals("-")) {
                    list.previous();
                    list.remove();
                } else if (list.hasPrevious() && token.equals("<")) {
                    list.previous();
                } else if (list.hasNext() && token.equals(">")) {
                    list.next();
                } else if (!"><-".contains(token)) {
                    list.add(token);
                }
            }
            for (String s : linkedList) {
                sb.append(s);
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}


