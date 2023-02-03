package _2110_r

import java.util.StringTokenizer

fun main() {
    val bufferReader = System.`in`.bufferedReader()
    val stringTokenizer = StringTokenizer(bufferReader.readLine())
    val n = stringTokenizer.nextToken().toInt()
    val k = stringTokenizer.nextToken().toInt()

    val house = IntArray(n){ bufferReader.readLine().toInt() }.apply { sort() }

    var high = house.last()-house.first()
    var low = 1

    while (true) {
        if (high < low) break

        val mid = (high + low) / 2
        val count = myCount(house, mid)

        if (count < k) {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }

    println(low-1)
}

fun myCount(house: IntArray, dis: Int): Int{
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