names = ["Shreya", "Josephine", "Lina", "Angela", "Lea", "Rebecca", "Maria", "Wendy", "Alice", "Melinda", "Bella", "Christine"]

for x in range(0,11):
    print("index is", x)
    print("name is",names[x])

print()
for x in names:
    print("name is",x)

answer = int(input("Pick a number"))
print(names[answer])
