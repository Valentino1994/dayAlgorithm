package _2110_r2

import _2110_r.myCount
import java.util.StringTokenizer

fun main() {
    val br = System.`in`.bufferedReader()
    val st = StringTokenizer(br.readLine())
    val n = st.nextToken().toInt()
    val k = st.nextToken().toInt()

    val house = IntArray(n){ br.readLine().toInt() }.apply { sort() }

    var high = house.last() - house.first()
    var low = 1

    while (true) {
        if (high < low) break

        val mid = (high + low) / 2
        val count = myCount(house, mid)

        if (count < k) {
            high = mid + 1
        } else {
            low = mid - 1
        }
    }

    println(low - 1)
}

fun myCount(house: IntArray, dis: Int): Int {
    var count = 1
    var pre = 0
    for (i in 1 until house.size) {
        if (house[i] - house[pre] >= dis) {
            pre = i
            count ++
        }
    }
    return count
}