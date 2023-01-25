package _1330

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.parseInt
import java.util.StringTokenizer

fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    var input = bufferedReader.readLine()
    val AB = StringTokenizer(input, " ")
    var a = parseInt(AB.nextToken())
    var b = parseInt(AB.nextToken())

    println(calculateBig(a, b))
}

fun calculateBig(a: Int, b: Int): String {
    var result = ""
    if (a > b) {
        result = ">"
    } else if (a < b) {
        result = "<"
    } else {
        result = "=="
    }
    return result
}