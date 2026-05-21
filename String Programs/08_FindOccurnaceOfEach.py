# for this we can get outout in dictionary
s = "shreyash"
d = {}

for ch in s:
    d[ch] = d.get(ch,0)+1

print(d)


# for this we get output in list
s1 = "hello"
count = []

for ch in s1:
    count.append((ch,s1.count(ch)))

print(count)