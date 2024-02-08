# import mymath
# import time
#
# if __name__ == "__main__":
#     n = int(input("Input n : "))
#     r = int(input("Input r : "))
#     print(f"{n}C{r} = {mymath.nCr(n,r)}")
#     end = time.time()
#
#     # f = int(input())
#     # print(mymath.factorial(f))
#

import random
answer = random.randrange(1,101)
chance = 7

print(answer)
while(chance != 0):
    guess = int(input("Input guess number : "))
    if guess == answer:
        print(f'You win. Answer is {answer}')
        break
    elif guess > answer:
        chance = chance - 1
        print(f'{guess} is bigger. Chance left : {chance}')
    else:
        chance = chance - 1
        print(f'{guess} is lower. Chance left : {chance}')

else:
    print(f"You lost. Answer is {answer}")