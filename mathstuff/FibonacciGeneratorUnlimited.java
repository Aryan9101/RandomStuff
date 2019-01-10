package mathstuff;

import java.util.*;
import java.math.*;

public class FibonacciGeneratorUnlimited {
	//Max is unlimited, but console can only display 153120
	//static int numFibCalls = 0;
	static HashMap<Integer, BigInteger> dict = new HashMap<Integer, BigInteger>();
	static Scanner fibTerm = new Scanner(System.in);
	static BigInteger fibNumber = new BigInteger("0");
		
	public static void main(String[] args)
	{
		dict.put(0 , new BigInteger("0")); 
		dict.put(1 , new BigInteger("1"));
		
		System.out.print("Enter the term:\t");
		int n = fibTerm.nextInt();
		
		BigInteger temp = new BigInteger("0"); //Init temporary bigint var
		
		long startTime = System.nanoTime();

		for (int i = 2; i < n; i++) {
			fibNumber = dict.get(i-1).add(dict.get(i-2));
			dict.remove(i-2);
			dict.put(i, fibNumber);
		}

		System.out.println(fibNumber);
		System.out.println("Time taken: " + ((double)(System.nanoTime() - startTime) / 1000000000));
	}

	/*
	public static BigInteger fib_efficient(int n) {
	    //numFibCalls += 1;
	    if (dict.containsKey(n)) {
	        return (dict.get(n));
	    } else {
	        fibNumber = (fib_efficient(n-1).add(fib_efficient(n-2)));
	        dict.remove(n-2);
	        dict.put(n, fibNumber);
	        return fibNumber;
	    }
	}
	*/
}
