package boj_java;

public class NumPY {

    public static void main(String[] args) throws Exception {
        System.out.println(solution("pPoooyY"));
    }

    static boolean solution(String s) {
        int pCnt = 0;
        int yCnt = 0;
        String lowerCase = s.toLowerCase();

        for (char c : lowerCase.toCharArray()) {
            if (c == 'p') {
                pCnt++;
            }
            if (c == 'y') {
                yCnt++;
            }
        }
        return pCnt == yCnt;
    }
}
