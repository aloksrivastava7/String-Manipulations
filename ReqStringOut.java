import java.util.Scanner;
class ReqStringOut {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1,s2;
        System.out.println("***** Enter First String *****");
        s1 = sc.next();
        System.out.println("***** Enter Second String *****");
        s2 = sc.next();
        //EXAMPLE - 1
        //Example - 2 - Replace University with Technologies

        System.out.println(s1 + " University " + s2); //Method 1 - Printing Directly

        String s3 = s1 + " University " + s2; //Method 2 - Concatenating into new String

        System.out.println(s3);
        s1 = s1.concat(" University "); //Method 3 - Using String Methods
        s1 = s1.concat(s2);
        System.out.println(s1);

    }
}
