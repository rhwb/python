sentence1 = "QA consultancy"
sentence2 = "Office for National Statistics"
vowels = ['a','e','i','o','u']
s1 = ""
s2 = ""

for x in sentence1:
    checkletter = x
    if checkletter.lower() in vowels:
        s1 += checkletter

for x in sentence2:
    checkletter = x
    if checkletter.lower() not in vowels:
        s2 += checkletter

print(s1)
print(s2)








