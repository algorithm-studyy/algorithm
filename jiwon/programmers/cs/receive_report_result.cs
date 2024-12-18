using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string[] id_list, string[] report, int k) {
        // 사용자 ID를 인덱스와 매핑
        var userIndexMap = id_list
            .Select((id, index) => new { id, index })
            .ToDictionary(item => item.id, item => item.index);

        // 각 사용자가 신고한 사용자 목록 저장
        var userReports = id_list.ToDictionary(id => id, id => new HashSet<string>());

        // 신고 처리 (중복 신고 제거)
        foreach (var r in report) {
            var parts = r.Split(' ');
            var reporter = parts[0];
            var reportedUser = parts[1];
            userReports[reporter].Add(reportedUser);
        }

        // 신고 횟수를 기록
        var reportCount = new Dictionary<string, int>();
        foreach (var reports in userReports.Values) {
            foreach (var reportedUser in reports) {
                if (!reportCount.ContainsKey(reportedUser)) {
                    reportCount[reportedUser] = 0;
                }
                reportCount[reportedUser]++;
            }
        }

        // 정지된 사용자에 대한 알림 처리
        var answer = new int[id_list.Length];
        foreach (var reporter in userReports.Keys) {
            foreach (var reportedUser in userReports[reporter]) {
                if (reportCount.TryGetValue(reportedUser, out int count) && count >= k) {
                    answer[userIndexMap[reporter]]++;
                }
            }
        }

        return answer;
    }
}
