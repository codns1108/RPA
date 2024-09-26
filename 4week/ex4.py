def sumfunc(a):
    sum = 0
    for i in range(a+1):
        sum = i + sum
    return sum

num1 = int(input("1이상의 정수를 입력하세요"))
if(num1 > 0):
    sum = sumfunc(num1)
    print(f"1~ {num1}  까지 합은  {sum}")
else:
    print("정수를 입력해주세요")
