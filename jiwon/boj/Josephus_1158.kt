import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val queue = LinkedList<String>()
    val str = mutableListOf<String>()
    val (n, k) = readln().split(" ").map { it.toInt() }
    (1..n).map { queue.offer(it.toString()) }
    var i = 1
    while (queue.isNotEmpty()) {
        if (i % k == 0) str.add(queue.poll())
        else queue.offer(queue.poll())
        i++
    }

    writer.write(str.joinToString(", ", prefix = "<", postfix = ">"))
    writer.flush()
    writer.close()
}