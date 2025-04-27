num1 = [1,2,3,4]
num2 = [3,4,5,6]
for i in num1:
    for j in range(i+1):
        if num1[i]==num2[j]:
            print(num1[i])
