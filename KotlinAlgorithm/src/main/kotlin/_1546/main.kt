package _1546

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.*;

fun main() {
    var br = BufferedReader(InputStreamReader(System.`in`))

    var N = Integer.parseInt(br.readLine())
    var st = StringTokenizer(br.readLine())
    var arr = IntArray(N);
    var max = Integer.MIN_VALUE / 16

    for(i : Int in 0 until N) {
        var num = st.nextToken().toInt()
        arr[i] = num
        max = max(max, num)
    }

    var sum = 0.00;
    for(i in arr) {
        sum += (100.00 * i) / max
    }

    print(sum / N)
}