import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*
import java.io.*
fun main() {
    val bufferReader = BufferedReader(InputStreamReader(System.`in`))
    val stringBuilder = StringBuilder()
    val n = bufferReader.readLine().toInt()
    val stack = ArrayList<Int>()
    var count = 1
    for (i in 1..n) {
        val data = bufferReader.readLine().toInt()
        while (count <= data) {
            stack.add(count)
            count += 1
            stringBuilder.appendln("+")
        }
        if (stack[stack.size - 1] == data) {
            stack.removeAt(stack.size - 1)
            stringBuilder.appendln("-")
        } 
        // 에잇 몰랑 !!
        else {
            println("NO")
            return
        }
    }
    println(stringBuilder)
}
