import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*
import java.io.*

fun main() {
    val bufferReader = BufferedReader(InputStreamReader(System.`in`))
    val num1 = bufferReader.readLine().toInt()
    val num2 = bufferReader.readLine().toInt()
    val gcd: Int

	// 지속적으로 계산하기 위해 쓰일 변수
	var n1 = num1
	var n2 = num2
    
	// 지속적인 나눗셈을 위한 반복문
	while (true) {
		var tmp: Int

		// 맨 처음 입력받는 두 수 중 어느 것이 큰 수인지를 알 수 없어 만든 조건문
		if (n1 > n2) {
        	// 첫번 째 이후로는 계속해서 이 조건으로 분기할 것이다.
        	// 왜냐하면 밑에서 n1을 큰 수로 설정해주기 때문
			tmp = n1 % n2
			n1 = n2
		} else {
			tmp = n2 % n1
            }
		n2 = tmp

		
		if (n2 == 0) {		// 나머지가 0이 됐을 때 최대공약수 출력하고 반복문 종료
			println(n1)		// 최대공약수 출력
			gcd = n1
			break
            }
        }
	println(gcd*(num1/gcd)*(num2/gcd))	// 최소공배수 출력
}