str.replace(".","[.]")
str.lower()
str.split('.',0)
s[:] = s[::-1]                      #数列倒序1
a[i:i+k] = reversed(a[i:i+k])       #数列倒序2
stack.pop()
filter(str.isdigit, crazystring)
filter(str.isalpha, crazystring) 
filter(str.isalnum, crazystring) 
str.isdigit()
str.isalpha()
words = ''.join([x for x in words if x.isalpha()]) 
count = collections.Counter(s)      #统计数列
x.pop(1)                            #字典删除元素

# 13. Roman to Integer
    def romanToInt(self, s: str) -> int:
        dic={            
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000    
        }
        value = 0
        i = 0
        while(i<len(s)-1):
            if dic[s[i]] < dic[s[i+1]]: 
                value = value - dic[s[i]]
            else:
                value = value + dic[s[i]]
            i = i+1
        value = value + dic[s[len(s)-1]]
        return value
# 14. Longest Common Prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        else:
            letter=''
            for i in range (0,min(len(x) for x in strs)):
                a = strs[0][i]
                for j in range(0,len(strs)):
                    if j < len(strs)-1 and strs[j][i] != a:
                        return letter
                        break
                    if j == len(strs)-1 and strs[j][i] == a:
                        print(i,j,strs[j][i],a)
                        letter = letter + a
                        print(letter)
                    else:
                        continue
                if len(letter)!=i+1:
                    print(len(letter) ,i+1)
                    return letter
            return letter
# 20. Valid Parentheses
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        # open_par = set(["(", "[", "{"])
        open_par = ["(", "[", "{"]
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []
# 28. Implement strStr()
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:                
                return i
        return -1
# 58. Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        if s.split() == []:
            return 0
        else:
            return len(s.split()[-1])
# 67. Add Binary
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        sum = bin(sum)
        print(sum)
        sum = str(sum)[2:]
        return sum
# 125. Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        s = ''.join(char for char in s if char.isalnum()).lower()
        return s[::-1] == s
# 169. Majority Element
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for i in count:
            if count[i] > len(nums)/2:
                return int(i)
# 344 Reverse String  
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]      
    def reverseString(self, s: List[str]) -> None:
        i = 0
        while(i<len(s)/2):
            a = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = a
            i=i+1
# 383. Ransom Note
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranso = list(ransomNote)
        mag = list(magazine)
        record = []
        for i in range(0,len(ranso)):
            for j in range(0,len(mag)):
                if ranso[i] == mag[j]:
                    record.append(mag[j])
                    mag[j] = ''
                    break
                else:
                    continue
        if record == ranso: return True
        else:return False
# 387. First Unique Character in a String
        def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
# 415. Add Strings
    def addStrings(self, num1: str, num2: str) -> str:
        def tran (num):
            value = 0
            for i in range(0,len(num)):
                value = value + int(num[len(num)-i-1])*(10**i)
            return value
        return str(tran(num1)+tran(num2))
# 443. String Compression
    def compress(self, chars: List[str]) -> int:
        a = chars[0]
        x = [chars[0],0]
        for i in range(0,len(chars)):
            if a != chars[i] and i < len(chars)-1:
                j = int(x[-1])
                x[-1]=str(i-j)             
                a = chars[i]
                x.append(a)
                x.append(str(i))
            if i == len(chars)-1:
                if a != chars[i]:
                    x.append(a)
                    x.append('1')
                else:
                    j = int(x[-1])
                    x[-1]=str(i-j+1) 
            else: continue
        print(x)
        return len(x)
# 520. Detect Capital
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower()==True: return True
        elif word.isupper()==True: return True
        elif word[0].isupper()==True and word[1:].islower()==True: return True
        else: return False
# 521. Longest Uncommon Subsequence I
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a),len(b))
        if a == b:
            return -1
        else:
            return len(a)
# 541. Reverse String II
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
    def reverseStr(self, s: str, k: int) -> str:
        y = ''
        n = int(len(s)/2*k)
        for i in range(0,n):
            l = list(s[2*i*k:(i+1)*2*k])
            l1=l[0:k]
            l2=(l[k:])
            l1.reverse()
            l1 = l1+l2
            l1= ''.join(l1)
            y=y+l1
        if len(s)%(2*k) >=k:
            l = list(s[2*n*k:])
            l1=l[0:k]
            l1.reverse()
            l2=l[k:]
            l1=l1+l2
            l1= ''.join(l1)
            y=y+l1
        return y
# 551. Student Attendance Record I
    def checkRecord(self, s: str) -> bool:
        count = collections.Counter(s)
        return (s.count('A') < 2) and ('LLL' not in s)
# 557. Reverse Words in a String III
    return " ".join([word[::-1] for word in s.split(' ')])
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        s_rever = []
        for word in s_list:
            word = list(word)
            word[:] = word[::-1]            
            word = ''.join(word)
            s_rever.append(word)
        s_rever = ' '.join(s_rever)        
        return s_rever 
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        result = ""
        for word in temp:
            word = word[::-1]
            result += word + " "
        return result[:-1]
# 680. Valid Palindrome II
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        while len(s)!=0:
            if s[0] == s[-1]:
                s=s[1:-1]
            else:
                return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
        return True
# 657. Robot Return to Origin
    def judgeCircle(self, moves: str) -> bool:
        (x,y)=(0,0)
        for letter in moves:
            if letter == 'L': x = x-1
            elif letter == 'R': x = x+1
            elif letter == 'U': y = y+1
            else: y = y-1  
        if (x,y)==(0,0):
            return True
        else:
            return False
# 686. Repeated String Match
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(int(len(B)/len(A)), int(len(B)/len(A))+3):
            Ac = A*i
            if B in Ac:
                return i
        return -1
# 709. To Lower Case
    def toLowerCase(self, str: str) -> str:
        return str.lower()
# 771. Jewels and Stones
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            for j in S:
                if i == j:
                    count += 1
        return count
# 804 Unique Morse Code Words    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        tran_set = set()
        for word in words: 
            tran="".join(MORSE[ord(c) - ord('a')]for c in word)
            tran_set.add(tran)
        return len(tran_set)
# 819. Most Common Word
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph =  paragraph.replace(c, " ")
        count = collections.Counter(paragraph.lower().split())    
        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banned:
                ans, best = word, count[word]
        return ans
# 824. Goat Latin
    def toGoatLatin(self, S: str) -> str:
        S=S.split()
        for i in range(len(S)):
            apd = 'a'
            for j in range(i):
                apd = apd + 'a'
            if S[i][0] in 'aeiouAEIOU':
                S[i] = str(S[i]) + 'ma' +apd
            else:
                S[i] = S[i][1:] + S[i][0] + 'ma' + apd
        S = ' '.join(S)
        return S
# 917. Reverse Only Letters
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
    def reverseOnlyLetters(self, S: str) -> str:
        Y = ''.join([x for x in S if x.isalpha()!=True])        
        # Y = str(reversed(Y))
        ind = []
        for i in range(len(S)):
            if S[i].isalpha() == False :
                ind.append(i)       
        S = ''.join([x for x in S if x.isalpha()])         
        S = reversed(S)
        print(S)
        S = list(S)
        for i in range(len(ind)):
            S.insert(ind[i], Y[i])
        word = ''.join(x for x in S)  
        return word
# 929 Unique Email Addresses 
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            [local,domain] = email.split('@',1)
            local = local.split('+')[0]
            local = local.replace('.','')
            email_set.add(local+'@'+domain)
        return len(email_set)
# 1021 Remove Outermost Parentheses    
    def removeOuterParentheses(self, S: str) -> str:
        S=list(S)
        trigger=0
        a=[]
        i=0
        while(i<len(S)):
            if trigger == 0:
                a.append(i)
            if S[i] == "(":
                trigger += 1
            if S[i] == ")":
                trigger -= 1
            if trigger == 0:
                a.append(i)
            i=i+1       
        print(a)
        j=0
        while(j<len(a)):
            print(a[j]-j)
            del S[a[j]-j]
            j = j+1
        print(S)
        S = "".join(S)
        return S
# 1108. Defanging an IP Address
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
# 1170. Compare Strings by Frequency of the Smallest Character
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq_num(s):
            tran=[]
            for letter in s:                
                tran.append(ord(letter))
            letter_sm= min(tran)
            count = 0
            for i in tran:                
                if i == letter_sm:                    
                    count = count+1
            return count       
        tran_queries = []
        for s in queries:
            tran_queries.append(freq_num(s))           
        tran_words = []
        for s in words:
            tran_words.append(freq_num(s))       
        List = []
        for i in tran_queries:
            count = 0
            for j in tran_words:
                 if i < j:
                    count = count+1
            List.append(count)
        return List  
# 1189. Maximum Number of Balloons
    def maxNumberOfBalloons(self, text: str) -> int:    
        for a in 'balon':
            if a not in text:
                return 0
        text = collections.Counter(text)
        count = min(text['b'],text['a'],text['n'],int(text['l']/2),int(text['o']/2))
        return count