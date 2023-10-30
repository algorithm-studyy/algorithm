import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        BufferReader bufferReader = new BufferReader(new InputStreamReader(System.in));
        int[] arr = new int[26];
        String s = bufferReader.readLine();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            arr[c - 97]++;
        }

    }
     for(int i = 0;i< 26;i++){
        System.out.print(arr[i] + " ");

    }
}