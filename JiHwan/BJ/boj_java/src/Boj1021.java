import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Boj1021 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        Deque<Integer> dq = new ArrayDeque<>();
        int[] arr = new int[m];
        int answer = 0;
        int index = 0;

        for (int i = 1; i <= n; i++) {
            dq.add(i);
        }
        for (int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }

        while (index < m) {
            Iterator<Integer> iterator = dq.stream().iterator();
            int target = 0;
            while (iterator.hasNext()) {
                if (iterator.next().equals(arr[index])) {
                    break;
                }
                target++;
            }
            if (n - target > target) {
                answer += target;
                for (int i = 0; i < target; i++) {
                    dq.add(dq.pollFirst());
                }
            } else {
                answer += n - target;
                for (int i = 0; i < n - target; i++) {
                    dq.addFirst(dq.pollLast());
                }
            }
            dq.pollFirst();
            index++;
            n--;
        }
        System.out.println(answer);
    }
}
