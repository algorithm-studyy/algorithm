package boj_java;

import java.util.Scanner;

public class Budget2 {

    public static void main(String[] args) throws Exception {
        System.out.println(solution(10000, 4, 4));
    }

    public static long solution(long wage, long hours, long days) {
        // 기본 설정
        final int HOURLY_WAGE = 9620;  // 2023년 기준 최저 시급
        final double INCOME_TAX_RATE = 0.033;  // 소득세율 (3.3%)

        Scanner scanner = new Scanner(System.in);

        // 사용자 입력
        System.out.print("한 주에 근무하는 일수를 입력하세요: ");
        int workingDays = scanner.nextInt();
        System.out.print("하루 평균 근무 시간을 입력하세요: ");
        double hoursPerDay = scanner.nextDouble();

        // 주간 총 근무 시간
        double weeklyHours = workingDays * hoursPerDay;

        // 주휴수당 시간 계산 (근무일수에 따라 다름)
        double paidLeaveHours =
            (weeklyHours >= 15 && workingDays >= 5) ? weeklyHours / workingDays : 0;

        // 월 급여 계산 (4주 기준)
        double monthlyWage = (weeklyHours + paidLeaveHours) * 4 * HOURLY_WAGE;

        // 소득세 계산
        double incomeTax = monthlyWage * INCOME_TAX_RATE;

        // 실 수령액
        double netSalary = monthlyWage - incomeTax;

        // 결과 출력
        System.out.printf("총 월급 (세전): %,.2f원\n", monthlyWage);
        System.out.printf("소득세: %,.2f원\n", incomeTax);
        System.out.printf("실 수령액 (세후): %,.2f원\n", netSalary);

        scanner.close();

        return (long) netSalary;
    }
}
