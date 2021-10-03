package Java;

import java.lang.Math;

public class helloWorld {
    public static void main(String[] args) {
        boolean aSoul = true;
        while (aSoul) {
            double xiaoluo = Math.random();
            if (xiaoluo < 0.1) {
                break;
            } else {
                System.out.println("逆天");
            }
        }
        System.out.println("反转了，铸币工具人给我整出脑了");
    }
}