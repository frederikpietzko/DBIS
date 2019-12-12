from collections import defaultdict
from queue import PriorityQueue
from itertools import cycle

class Node(object):
    def __init__(self, value, parent = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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
        i += 1
    _,_,root = q.get()
    return root


def compute_depth(root, chars, depth):
    if root.is_leaf():
        return chars[root.value] = (depth, root)
    else if root.left is not None and root.right is not None:
        chars.update(compute_depth(root.left, chars, depth +1))
        chars.update(compute_depth(root.right, chars, depth +1))
        return chars
    else if root.left is not None:
        return chars.update(compute_depth(root.left, chars, depth +1))
    else:
        return chars.update(compute_depth(root.right, chars, depth +1))



def compute_tree_hu_tucker(freq_table):
    root = compute_tree(freq_table)
    alph_depth = {k: -1 for k in freq_table.keys()}
    alph_depth = compute_depth(root, alph_depth, 0)
    alph_order = list(sorted(freq_table.keys()))
    # über Matrix relaisieren
    
    
    
    return root

        

def compute_codes(node, path, code_book):
    if node.value != '':
        code_book[node.value] = path
        return code_book

    code_book.update(compute_codes(node.left, path + '0', code_book))
    code_book.update(compute_codes(node.right, path + '1', code_book))
    return code_book
    

def encode(input_str, code_book):
    return [code_book[c] for c in input_str]
        

def decode(input_str, code_book):
    # the easy way
    inv_code_book = dict([[v,k] for k,v in code_book.items()])
    return "".join([inv_code_book[c] for c in input_str])


def decode_hard(input_str, htree):
    ret = ""
    for code in input_str:
        cnode = htree
        for bit in code:
            print(bit)
            if cnode.is_leaf():
                break
            if bit is '0':
                cnode = cnode.left
            else:
                cnode = cnode.right
        ret += cnode.value
    return ret
            


if __name__ == '__main__':
    test_string = 'abracadabra'
    freq_table = compute_freq(test_string)
    htree = compute_tree(freq_table)
    code_book = compute_codes(htree, '', {})
    encoded = encode(test_string, code_book)
    decoded = decode(encoded, code_book)
    decoded_hard = decode_hard(encoded, htree)
    print(f'The test String is: {test_string} \n' + \
          f'and was encoded to: {encoded} \n' + \
          f'decoding resulted in: {decoded} \n' + \
          f'the hard decoding resulted in: {decoded_hard}')
    
    
