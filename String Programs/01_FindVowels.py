s = "shreyash"
vowels = "aeiou"
result = ""

for ch in s.lower():
    if ch in vowels:
        result+=ch
    
print(result)
