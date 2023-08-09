import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.LinkedList
import java.util.Stack

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val list = Stack<String>()
    val temp = Stack<String>()
    readln().toList().map{ list.add(it.toString()) }
    (1..readln().toInt()).forEach {
        when (val line = readln()) {
            "L" -> if (list.isNotEmpty()) temp.push(list.pop())
            "D" -> if (temp.isNotEmpty()) list.push(temp.pop())
            "B" -> if (list.isNotEmpty()) list.pop()
            else -> list.push(line.last().toString())
        }
    }
    while (temp.isNotEmpty()) list.push(temp.pop())
    writer.write(list.joinToString(""))
    writer.flush()
    writer.close()
}