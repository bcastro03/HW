public class badVersion implements isBadVersion {
	
	public static boolean isBadVersion(int n) {
		int first = 16;
		if (n >= first) {
			return true;
		}
		return false;
	}


	public static int firstBadVersion(int first) {
		int beg, last, mid;
		beg = 1;
		last = first;
		long pos = 1;
		while (beg <= last) {

			mid = beg + (last - beg) / 2;
			boolean x = isBadVersion(mid);
			if (x == true) {
				pos = mid;
				last = mid - 1;
			} else
				beg = mid + 1;
		}

		return (int) pos;
	}

	public static void main(String[] args) {

		System.out.println(firstBadVersion(19));

	}
}
