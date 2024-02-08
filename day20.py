class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start  # current가 head를 받는다 (메모리 참조의 참조)
    if current == None: # head가 node 생성이 안되있다싶으면 노드 프린트 안할거
        return
    print(current.data, end = ' ')
    while(current.link != None):
        current = current.link
        print(current.data, end = ' ')



memory = []
head, current, pre = None, None, None
dataArray = ["다현","정현","쯔위","사나","지효"]

if __name__ == "__main__":
    node = Node() # node 생성
    node.data = dataArray[0] # 첫번째 노드의 data 기입
    head = node         # 이 링크드 리스트의 헤드 = node (참조)
    memory.append(node) # memory 리스트에 첫번째 노드를 넣어준다

    for data in dataArray[1:]:
        pre = node # 현재 노드의 메모리 주소를 pre로 참조
        node = Node() # 새로운 노드 생성 (기존의 노드 말고 새로운 메모리번지수를 할당)
        node.data = data # 새로운 노드에 데이터 넣어줌
        pre.link = node # 참조하고 있는 pre의 link를 현재 노드에 연결
        memory.append(node) # 현재 노드를 메모리 리스트에 넣어줌

    printNodes(head)