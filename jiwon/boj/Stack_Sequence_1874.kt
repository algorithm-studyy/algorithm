import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*
import kotlin.collections.ArrayList

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val printString = ArrayList<String>()
    var i = 1
    val stack = Stack<Int>()

    (1..(readln().toInt())).forEach {
        val n = readln().toInt()

        (i..n).map {
            printString.add("+\n")
            stack.push(it)
            i++
        }
        val value = stack.pop()
        if (value == n) {
            printString.add("-\n")
        } else {
            println("NO")
            return@main
        }
    }

    printString.map { writer.write(it)}
    writer.flush()
    writer.close()
}