class RandomizedSet:

    def __init__(self):
        self.nums = []
        # num : index in nums
        self.indexes = {}

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.indexes[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.indexes:
            # swap and pop
            idx = self.indexes[val]

            self.nums[idx] = self.nums[-1]
            self.indexes[self.nums[idx]] = idx
            # self.nums[-1] = val

            self.nums.pop()
            del self.indexes[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()