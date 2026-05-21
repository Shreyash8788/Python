s = "shreyash"
d = {}
duplicate = ""

for ch in s:
    d[ch] = d.get(ch,0)+1

for ch in s:
    if d[ch] > 1 and ch not in  duplicate:
        duplicate+=ch

print(duplicate)