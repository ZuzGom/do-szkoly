import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        
        
        Scanner input = new Scanner(System.in);

        // nextInt() reads the next integer from the keyboard
        System.out.println("Proszę wpisać literę: ");
        String name = input.nextLine();
        char c = name.charAt(0);

        if( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
            System.out.println(c + " is an alphabet.");
        else
            System.out.println(c + " is not an alphabet.");
            
        System.out.println("Teraz pora na liczenie średniej");
        System.out.println("Podaj ilość ocen");
        int n = input.nextInt();
        float srednia = 0;
        float o;
        ArrayList<Float> myList = new ArrayList<>(n);
        
        for (int i = 0; i<n; i++){
            o = input.nextInt();
            myList.add(o);
            srednia += 1.0*o/n;
        }
        
        
        //int[] array = {1, 2, 3, 4, 5};

        //System.out.println(Arrays.toString(array));
        
        
        System.out.println(myList);
        System.out.println("Średnia to: "+srednia);
    }
}
