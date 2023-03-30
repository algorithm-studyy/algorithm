// 빈 문자열 배열 초기화
// X split("") -> arrX에 하나씩 add.
// Y split("") -> arrY에 하나씩 add.
// for문으로 arrX.size * arrY.size 만큼 반복 
// (arrX의 인덱스값) contains로 arrY배열 안에 있는지 비교
// 일치하는 값 빈 배열에 추가
class Solution {
    fun solution(X: String, Y: String): String {
        var answer: String = ""
        var arrX: arrayString = X.split("")
        var arrY: arrayString = Y.split("")
        var resarr = ""
        for(i in 0..arrX.size * arrY.size - 1) {
            if(arrX[i] == arrY[i])
        }
        return answer
    }
}