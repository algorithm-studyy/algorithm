import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val queue = LinkedList<String>()
    (1..readln().toInt()).forEach {
        when(val line = readln()) {
            "front" -> if (queue.isNotEmpty()) writer.write(queue.first + "\n") else writer.write("-1\n")
            "back" -> if (queue.isNotEmpty()) writer.write(queue.last + "\n") else writer.write("-1\n")
            "size" -> writer.write(queue.size.toString() + "\n")
            "empty" -> if (queue.isEmpty()) writer.write("1\n") else writer.write("0\n")
            "pop" -> if (queue.isNotEmpty()) writer.write(queue.poll() + "\n") else writer.write("-1\n")
            else -> queue.addLast(line.split(" ")[1])
        }
    }
    writer.flush()
    writer.close()
}