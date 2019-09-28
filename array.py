a.remove('s') 
del a[1] 
a.pop() 
zip(*A)             #Transpose Matrix
A = [x for row in nums for x in row ]

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
# 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i< len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)   
# 35. Search Insert Position
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            else:
                if i == len(nums)-1 and  nums[i]< target:
                    return i+1
                elif i == 0 and nums[i] > target:
                    return i
                elif nums[i] < target < nums[i+1]:
                    return i+1
                else:
                    i = i+1
# 66. Plus One
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join([str(x) for x in digits]))
        n = n+1
        digits = list(str(n))
        return [int(x) for x in digits]
# 88. Merge Sorted Array
        j = 0
        for i in range(len(nums2)):
            print('j',j)
            while j < len(nums1):
                if nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    j += 1
                    print(i,j,nums1)
                    break
                if j >= m+i:
                    nums1[m+i]=nums2[i]
                    j = j+1
                    break
                j = j+1
        return nums1
# 118. Pascal's Triangle
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0: return []
        if numRows==1: return [[1]]
        if numRows==2: return [[1],[1,1]]
        if numRows==3: return [[1],[1,1],[1,2,1]]
        L=[[1],[1,1],[1,2,1]]
        for i in range(4,numRows+1):
            l = [1]
            for j in range(1,i-1):
                print(i,j)
                l.append(L[i-2][j-1]+L[i-2][j])
            l.append(1)
            L.append(l) 
# 119. Pascal's Triangle II
        def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        if rowIndex==1: return [1,1]
        if rowIndex==2: return [1,2,1]
        L = L=[[1],[1,1],[1,2,1]]
        for i in range(3,rowIndex+1):
            l = [1]
            for j in range(1,i):
                print(i,j)
                l.append(L[i-1][j-1]+L[i-1][j])
            l.append(1)
            L.append(l)                              
        return L[rowIndex]

# 121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        down = prices[0]
        best = 0
        for i in prices:
            if i < down:
                down = i
            else:
                if i-down > best:
                    best = i-down
        return best

    def maxProfit(self, prices: List[int]) -> int:
        collect = set()
        best = 0
        if len(prices)>2
        for i in prices:
            collect.add(i)
            for j in collect:
                if i-j > best:
                    best = i-j
                collect.add(i)
        return best
# 122. Best Time to Buy and Sell Stock II
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if prices == []: return 0
        line = [prices[0]]
        for i in prices:
            if len(line)%2 == 1:
                if i <= line[-1]:
                    line[-1] = i
                else:
                    line.append(i)
            if len(line)%2 == 0:
                if i >= line[-1]:
                    line[-1] = i
                else:
                    line.append(i)
        for j in range(int(len(line)/2)):
            profit += line[2*j+1]- line[2*j]
        return profit
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
# 189. Rotate Array
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        print(nums[n-k:])
        print(nums[:n-k])   
        l = nums[n-k:] + nums[:n-k]
        for i in range(len(nums)):
            nums[i] = l[i]
        return
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
# 268. Missing Number
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
    def missingNumber(self, nums: List[int]) -> int:        
        L = list(range(len(nums)+1))
        print(L)
        for i in nums:
            L.remove(i)
        return L[0]
# 283. Move Zeroes
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        for i in range(count):
            nums.append(0)
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
# 414. Third Maximum Number
    def thirdMax(self, nums: List[int]) -> int:
        S = set(nums)
        s = list(S)
        s.sort()
        if len(s) < 3:
            return s[-1]
        return(s[-3])
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
# 448. Find All Numbers Disappeared in an Array
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        X = set(range(1, len(nums)+1))
        Y = set(nums)
        return list(X-Y)
# 485. Max Consecutive Ones
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        long = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums)-1:
                    if count > long:
                        long = count                    
            if nums[i] == 0 and count > 0:
                if count > long:
                    long = count
                count = 0            
        return long
   def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = ''.join([str(x) for x in nums])
        nums = nums.split('0')
        long = 0
        for i in nums:
            if len(i) > long:
                long = len(i)
        return long
# 509. Fibonacci Number
    def fib(self, N: int) -> int:
        if N ==0: return 0
        if N ==1: return 1
        ans = [0,1]
        for i in range(2, N+1):            
            ans.append(ans[0]+ans[1])
            ans = ans[-2:]
        return ans[-1]
# 561. Array Partition I
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        A = nums[0::2]
        return sum(nums.sort()[0::2])
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
# 566. Reshape the Matrix
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        A = [x for row in nums for x in row ]
        if r * c == len(A):
            return [A[i*c : (i + 1)*c] for i in range(r) ]
        else:
            return nums
# 766. Toeplitz Matrix
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix[0])-1):
            for j in range(len(matrix)-1):
                if matrix[j][i] != matrix[j+1][i+1]:
                    return False
        return True
# 832. Flipping an Image
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def to_revesrse(l):
            for i in range(int(len(l)/2)):
                l[i], l[len(l)-1-i] = l[len(l)-1-i],l[i]
        def to_image(l):
            for i in range(len(l)):
                if l[i] == 0:
                    l[i] = 1
                else:
                    l[i] = 0
        for row in A:
            to_revesrse(row)
            print(row)
            to_image(row)
        return A
# 867. Transpose Matrix
def transpose(self, A):
        return zip(*A)
# 905. Sort Array By Parity
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
# 922. Sort Array By Parity II
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = [x for x in A if x % 2 == 0]
        C = [x for x in A if x % 2 == 1]
        D = []
        for i in range(len(C)):
            D.append(B[i])
            D.append(C[i])
        return D
# 977. Squares of a Sorted Array
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = [x**2 for x in A]
        B.sort()
        return B
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
# 999. Available Captures for Rook
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R': m, n = i, j
        count = 0
        x = n
        while x < len(board):
            if board[m][x] != '.':
                if board[m][x] == 'B':
                    break
                if board[m][x] == 'p':
                    count +=1
                    break
            x += 1
        x = n
        while x != 0 :
            if board[m][x] != '.':
                if board[m][x] == 'B':
                    break
                if board[m][x] == 'p':
                    count +=1
                    break
            x -= 1
        y = m
        while y < len(board[0]) :
            if board[y][n] != '.':
                if board[y][n] == 'B':
                    break
                if board[y][n] == 'p':
                    count +=1
                    break
            y += 1        
        y = m
        while y != 0 :
            if board[y][n] != '.':
                if board[y][n] == 'B':
                    break
                if board[y][n] == 'p':
                    count +=1
                    break
            y -= 1
        return count
# 1002. Find Common Characters
    def commonChars(self, A: List[str]) -> List[str]:
        for i in range(len(A)): A[i]=list(A[i])
        check = A[0][:]
        for j in A[0]:
            for q in range(1,len(A)):
                if j not in A[q]:
                    check.remove(j)
                    break
                else:
                    A[q].remove(j)                   
        return check    
# 1051. Height Checker
    def heightChecker(self, heights: List[int]) -> int:
        A = heights[:]
        heights.sort()
        count = 0
        for i in range(len(A)):
            if A[i] != heights[i]:
                count += 1
        return count
# 1089. Duplicate Zeros
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 2
            else:
                i += 1
# 1160. Find Words That Can Be Formed by Characters
    def countCharacters(self, words: List[str], chars: str) -> int:
        def judge(word):
            D = collections.Counter(chars)
            for i in word:
                if i in D and D[i] > 0:
                    D[i] = D[i]-1
                    continue
                return False
            return True
        ans = 0
        for word in words:
            if judge(word):
                ans += len(word)
        return ans
# 1122. Relative Sort Array
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        D = collections.Counter(arr1)
        arr = arr2[:]
        arr3 = arr1[:]
        i = 0
        P = 0
        while i < len(arr2):            
            for j in range(D[arr2[i]]-1):
                arr.insert(i+P,arr2[i])
                arr3.remove(arr2[i])
            P += D[arr[i]]
            arr3.remove(arr2[i])
            del D[arr2[i]]
            i += 1
        arr = arr + sorted(arr3)  
        return arr
# 1185. Day of the Week
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        import calendar
        my_date = datetime.datetime(year, month, day)
        print(my_date)
        return calendar.day_name[my_date.weekday()]
# 1200. Minimum Absolute Difference
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mins = arr[1] - arr[0]
        ans = [[arr[0],arr[1]]]    
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] < mins:
                mins = arr[i]-arr[i-1]
                ans = [[arr[i-1],arr[i]]]     
                continue
            if arr[i]-arr[i-1] == mins:
                ans.append([arr[i-1],arr[i]])
        return ans