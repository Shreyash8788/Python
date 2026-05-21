s = "absbd"
result = ""

for ch in s:
    if s.count(ch)>1:
        result+=ch
        break

print(result)