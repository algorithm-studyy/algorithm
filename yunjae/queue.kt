import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.util.*
import java.io.*

val queue: Queue<Int> = LinkedList<Int>()

fun main(args: Array<String>) {

   val bufferReader = BufferedReader(InputStreamReader(System.`in`))

   val n = bufferReader.readLine().toInt()

    for (i in 0 until n) {
        val input = bufferReader.readLine().split(" ")

        when (input[0]) {
            "push" -> {
                queue.add(input[1].toInt())
            }

            "front" -> {
                if (queue.isEmpty()) {
                    println(-1)
                } else {
                    println(queue.element())
                }
            }

            "back" -> {
                   if (queue.isEmpty()) {
                        println(-1)
                    } else {
                        println(queue.last())
                    }
                }

            "empty" -> {
                   if (queue.isEmpty()){
                        println(1)
                   } else {
                        println(0)
                   }
                }

               "size" -> {
                   println(queue.size)
                }

               "pop" -> {
                   if (queue.isEmpty()){
                        println(-1)
                   } else {
                        println(queue.poll())
                   }
                }
            }
        } 
}