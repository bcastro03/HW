def threeSum(nums):
    nums.sort()
    pair = []
    seen = set()
    
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = (nums[i], nums[j], nums[k])
                if triplet not in seen:
                    pair.append(list(triplet))
                    seen.add(triplet)
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

    return pair

if __name__ == "__main__":
    nums = [-12, 3, 6, 1, 6, 9]
    triplets = threeSum(nums)

    if triplets:
        print(triplets)
    else:
        print("No triplets can be formed")