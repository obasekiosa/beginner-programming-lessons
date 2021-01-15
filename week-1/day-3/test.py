



s = "RichieSemi"
print(len(s))

totalCharacters = 0
# range(len(s))
c = 9
for c in s:
    totalCharacters = totalCharacters + 1
    for c in s:
        print()
    print()

print(c)
t = 0
while(t < len(s)):
    t = t + 1

print(totalCharacters)
print(t)