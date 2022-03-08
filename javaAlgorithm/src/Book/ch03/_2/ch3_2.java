package Book.ch03._2;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class ch3_2 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src/Book/ch03/_2/input.txt"));
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        System.out.println(n + m + k);
    }
}
