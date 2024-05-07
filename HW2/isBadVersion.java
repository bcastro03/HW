
public interface isBadVersion {
	
	public static boolean isBadVersion(int n) {
		int first = 16;
		if (n >= first) {
			return true;
		}
		return false;
	}

}
