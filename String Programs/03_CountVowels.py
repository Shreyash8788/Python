s = "shreyash"
count = 0
vowels = "aeiou"

for ch in s.lower():
    if ch in vowels:
        count+=1
        
print(count)
