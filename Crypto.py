# Topcoder Security Agency 설립 됬습니다.
# 새로운 암호화알고리즘을 구현했는데 숫자들을 주면 모든숫자를 곱한값이 암호화된 값입니다
# 암호화된값중에서 가장큰값으로 암호화를하려고하는데 숫자하나만 1을 더해가지구 암호화를 합니다
# 인풋은 int numbers[] output number 입니다

number = [3, 2, 1]

crypto = []
# 기본 구현방식
for idx, num in enumerate(number):
    myNumber = 1
    for nums in number:
        if nums == num:
            nums = nums + 1
        myNumber *= nums
    crypto.append(myNumber)
print(max(crypto))

# 곱셉에서 가장큰값이 나오려면 제일 작은값에다가 1을 더한값이다 적재율을 확인할때 (n+1)/n 인값인데 가장큰값을 구하려면 숫자가 작을수록 좋다
number = sorted(number)
number[0] += 1
maxNumber = 1

for i in number:
    maxNumber *= i

print(maxNumber)
