import java.util.Scanner;
class ChangeCase {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char ch,ch1;
        System.out.println("***** Enter a character *****");
        ch = sc.next().charAt(0);
        ch1 = ch;  //A copy of it for Use in the Second Method
        //Method - 1 : Using ASCII Values (A-Z : 65-90 , a-z : 97 - 122)

        if (ch >= 65 && ch <= 90)
            ch = (char) (ch + 32);
        else if (ch >= 97 && ch <= 122)
            ch = (char) (ch - 32);
        System.out.println("After changing case : "+ch);

        //Method - 2 : Using Wrapper Class Methods ( isLowerCase(),isUpperCase() , toLowerCase(),toUpperCase() )

        if(Character.isLowerCase(ch1))
            ch1 = Character.toUpperCase(ch1);
        else if (Character.isUpperCase(ch1))
            ch1 = Character.toLowerCase(ch1);
        System.out.println("After changing case : "+ch1);
    }
}
