using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string[] friends, string[] gifts) {
        // 친구별 점수와 선물 카운트를 저장
        var giftPoints = friends.ToDictionary(friend => friend, _ => 0);
        var giftCounts = InitializeGiftCounts(friends);

        // 선물 처리
        foreach (var gift in gifts) {
            var parts = gift.Split(' ');
            var giver = parts[0];
            var receiver = parts[1];
            
            giftCounts[giver][receiver]++;
            giftPoints[giver]++;
            giftPoints[receiver]--;
        }

        // 결과 계산
        return friends.Max(friend => CalculateScore(friend, friends, giftCounts, giftPoints));
    }

    // 친구 간 선물 기록 초기화 함수
    private IDictionary<string, IDictionary<string, int>> InitializeGiftCounts(string[] friends) {
        var giftCounts = new Dictionary<string, IDictionary<string, int>>();
        foreach (var friend in friends) {
            giftCounts[friend] = friends.ToDictionary(f => f, _ => 0);
        }
        return giftCounts;
    }

    // 특정 친구의 점수를 계산하는 함수
    private int CalculateScore(string friend, string[] friends, 
                               IDictionary<string, IDictionary<string, int>> giftCounts, 
                               IDictionary<string, int> giftPoints) {
        int score = 0;

        foreach (var otherFriend in friends) {
            if (friend == otherFriend) continue;
            
            var giftsGiven = giftCounts[friend][otherFriend];
            var giftsReceived = giftCounts[otherFriend][friend];

            if (giftsGiven > giftsReceived || 
                (giftsGiven == giftsReceived && giftPoints[friend] > giftPoints[otherFriend])) {
                score++;
            }
        }

        return score;
    }
}
