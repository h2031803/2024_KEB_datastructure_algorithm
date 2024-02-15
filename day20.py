# 개선된 선택 정렬
def selectionSort(ary): # 선택 정렬 시킬 ary를 받음
    n = len(ary)    # n 값 = ary 행렬 길이
    for i in range(0,n-1): # i가 0부터 ary 행렬길이-2 값을 가지면서 for문을 돈ㄷ
        minIdx = i # 초기 minIdx = 0
        for k in range(i+1,n): # k가 i+1부터 행렬길이-1(끝) 값을 가지면서 for문을 돈다
            if(ary[minIdx]>ary[k]):
                minIdx = k
        tmp = ary[i] # ary[0]값을 tmp에 임시저장
        ary[i] = ary[minIdx] # ary[0]값에 최솟값을 저장
        ary[minIdx] = tmp # 변경할 값을 ary[minIdx]에 넣는다

    return ary




dataAry = [188,162,168,120,50,150,177,105]

print('정렬 전 -->',dataAry)
# dataAry = selectionSort(dataAry)
selectionSort(dataAry) #이렇게만 해줘도 메모리에 접근하여 리스트 원소를 변경하기 때문에 문제가 없다
print('정렬 후 -->', dataAry)
