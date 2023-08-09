import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val deque:Deque<String> = LinkedList<String>()
    val printBuffer = mutableListOf<String>()
    (1..readln().toInt()).forEach {
        when (val line = readln()) {
            "front" -> if (deque.isNotEmpty()) printBuffer.add(deque.first) else printBuffer.add("-1")
            "back" -> if (deque.isNotEmpty()) printBuffer.add(deque.last) else printBuffer.add("-1")
            "empty" -> if (deque.isNotEmpty()) printBuffer.add("0") else printBuffer.add("1")
            "size" -> printBuffer.add(deque.size.toString())
            "pop_front" -> if (deque.isNotEmpty()) printBuffer.add(deque.poll()) else printBuffer.add("-1")
            "pop_back" -> if (deque.isNotEmpty()) printBuffer.add(deque.pollLast()) else printBuffer.add("-1")
            else -> {
                if (line.contains("push_front"))
                    deque.offerFirst(line.split(" ").last())
                if (line.contains("push_back"))
                    deque.offerLast(line.split(" ").last())
            }
        }
    }
    writer.write(printBuffer.joinToString("\n"))
    writer.flush()
    writer.close()
}