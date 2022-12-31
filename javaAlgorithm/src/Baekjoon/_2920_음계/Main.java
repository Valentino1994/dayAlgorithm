package Baekjoon._2920_음계;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        String a = "1 2 3 4 5 6 7 8";
        String d = "8 7 6 5 4 3 2 1";

        if(s.equals(a))
            bw.write("ascending");
        else if(s.equals(d))
            bw.write("descending");
        else
            bw.write("mixed");

        bw.flush();
        bw.close();
    }
}
