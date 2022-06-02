//
//  main.swift
//  AlgorithmSwift
//
//  Created by Geunil Park on 2022/06/02.
//

import Foundation

let max = Int(1e3) + 1
var queue: [(cnt: Int, cb: Int)] = [(1, 0)]

var visit = [[Bool]](repeating: [Bool](repeating: false, count: max), count: max)
visit[1][0] = true
var indx = 0
var dur = 0

func solution(_ s: Int) -> Int {
    // q가 끝나면 끝 !
    while indx < queue.count {
        for i in indx..<queue.count {
            let emoji = queue[i]
            // s에 도착하면 끝 !
            if emoji.cnt == s {
                return dur
            }
            // 하나 뺐을 때의 클립보드의 수가 c면
            if 0 < emoji.cnt - 1 && !visit[emoji.cnt - 1][emoji.cb] {
                queue.append((emoji.cnt - 1, emoji.cb))
                visit[emoji.cnt - 1][emoji.cb] = true
            }
            // 클립보드에 저장할 때
            if !visit[emoji.cnt][emoji.cnt] {
                queue.append((emoji.cnt, emoji.cnt))
                visit[emoji.cnt][emoji.cnt] = true
            }
            // 붙여넣기 연산일 때
            if emoji.cnt + emoji.cb < max && !visit[emoji.cnt + emoji.cb][emoji.cb] {
                queue.append((emoji.cnt + emoji.cb, emoji.cb))
                visit[emoji.cnt + emoji.cb][emoji.cb] = true
            }
            indx += 1
        }
        dur += 1
    }
    return dur
}

let s = Int(readLine()!)!
print(solution(s))

//다익스트라로 푼 것
//#include<bits/stdc++.h>
//#define xx first
//#define yy second
//using namespace std;
//using ll = long long;
//using pii = pair<int,int>;
//using pll = pair<ll,ll>;
//using tpi = tuple<int,int,int>;
//using tpl = tuple<ll,ll,ll>;
//using dpi = pair<pii,pii>;
//using dpl = pair<pll,pll>;
//const int INF = 0x3f3f3f3f;
//
//int N;
//int dp[1005][1005]{};
//
//void bfs(){
//    memset(dp,0x3f,sizeof(dp));
//    priority_queue<tpi, vector<tpi>, greater<tpi>> pq;
//    pq.push({0,1,0});
//    dp[1][0] = 0;
//
//    while(!pq.empty()){
//        int d,n,c;
//        tie(d,n,c) = pq.top();
//        pq.pop();
//
//        if(dp[n][c] < d) continue;
//        if(dp[n][n] > d+1){
//            pq.push({d+1,n,n});
//            dp[n][n] = d+1;
//        }
//
//        if(n+c < N+2 && dp[n+c][c] > d+1){
//            pq.push({d+1,n+c,c});
//            dp[n+c][c] = d+1;
//        }
//
//        if(n-1 > 0 && dp[n-1][c] > d+1){
//            pq.push({d+1,n-1,c});
//            dp[n-1][c] = d+1;
//        }
//    }
//}
//
//int main() {
//    ios_base::sync_with_stdio(0);
//    cin.tie(0);
//    cin>>N;
//
//    bfs();
//
//    int res = INF;
//    for(int i=0; i<N+2; i++){
//        res = min(res, dp[N][i]);
//    }
//    cout<<res;
//}
