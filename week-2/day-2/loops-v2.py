



elements = [1,3,4]
new_element = []
list_of_lists = [[222,22], [333,333], [[111,2222], 2222], "ssdffff"]

for e in elements:
    new_element.append(e * 3)


print("old elements:")
print(elements)

print("")
print("new elemets: ")
print(new_element)
print(list_of_lists)





# condition = i < 4
# condition = True
i = 1
print("before while loop")
while(i < 8):
    print("While loop entered")

    i += 1
    if i < 4:
        continue

    print("loop code")

print("after while loop")

simple_string = "dhdhd"
new_str = simple_string + " Hurrah!!!"
print(new_str)
long_string = """
sffggdjdjjdjdjdjdjfjddkdkkdkdkdkkdkdkdkdkdkdkdkdkdkdkkdkkdkddk
\tsjdjfjfjfkkdkkdkdkdkdkdk
            \rdkdfkfkfkfkfkfkfkfjgjgjjfkfkfj \n
        fjfjffjdjdjdkfdjfjfkjfkd
        \\
        \\n
        s"""


print(long_string)

print(bin(8))
print(bin(8 >> 1))

y = 'hgrdudjufv'
print("""
    #########
    #########
    #########
    #########
    #########
""")
print(y + y + y + y + y + y)
