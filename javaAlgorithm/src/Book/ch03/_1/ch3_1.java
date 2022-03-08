package Book.ch03._1;

public class ch3_1 {
    public static void main(String[] args) {
        int n = 1260;
        int cnt = 0;
        int[] coins = {500, 100, 50, 10};

        for (int i = 0; i < 4; i++) {
            cnt += (n / coins[i]);
            n %= coins[i];
        }
        System.out.println(cnt);
    }
}
