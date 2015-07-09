s = 'azcbobobegghakl'
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

substring = []
i = 0
s_count = 0
final = []

while(s_count < len(s)):
    while(i < len(alp)):
        if(s[s_count] == alp[i]):
            substring.append(s[s_count])
            s_count += 1
            break
        i += 1
    if(i == 26 or s_count == len(s)):
        if(len(final) < len(substring)):
            final = substring
        i = 0
        substring = []
print("Longest substring in alphabetical order is: " + ''.join(final))