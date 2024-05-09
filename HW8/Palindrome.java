public class Palindrome {

	public static int longestPalindrome(String s) {
		int[] frequency = new int[128];
		int len = 0;
		for (char c : s.toCharArray()) {
			frequency[c]++;
			if (frequency[c] == 2) {
				len += 2;
				frequency[c] = 0;
			}
		}
		if (len < s.length()) {
			len++;
		}
		return len;
	}

	public static void main(String[] args) {
		String s = "aAb";

		// Function call
		System.out.print(longestPalindrome(s));
	}
}
