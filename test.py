stack =[]

sortedList =[]

for i in sortedList:
  while stackNotEmpty and stack.top()<= i[1]:
    stack.pop()
  stack.push(i)

print(stack)  
