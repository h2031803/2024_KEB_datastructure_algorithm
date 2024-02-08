import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time elapsed : {end - start}")
        return result
    return wrapper
def factorial(number) -> int :
    '''
    factorial by repetition
    :param number: number (int)
    :return: factorial result (int)
    '''
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result

# def factorial(number) -> int:
#     '''
#     factorial by recursion
#     :param number: number (int)
#     :return: factorial result
#     '''
#     if number == 1:
#         return 1
#     else:
#         return number*factorial(number-1)

@timer
def nCr(n, r) -> int:  # SRP, OCP 위반 / 클로져 / 어노테이션 / 개방폐쇠 원칙
    "조합 함수"
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)