package mathstuff;
import java.util.*;
public class Factorial {
	static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.print("Enter num:\t");
		int n = in.nextInt();
		long fact = 1;
		System.out.println(Long.MAX_VALUE);
		String factorial = "" + n + "! = ";
		for (int i = 1; i <= n-1; i++) {
			factorial += i + "*";
			fact *= i;
			System.out.println(fact);
		}
		fact *= n;
		factorial += n + " = ";
		System.out.print(factorial);
		System.out.println(fact);
	}

}
