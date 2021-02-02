import keyword

# 1
# Keywords in Python
for kwords in keyword.kwlist:
    print(kwords, end = ' ')

# 2
# Transpiler is used for translating code from one language to another

# 3
# ## Pattern
nspaces = 2
n = 7

for i in range(n):
    print((" " * (n - i)) + ("#" * i))

for i in range(n + 1):
    print(((" " * (n - i)) + ("#" * i)), end = ' ' * nspaces)
    print(("#" * i) + (" " * (n - i)))
    # print(((" " * (n - i)) + ("#" * i)) + nspaces + (("#" * i) + (" " * (n - i))) )

print(' ')
for i in range(n):
    print((" " * i) + (("#" * (n - i))), end = ' ' * nspaces)
    print(("#" * (n - i)))