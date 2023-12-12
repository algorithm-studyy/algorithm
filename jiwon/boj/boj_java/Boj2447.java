package boj_java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Boj2447 {

    private static char[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        drawPattern(0, 0, n);
        printBoard();
    }

    private static void drawPattern(int row, int col, int size) {
        if (size == 1) {
            board[row][col] = '*';
            return;
        }

        int newSize = size / 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 1 && j == 1) {
                    fillSpace(row + newSize, col + newSize, newSize);
                } else {
                    drawPattern(row + i * newSize, col + j * newSize, newSize);
                }
            }
        }
    }

    private static void fillSpace(int row, int col, int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                board[row + i][col + j] = ' ';
            }
        }
    }

    private static void printBoard() {
        StringBuilder stringBuilder = new StringBuilder();
        for (char[] row : board) {
            for (char c : row) {
                stringBuilder.append(c);
            }
            stringBuilder.append('\n');
        }
        System.out.print(stringBuilder);
    }
}
