import string

def lz77(input_str, d_size, p_size):
    preview = input_str[:p_size]
    input_str = input_str[p_size:]
    dictionary = ['' for i in range(d_size)]
    s = ''
    while len(preview) > 0:
        
        print(preview)
        print(input_str)
        print(dictionary)
        for i in range(len(preview),0,-1):
            k = preview[:i]
            print(k)
            if k in ''.join(dictionary) or len(k)== 1:
                
                c = preview[i] if i==0 else k
                
                pos = d_size -1 - ''.join(dictionary).find(k)
                l = len(k)
                if len(k) == 1:
                    pos = 0
                    l = 0
                s += f'({pos},{l},{c})'
                preview = preview[len(k)+l:]
                dif = p_size - len(preview)
                if dif <= len(input_str):
                    preview += input_str[:dif]
                    input_str = input_str[dif:]
                else:
                    preview += input_str
                    input_str = ''
                dictionary.append(c)
                dictionary = dictionary[1:]
                break
            
                
        
        if len(preview) == 1:
            break
    return s


def lz78(input_str):
    d = {}
    s = ''
    counter = 0
    pref = ''
    for i in range(len(input_str)):
        _id = 0
        c = input_str[i]
        if pref == '' and c not in d:
            counter += 1
            d[c] = counter
            s += f'({_id},{c})'
        elif pref + c in d:
            pref += c
            
            if i == len(input_str)-1:
                _id = d[pref]
                s += f'({_id},)'
        else:
            _id = d[pref]
            counter += 1
            d[pref+c] = counter
            
            pref = ''
            s += f'({_id},{c})'
        
    return s

                
def lz78_decode(input_str):
    s = input_str.strip('()').split(')(')
    d = {}
    erg = ''
    counter = 0
    for pair in s:
        _id, letter = pair.split(',')
        _id = int(_id)
        if _id not in d:
            counter += 1
            d[counter] = letter
            erg += letter
        else:
            counter += 1
            pref = d[_id]
            d[counter] = pref + letter
            erg += pref + letter
    return erg


def lzw(input_string):
    letters = list(string.ascii_lowercase)
    d = {letters[k]:k+1 for k in range(0,len(letters))}
    S = input_string
    pref = S[0]
    erg = ''
    j = len(letters)
    for i in range(1,len(S)):
        c = S[i]
        if pref + c not in d:
            j+= 1
            d[pref+c] = j
            erg += str(d[pref]) + ','
            pref = c
        else:
            pref += c
            if i == len(S) -1:
                erg += str(d[pref])
    return erg
        
        

if __name__ == '__main__':
    print(lz78('tobeornottobeortobeornot'))
    print(lz78_decode(lz78('tobeornottobeortobeornot')))
    print(lzw('tobeornottobeortobeornot'))
            
