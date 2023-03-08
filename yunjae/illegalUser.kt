class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): MutableCollection<Int> {
        // val items = HashMap<String, Int>()
        // HashMap 어케 쓰는지 몰라서 실패;
        // 유저들을 hashMap으로 초기화 items[i] = 0
        // report안의 string을 공백 기준 " "으로 replace한 값 첫번째를 가져옴
        // ....걍 먹은 애들만 따로 모아서 집계하는게 나을 수도...?
        // for문으로 items[i]가 report -> 별로인듯..
        // 아 너무 어렵다 
        // mutableMapOf<String, Int>("지원" to 29,"성연" to 27) 당신들은 대체....?
        
        
        // 기본이 immutable이니 mutableMap으로 만들기
        var illegalUser = mutableMapOf<String, Int>()
        // 중복 신고는 안되니 중복은 제끼고 forEach
        report.distinct().forEach {
            val key = it.split(' ')[1]
            // 신고 많이 먹은놈 count
            illegalUser[key] = illegalUser.getOrDefault(key, 0) + 1
        }
        
        var list = illegalUser.filterValues { it >= k }
        
        var userMap = mutableMapOf<String, Int>()
        id_list.forEach {
            val key2 = it
            userMap[key2] = userMap.getOrDefault(key2, 0)
        }
        
        // 정지된 애들 신고한 애들 찾기
        report.forEach {
            // 배열 첫번째놈을 key로 잡고 나머지를 value로 해서 위 리스트에 걸리는 애들 솎아내기
            val key = it.split(' ')[0]
            if(id_list.contains(it.split(' ')[1])) {
                userMap.values += 1
            }
        }

        return userMap.values
        
    }
}