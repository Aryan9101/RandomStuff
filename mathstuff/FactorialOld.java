package mathstuff;
import java.util.*;
import java.math.*;
public class FactorialOld {
	static Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.print("Enter num:\t");
		int n = in.nextInt();
		BigInteger fact = new BigInteger("1");
		String factorial = "" + n + "! = ";
		for (int i = 1; i <= n-1; i++) {
			factorial += i + "*";
			fact = fact.multiply(BigInteger.valueOf(i));
			//System.out.println(fact.toString());
		}
		fact = fact.multiply(BigInteger.valueOf(n));
		factorial += n + " = ";
		System.out.print(factorial);
		System.out.println(fact);
	}

}
