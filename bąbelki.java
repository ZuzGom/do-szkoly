import java.util.Arrays;

public class Main
{
	public static void main(String[] args) {
		int[] tab = {1, 2, 3, 4, 5, 7, 8};
		int n = 7, p;
		System.out.println(Arrays.toString(tab));
		
		for (int j = 0; j<n; j++){
        for (int i = 1; i<n; i++){
            if (tab[i-1]<tab[i]){
                p = tab[i-1];
                tab[i-1] = tab[i];
                tab[i] = p;
            }
        }
		}
        System.out.println(Arrays.toString(tab));
	}
}
