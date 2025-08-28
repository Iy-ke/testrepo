# Display the ouput
print("New Python file")

lst = [2, 2, 5., 6, 9, 1, 5, 3, 2., 9]
count = {}
for i in lst:
  count[i]= count.get(i, 0) + 1

print(count)
