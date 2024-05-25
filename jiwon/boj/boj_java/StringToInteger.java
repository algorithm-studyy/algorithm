package boj_java;

public class StringToInteger {

    public static void main(String[] args) throws Exception {
        System.out.println(solution("-1234"));
        System.out.println(solution("1234"));
    }

    public static int solution(String s) {
        return Integer.parseInt(s);
    }
}
