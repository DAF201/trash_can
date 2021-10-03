package Java;

public class hs {
    public static void main(String[] args) {
        int damage = 6;
        int out_of_card = 6;
        int health = 62473;
        int out_of_card_meterer = 0;
        int couter = 0;
        while (health > 0) {
            health = health - damage;
            damage++;
            out_of_card_meterer++;
            if (out_of_card_meterer % 2 == 0) {
                health = health - out_of_card;
                out_of_card++;
            }
            health++;
            couter++;
        }
        System.out.print(couter);
    }
}