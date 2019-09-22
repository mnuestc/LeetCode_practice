a.remove('s') 
del a[1] 
a.pop(1) 


# 1 two sum    
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
# 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while(i<len(nums)):
            if nums[i] ==  nums[i-1]:
                del nums[i]
            else:
                i +=1                
        return len(nums)
    def removeDuplicates(self, nums: List[int]) -> int:
        collect = set()
        i = 0
        while(i<len(nums)):
            if nums[i] in collect:
                del nums[i]
            else:
                collect.add(nums[i])
                i +=1                
        return len(nums)
# 66. Plus One
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join([str(x) for x in digits]))
        n = n+1
        digits = list(str(n))
        return [int(x) for x in digits]
# 169. Majority Element
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for i in count:
            if count[i] > len(nums)/2:
                return int(i)    
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dic = {}
        for i,num in enumerate(nums):
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                if dic[num] > len(nums)/2:
                    return num
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
# 217. Contains Duplicate
    def containsDuplicate(self, nums: List[int]) -> bool:
        tran_set=set()
        for i in nums:
            if i not in tran_set:
                tran_set.add(i)
            else:
                return True
        return False
# 219 Contains Duplicate II
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            else:
                if abs(i-dic[num]) < k+1:                    
                    return True
                else:
                    dic[num] = i                   
        return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            for j, n in enumerate(nums):
                if num == n and 0 < abs(i-j) < k+1:
                    return True
        return False