package boj_java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class ManyPresent {

    private static Map<String, Integer> map = new HashMap<>();

    public static void main(String[] args) {
//        System.out.println(solution(new String[]{"a", "b", "c"},
//            new String[]{"a b", "b a", "c a", "a c", "a c", "c a"}));
//        System.out.println("===============================");
        System.out.println(solution(new String[]{"muzi", "ryan", "frodo", "neo"},
            new String[]{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
                "frodo muzi", "frodo ryan", "neo muzi"}));
    }

    public static int solution(String[] friends, String[] gifts) {

        int[] presentArr = new int[friends.length];
        Map<String, Integer> presentMap = countPresent(friends, gifts);

        for (Entry<String, Integer> stringIntegerEntry : map.entrySet()) {
            System.out.print(stringIntegerEntry.getKey() + " ");
            System.out.println(stringIntegerEntry.getValue());
        }
        System.out.println("------------------------------");
        for (Entry<String, Integer> stringIntegerEntry : presentMap.entrySet()) {
            System.out.print(stringIntegerEntry.getKey() + " ");
            System.out.println(stringIntegerEntry.getValue());
        }
        for (int i = 0; i < friends.length; i++) {
            for (int j = i + 1; j < friends.length; j++) {
                int ab = map.getOrDefault(friends[i] + " " + friends[j], 0);
                int ba = map.getOrDefault(friends[j] + " " + friends[i], 0);
                // 주고받 선물이 같고, 선물지수가 다른 경우
                if (ab == ba) {
                    if (presentMap.get(friends[i]) > presentMap.get(friends[j])) {
                        presentArr[i] += 1;
                    } else if (presentMap.get(friends[i]) < presentMap.get(friends[j])) {
                        presentArr[j] += 1;
                    }
                    // 주고받 선물이 다른 경우
                } else if (ab > ba) {
                    presentArr[i] += 1;
                } else {
                    presentArr[j] += 1;
                }
            }
        }

        return Arrays.stream(presentArr).max().getAsInt();
    }

    private static Map<String, Integer> countPresent(String[] friends, String[] gifts) {
        Map<String, Integer> giveMap = new HashMap<>();
        Map<String, Integer> receiveMap = new HashMap<>();
        Map<String, Integer> result = new HashMap<>();

        for (String gift : gifts) {
            String[] toFrom = gift.split(" ");
            Integer count = giveMap.getOrDefault(toFrom[0], 0);
            giveMap.put(toFrom[0], count + 1);

            Integer count2 = receiveMap.getOrDefault(toFrom[1], 0);
            receiveMap.put(toFrom[1], count2 + 1);

            map.put(gift, map.getOrDefault(gift, 0) + 1);
        }

        for (String friend : friends) {
            Integer sendCount = giveMap.getOrDefault(friend, 0);
            Integer receiveCount = receiveMap.getOrDefault(friend, 0);

            result.put(friend, sendCount - receiveCount);
        }

        return result;
    }
}
