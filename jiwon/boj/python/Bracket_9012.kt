import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    repeat(readln().toInt()) {
        val stack = Stack<Char>()
        (readln()).forEach {
            if (it == '(') stack.push(it)
            else if (stack.size != 0 && stack.peek() == '(') stack.pop()
            else {
                stack.push(it)
                return@forEach
            }
        }
        if (stack.size != 0 ) writer.write("NO")
        else writer.write("YES")
        writer.newLine()
    }
    writer.flush()
    writer.close()
}