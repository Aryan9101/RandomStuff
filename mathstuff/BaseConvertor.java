package mathstuff;

import cryptoUtils.*;
import java.util.*;

public class BaseConvertor {
	static Scanner in = new Scanner(System.in);
	static HashMap<Integer, Character> numToChar = buildDict();
	static HashMap<Character, Integer> charToNum = buildDictReverse();
	private static final int ASCII_CAPITAL_A = 65;
	private static final int ASCII_CAPITAL_Z = 90;

	public static void main(String[] args) {
		while (true) {
			System.out.print("Enter number:\t");
			String num = in.next();
			System.out.print("Change from base ");
			int base = in.nextInt();
			System.out.print("To base ");
			int base2 = in.nextInt();
			System.out.println(baseToBaseConversion(base, base2, String.valueOf(num)).toString() + "\n");
		}
	}
	
	public static String baseToBaseConversion(int prevBase, int nextBase, String num){
		int afterNum = baseToDecimalConversion(prevBase, num);
		//System.out.println(afterNum);
		return Base.arrayToString(nextBase, decimalToBaseConversion(nextBase, afterNum));
	}
	
	private static ArrayList<String> decimalToBaseConversion(int base, int num) {
		ArrayList<String> digits = new ArrayList<>();
		for (int n = -1; Math.pow(base, n) <= num; n++) {
			if (Math.pow(base, n+1) > num) {
				int f = num / (int)Math.pow(base, n);
				if (f >= 10 && f < 36 && base <= 36) {
					digits.add(String.valueOf(numToChar.get(f)));
				} else {
					digits.add(String.valueOf((f)));
				} 
				System.out.println("*" + n + ", " + num + ", " + Math.pow(base, n) + ", " + (num / (int)Math.pow(base, n)));
				num -= (f * Math.pow(base, n));
				System.out.println(num);
				n = -1;
			} else {
				continue;
			}
		}
		return digits;
	}
	
	private static int baseToDecimalConversion(int base, String num) {
		char[] digits = num.toCharArray();
		//System.out.println(Arrays.toString(digits));
		int decimal = 0;
		//System.out.println(decimal);
		for(int i = digits.length-1; i >= 0; i--) {
			if (charToNum.containsKey(digits[digits.length-i-1])) {
				decimal += charToNum.get(digits[digits.length-i-1]) * Math.pow(base, i); 
			} else {
				System.out.println(Integer.valueOf(digits[digits.length-i-1]) - 48);
				System.out.println(Math.pow(base, i));
				decimal += ((Integer.valueOf(digits[digits.length-i-1])-48) * Math.pow(base, i));
			}
			System.out.println(decimal);
		}
		return decimal;
	}
	
	private static HashMap<Integer, Character> buildDict(){
		HashMap<Integer, Character> numToChar = new HashMap<>();
        for (int i = ASCII_CAPITAL_A; i <= ASCII_CAPITAL_Z; i++ ) {
        	numToChar.put(i - (ASCII_CAPITAL_A - 10), (char)i);
        }
        return numToChar;
	}
	
	private static HashMap<Character, Integer> buildDictReverse(){
		HashMap<Character, Integer> charToNum = new HashMap<>();
        for (int i = ASCII_CAPITAL_A; i <= ASCII_CAPITAL_Z; i++ ) {
        	charToNum.put((char) i, i - (ASCII_CAPITAL_A - 10));
        }
        return charToNum;
	}
}
