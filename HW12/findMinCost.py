class FindMinCost:
    def minCostToSupplyWater(self, n, wells, pipes):
        nums = pipes + [[0, i + 1, wells[i]] for i in range(n)]
        nums.sort(key=lambda x: x[2])
        self.p = [i for i in range(n + 1)]
        ans = 0
        for x in nums:
            a, b, c = x
            pa = self.find(a)
            pb = self.find(b)
            if pa != pb:
                self.p[pa] = pb
                ans += c
                n -= 1
                if n == 0:
                    return ans
        return ans

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


if __name__ == "__main__":
    n = 3
    wells = [1, 2, 9]
    pipes = [[1, 2, 8], [2, 3, 4], [3, 2, 5]]

    find_min_cost = FindMinCost()
    print("The minimum cost is", find_min_cost.minCostToSupplyWater(n, wells, pipes))