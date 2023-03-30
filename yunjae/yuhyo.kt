class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        // terms = mutableMapof<String, Int>
        // terms key에 해당하는 privacies key를 value MM에 더하기
        // 오늘 날짜 today를 dateformat yy.MM.dd 로 포맷
        // privacies filter를 통해 it이 today 보다 크거나 같으면 인덱스값 리턴
        var answer: IntArray = intArrayOf()
        
        var termsM = mutableMapOf<String, Int>()
        
        terms.forEach {
            val key = it.split(' ')[0]
            val values = it.split(' ')[1].toInt()
            termsM[key] = values
        }
        
        var privaciesM = mutableMapOf<String, String>()
        
        privacies.forEach {
            val key = it.split(' ')[1]
            val date = it.split(' ')[0]
            privaciesM[key] = date
        }
        println(privaciesM.toList())
        println(termsM)
        return answer
    }
}