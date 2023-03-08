// 백트래킹 문제
// 백트래킹은 모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것입니다.
// 즉 답이 될 만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기 하는 것을 백트래킹이라고 생각하면 됩니다.
// 트리구조


fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    val n = readLine().split(" ")

    fun dfs(arr: ArrayList<Int>){
        // 매개변수로 받은 배열의 길이가 input 두 번째 숫자와 같다면
        if(arr.size == n[1].toInt()) {
            // 해당 배열을 하나씩 찍음
            arr.forEach { print("$it ") }
            println()
            return
        }
        // 매개변수로 받은 배열의 길이가 input 두 번째 숫자와 같지 않다면
        // input 첫번째 숫자만큼 for loop
        for(i in 1 .. n[0].toInt()){
            // arr의 i번째 인덱스에 아무것도 없다면
            if(!arr.contains(i)){
                // 새로운 arrayList를 만듬
                val curArr = ArrayList<Int>()
                // 매개변수로 받은 arr를 다 집어 넣음
                curArr.addAll(arr)
                // i를 하나씩 집어넣음
                curArr.add(i)
                // 완성된 List를 집어넣고 다시 호출
                dfs(curArr)
            }
        }
    }

    // 처음 0번째 input만큼 for loop
    for(i in 1 .. n[0].toInt()){
        // i크기만큼 i를 넣은 arryList를 만듬
        dfs(arrayListOf(i))
    }
}