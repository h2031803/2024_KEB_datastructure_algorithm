class Node:
    def __init__(self):
        self.data = None
        self.link = None


def insertNode(findData, insertData) :
    global head, current, pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node()
    node.data = insertData
    current.link = node



def print_Nodes(start):
    current = start  # current가 head를 받는다 (메모리 참조의 참조)
    if current is None: # head가 node 생성이 안되있다싶으면 노드 프린트 안할거
        return
    print(current.data, end = ' ')
    while(current.link is not None):
        current = current.link
        print(current.data, end = ' ')



head, current, pre = None, None, None
dataArray = ["다현","정현","쯔위","사나","지효"]

if __name__ == "__main__":
    node = Node() # node 생성
    node.data = dataArray[0] # 첫번째 노드의 data 기입
    head = node         # 이 링크드 리스트의 헤드 = node (참조)

    for data in dataArray[1:]:
        pre = node # 현재 노드(객체)의 메모리 주소를 pre로 참조
        node = Node() # 새로운 노드 생성 (기존의 노드 말고 새로운 메모리번지수를 할당)
        node.data = data # 새로운 노드에 데이터 넣어줌
        pre.link = node # 참조하고 있는 pre의 link를 현재 노드에 연결

    insertNode("다현","화사")
    print_Nodes(head)
    print("\n")

    insertNode("사나", "솔라")
    print_Nodes(head)
    print("\n")

    insertNode("재남", "문별")
    print_Nodes(head)
    print("\n")

