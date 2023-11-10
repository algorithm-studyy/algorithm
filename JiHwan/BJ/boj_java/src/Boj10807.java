import java.util.Scanner;

public class Boj10807 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int [] arr = new int[num];
        int count = 0;

        for (int i = 0; i < num; i++) {
            arr[i] = sc.nextInt();
        }
        int b = sc.nextInt();
        for (int i = 0; i < arr.length; i++) {
            if (b == arr[i]){
                count += 1;
            }

        }
        System.out.println(count);
    }
}
