package _2438

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.parseInt
import java.util.StringTokenizer

fun main() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val N = parseInt(StringTokenizer(bufferedReader.readLine()).nextToken())
    for (i in 1..N) {
        println("*".repeat(i))
    }
}