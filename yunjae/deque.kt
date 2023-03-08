import java.io.BufferedWriter
import java.io.OutputStreamWriter
import kotlin.collections.ArrayDeque
import java.util.*
import java.io.*



fun main(args: Array<String>) {
   val arrDequeue: LinkedList<Int> = LinkedList()
   val bufferReader = BufferedReader(InputStreamReader(System.`in`))

   val n = bufferReader.readLine().toInt()

    for (i in 0 until n) {
        val input = bufferReader.readLine().split(" ")

        when (input[0]) {
            "push_front" -> {
                arrDequeue.addFirst(input[1].toInt())
            }

            "push_back" -> {
                arrDequeue.addLast(input[1].toInt())
            }

            "pop_front" -> {
                   if (arrDequeue.isEmpty()) {
                        println(-1)
                    } else {
                        println(arrDequeue.removeFirst())
                    }
                }

            "pop_back" -> {
                   if (arrDequeue.isEmpty()){
                        println(-1)
                   } else {
                        println(arrDequeue.removeLast())
                   }
                }

            "size" -> {
                   println(arrDequeue.size)
            }

            "empty" -> {
                   if (arrDequeue.isEmpty()){
                        println(1)
                   } else {
                        println(0)
                   }
            }
            "front" -> {
                   if (arrDequeue.isEmpty()){
                        println(-1)
                   } else {
                        println(arrDequeue.first)
                   }
                }

            "back" -> {
                   if (arrDequeue.isEmpty()){
                        println(-1)
                   } else {
                        println(arrDequeue.last)
                   }
                }
            }
        } 
}