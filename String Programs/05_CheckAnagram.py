def is_anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1)!=len(s2):
        return False

    if sorted(s1)!=sorted(s2):
        return False
    return True

if is_anagram("car","arrc"):
    print("this is a Anagram")
else:
    print("this is not Anagram")
