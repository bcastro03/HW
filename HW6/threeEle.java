	import java.util.*;

	public class threeEle {

		public static List<List<Integer>> threeSum(int[] nums) {

		
			Arrays.sort(nums);

			List<List<Integer>> pair = new ArrayList<>();
			TreeSet<String> set = new TreeSet<String>();
			List<Integer> triplets = new ArrayList<>();

						 
			for (int i = 0; i < nums.length - 2; i++) {

				
				int j = i + 1;

				
				int k = nums.length - 1;

				while (j < k) {

					if (nums[i] + nums[j] + nums[k] == 0) {

						String str = nums[i] + ":" + nums[j] + ":" + nums[k];

						if (!set.contains(str)) {

						
							triplets.add(nums[i]);
							triplets.add(nums[j]);
							triplets.add(nums[k]);
							pair.add(triplets);
							triplets = new ArrayList<>();
							set.add(str);
						}

						// increment the second value index
						j++;

						// decrement the third value indexz
						k--;
					} else if (nums[i] + nums[j] + nums[k] < 0)
						j++;

					else
						k--;
				}
			}
			return pair;
		}

		public static void main(String[] args) {
			int[] nums = { -12, 3, 6, 1, 6, 9 };

			List<List<Integer>> three = threeSum(nums);

			if (!three.isEmpty()) {
				System.out.println(three);
			} else {
				System.out.println("No triplets can be formed");
			}
		}
	}



