from collections import defaultdict
from queue import PriorityQueue

class Node(object):
    def __init__(self, value,parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.bits = []

    def rank(self, bit, pos):
        self.bits.count(bit, 0, pos)

    def select(self, bit, p):
        i = 0
        while p > 0:
            if self.bits[i] == bit:
                p -= 1
            i += 1
        return i

    def is_leaf(self):
        return self.left is None and self.right is None


def compute_freq(input_str):
    freq_table = defaultdict(int)
    for c in input_str:
        freq_table[c] += 1
    return freq_table


def compute_tree(freq_table):
    q = PriorityQueue()
    i = 0
    for key, value in freq_table.items():
        q.put((value, i, Node(key)))
        i+= 1
    
    while q.qsize() != 1:
        freq1,_, n1 = q.get()
        freq2,_, n2 = q.get()
        
        n = Node('', left = n1, right = n2)
        n1.parent = n
        n2.parent = n
        q.put((freq1+freq2,i, n))

        i += 1 # weird stuff for pq
        
    _,_,root = q.get()
    return root


def compute_codes(node, path, code_book):
    if node.value != '':
        code_book[node.value] = path
        return code_book

    code_book.update(compute_codes(node.left, path + '0', code_book))
    code_book.update(compute_codes(node.right, path + '1', code_book))
    return code_book

code_book = None # overrride in main

def insert_char(root, pos, c):
    code = code_book[c].copy()
    cnode = root
    while not cnode.is_leaf():
        bit = int(code[0])
        cnode.bits.insert(bit , pos)
        del code[0]
        pos = cnode.rank(bit, pos)
        cnode = cnode.left if bit is 0 else cnode.right


def get_char(root, pos):
    cnode = root
    while not cnode.is_leaf():
        bit = cnode.bits[pos]
        pos = cnode.rank(bit, pos)
        cnode = cnode.left if bit is 0 else cnode.right
    return cnode.value


def find_leaf(node, c):
    if not node.is_leaf():
        found1, n1 = find_leaf(node.left, c)
        found2, n2 = find_leaf(node.right, c)
        return True, n1 if found1 else True, n2
    else:
        if node.value == c:
            return True, node


def select_char(root, c, p):
    leaf = find_leaf(root, c)
    cnode = leaf
    pos = p
    while True:
        parent = cnode.parent
        bit = 0 if parent.left is cnode else 1
        pos = parent.select(bit, pos)
        cnode = parent
        if cnode is root:
            return pos


def encode(input_str, root):
    for i in range(len(input_str)):
        insert_char(root, i, input_str[i])
    return root, [code_book[c] for c in input_str]
        

def decode(input_str, root):
    s = ''
    
    for code in input_str:
        cnode = root
        for bit in code:
            cnode = cnode.left if bit == 0 else cnode.right
        s += cnode.value
    return s
            

if __name__ == '__main__':
    pass

    
