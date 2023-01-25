package _1008

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Double.parseDouble
import java.util.*

fun solution() {
    val bufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val input = bufferedReader.readLine()
    val tokens = StringTokenizer(input, " ");
    val a = parseDouble(tokens.nextToken());
    val b = parseDouble(tokens.nextToken());

    print(a / b);
}