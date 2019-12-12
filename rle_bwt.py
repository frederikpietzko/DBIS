

def rle(input_str):
    bit_array = [1]
    out_str = [input_str[0]]
    for i in range(1, len(input_str)):
        bit_array.append(1 if input_str[i] != input_str[i-1] else 0)
        out_str.append(input_str[i] if input_str[i] != input_str[i-1] else '')
    return "".join(out_str), bit_array


def transform(input_str):
    rotation_array = sorted([input_str[-i:] + input_str[:-i] for i in range(len(input_str))])
    return ''.join([rotation[-1] for rotation in rotation_array])
    
        
def count(given_str, given_char):
    i = 0
    for c in given_str:
        if c < given_char:
            i+=1
    return i


def rank(c, p, s):
    return s.count(c,0,p+1) -1


def retransform(bwt_str):
    e = bwt_str.index('$')
    p = e
    s = ''
    while True:
        c = bwt[p]
        s += c
        p = count(bwt_str, c) + rank(c, p, bwt_str)
        if (p == e):
            break
    return "".join(reversed(s))
        


if __name__ == '__main__':
    test_string = "abracadabra$"
    bwt = transform(test_string)
    t_rle = rle(bwt)
    print(count(bwt, 'b'))
    print(rank('a',6,bwt))
    retransformed_bwt = retransform(bwt)
    print(f'The bwt transformation resulted: {bwt} \n' + \
          f'The RLE on that is: {t_rle} \n' + \
          f'The retransformation resulted in: {retransformed_bwt}')
    
    
    
