package _2562

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.parseInt
import java.util.StringTokenizer

fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val list = mutableListOf<Int>()
    for (i in 0..8) {
        val readLine = bufferedReader.readLine()
        val num = parseInt(StringTokenizer(readLine).nextToken())
        list.add(num)
    }

    var maxIndex = 0
    var maxVal = 0

    for (i in 0..list.size-1) {
        if (list[i] > maxVal) {
            maxVal = list[i]
            maxIndex = i
        }
    }

    println("$maxVal\n${maxIndex + 1}")
}