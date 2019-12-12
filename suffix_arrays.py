

def make_SA(input_str):
    suffix_array = [(input_str[i:] + input_str[:i], i+1) for i in range(len(input_str))]
    _, SA = list(zip(*sorted(suffix_array, key=lambda x: x[0])))
    return SA


def lcp(a,b):
    erg = ''
    #asi = a.find('$')
    #abi = b.find('$')
    #l = min(asi,abi)
    l = min(len(a),b.find('$'))
    for i in range(l):
        if a[i] == b[i]:
            erg += a[i]
        else:
            break
    return erg





def find(SA, sub, inp, L, R):
    M = int((L+R)/2)
    s = SA[M]
    suffix = inp[s:] + inp[:s]
    #suffix = suffix[:suffix.find('$')]
    lcpref = lcp(sub,suffix)
    l = SA[L]
    r = SA[R]
    suffixL = inp[l:] + inp[:l]
    #suffixL = suffixL[:suffixL.find('$')]
    suffixR = inp[r:] + inp[:r]
    #suffixR = suffixR[:suffixR.find('$')]
    lcprefL = lcp(sub, suffixL)
    lcprefR = lcp(sub, suffixR)
    print([suffix, lcpref, suffixL, lcprefL, suffixR, lcprefR])
    if lcprefL == sub and lcprefR == sub:
        return [L,R] if L!=R else [L]
    elif lcpref < sub:
        return find(SA,sub, inp, L, M)
    elif lcpref > sub:
        return find(SA, sub, inp, M, R)
    else:
        return find(SA,sub, inp, L, M) + find(SA, sub, inp, M, R)
        
            
            
    

if __name__ == '__main__':
    test = 'abracadabra$'
    print(make_SA(test))
    print(find(make_SA(test), 'abr', test, 0, len(test)-1))
    
    
