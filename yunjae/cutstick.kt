import java.io.*
import java.util.*
import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() {
    val bufferReader = BufferedReader(InputStreamReader(System.`in`))
    var s = bufferReader.readLine()

    var stick = 0
    var cutStick = 0
    var laser = 0
    for(i in 0 until s.length){
        when {
            s[i]=="(" && s[i+1]==")" -> laser += 1
            else -> for(j in 0 until s.length) {
                if(s[j] == )
            }
        }
        
    }
    println(cutStick)
}