import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    repeat(readln().toInt()) {
        readln().split(" ").map { writer.write(it.reversed() + " ") }
        writer.newLine()
    }
    writer.flush()
    writer.close()
}