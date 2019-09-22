S = "j-Ih-gfE-dCba"
index = {}
for i in range(len(S)):
    if S[i].isalpha() == False :
        index[str(len(S)-i-1)] = S[i]
S = filter(str.isalpha, S) 
print(S)
S = reversed(S)
S = list(S)
for i in index:
    words.insert(i, index[i])
S = ''  
for word in words:
    S = S + word

print(S)