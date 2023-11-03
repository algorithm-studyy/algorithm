package boj_kotlin

fun main() {
    val n = readln().toInt()
    val s = readln().split(" ").map { it.toInt() }.toIntArray().sortedArray()

    var a = 1
    s.asSequence().forEach {
        if (a < it) return@forEach
        a += it
    }
    println(a)
}

