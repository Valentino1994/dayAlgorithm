package _2675

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n: Int = readLine().toInt()
    for (i : Int in 0 until n) {
        val questionLine = StringTokenizer(readLine())
        val cnt = questionLine.nextToken().toInt()
        val str = questionLine.nextToken().toString()

        val strArr = str.toCharArray().toTypedArray()

        var answer: String = ""
        strArr.forEach {
            answer = plusStr(answer, it.toString().repeat(cnt))
        }

        println(answer)
    }
}

fun plusStr(a: String, b: String): String {
    return a + b
}