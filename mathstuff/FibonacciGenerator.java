package mathstuff;

import java.util.*;
public class FibonacciGenerator {
	static int numFibCalls = 0;
	static HashMap<Integer, Long> d = new HashMap<Integer, Long>();
	static Scanner fibNumber = new Scanner(System.in);
	public static void main(String[] args) 
	{
		System.out.println("Enter the term for Fibonnaci sequence:\t");
		int n = fibNumber.nextInt();
		d.put(0 , (long) 0); 
		d.put(1 , (long) 1);
		for (int  i = 0; i <= n; i++) {
			System.out.println(i + " :\t" + fib_efficient(i, d));
			//System.out.println(d.toString());
		}
		fibNumber.close();
	}
	public static long fib_efficient(int n, HashMap<Integer, Long> d) {
	    numFibCalls += 1;
	    if (d.containsKey(n)) {
	        return d.get(n);
	    } else {
	        long ans = fib_efficient(n-1, d) + fib_efficient(n-2, d);
	        d.put(n, ans);
	        return ans;
	    }
	}
}
