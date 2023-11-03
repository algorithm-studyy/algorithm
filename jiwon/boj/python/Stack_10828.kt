import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main(args: Array<String>) {
    val writer = BufferedWriter(OutputStreamWriter(System.out))
    val n = readln().toInt()
    val list = mutableListOf<Int>()
    var top = -1;
    (1..n).forEach{
        var line = readln()
        when  {
            line.contains("push") -> {
                val lineList = line.split(" ")
                list.add(lineList[1].toInt())
                top++;
            }
            line.contains("top") -> if (top != -1) writer.write("${list[top]}\n") else writer.write("-1\n")
            line.contains("size") -> writer.write("${list.size}\n")
            line.contains("empty") -> {
                if (top == -1) writer.write("1\n")
                else writer.write("0\n")
            }
            else -> {
                if (top == -1) writer.write("-1\n")
                else {
                    val value = list[top]
                    list.removeAt(top--)
                    writer.write("${value}\n")
                }
            }
        }
    }
    writer.flush()
    writer.close()
}