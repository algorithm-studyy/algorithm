import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val stack = Stack<Char>()
    val line = readln()
    var answer = 0
    for ((i, stick) in line.withIndex()) {
        if (stick == '(') {
            stack.push(stick)
            continue
        }
        answer += if (line[i - 1]  == ')') 1 else stack.size - 1
        stack.pop()
    }
    writer.write(answer.toString())
    writer.flush()
    writer.close()
}