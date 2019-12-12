


def DNA2binary(input_string):
    return input_string.replace('A','00').replace('C','01').replace('G','10').replace('T','11')


def binary2DNA(bin_str):
    s = ''
    for i in range(1, len(bin_str), 2):
        a = bin_str[i-1]
        b = bin_str[i]
        c = a + b
        
        if c == '00':
            s+='A'
        elif c == '01':
            s += 'c'
        elif c == '10':
            s += 'G'
        else:
            s += 'T'
    return s


def bin2BWT(input_str):
    even, odd = zip(*[ ((input_str[i:] + input_str[:i], i), (input_str[i-1:] + input_str[:i-1], i))
                       for i in range(0,len(input_str), 2)])
    
    s_odd = list(sorted(odd, key= lambda x: x[0]))
    s_even = list(sorted(even, key= lambda x: x[0]))
    e = s_even.index((input_str, 0))
    bwt1 = list(map(lambda x: x[0], s_even))
    bwt2 = list(map(lambda x: x[0], s_odd))
    bwt1 = [bits[-1] for bits in bwt1 ]
    bwt2 = [bits[-1] for bits in bwt2]
    return bwt1, bwt2, e


def count(given_str, given_char):
    i = 0
    for c in given_str:
        if c < given_char:
            i+=1
    return i


def rank(c, p, s):
    return ''.join(s).count(c,0,p+1) -1


def retransform(e, bwt1, bwt2):
    p = e
    s = ''
    while len(s) != len(bwt1) + len(bwt2):
        c1 = bwt1[p]
        p = count(bwt1, c1) + rank(c1, p, bwt1)
        c2 = bwt2[p]
        p = count(bwt2, c2) + rank(c2, p, bwt2)
        s += c1 + c2
        if(False):
            break
    return s


if __name__ == '__main__':
    test_str = "10110011"
    bwt1, bwt2, e = bin2BWT( test_str)
    decoded = retransform(e, bwt1, bwt2)
    print(f'test: {test_str} \nencoded: {e}, {bwt1}, {bwt2} \ndecoded: {decoded}')
    
