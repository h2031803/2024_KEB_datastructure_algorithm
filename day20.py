# after 라는 새로운 변수를 생성하고 해당 값에 복제하는 선택정렬 방식

def findMinIdx(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if(ary[minIdx]>ary[i]):
            minIdx = i
    return minIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전 ->',before)
for _ in range(len(before)):
    minIdx = findMinIdx(before)     # before  = [ 한개 원소 ]
    after.append(before[minIdx])    # len(ary) = 1
    del(before[minIdx])
print('정렬 후 -->', after)

