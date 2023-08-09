import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val stack:Stack<String> = Stack<String>()
    val pb = mutableListOf<String>()
    val str = readln() + " "
    var i = -1
    while (++i < str.length ) {
        if (str[i].toString() == "<") {
            while (stack.isNotEmpty()) pb.add(stack.pop())
            while (i < str.length) {
                pb.add(str[i].toString())
                if (str[i].toString() == ">") break
                i++
            }
        } else if (str[i].toString() == " ")  {
            while (stack.isNotEmpty()) pb.add(stack.pop())
            pb.add(" ")
        }
        else stack.push(str[i].toString())
    }

    writer.write(pb.joinToString("").trim())
    writer.flush()
    writer.close()
}