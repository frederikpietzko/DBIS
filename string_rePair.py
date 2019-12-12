from collections import defaultdict
from string import ascii_uppercase


blub = iter(ascii_uppercase)


def findMFD(input_str):
    
    digrams = defaultdict(int)
    for i in range(1,len(input_str)):
        last_char = input_str[i-1]
        c_char = input_str[i]
        digrams[last_char + c_char] += 1
    return sorted(digrams.items(),key=lambda x: x[1], reverse=True)[0]


def replaceMFD(digram, input_str, non_terminal):
    return input_str.replace(digram, non_terminal)


def repair(input_str):
    mfd, freq = findMFD(input_str)
    rules = []
    while freq > 1:
        nt = next(blub)
        input_str = replaceMFD(mfd, input_str, nt)
        rules.append(f'{nt}-->{mfd}')
        mfd, freq = findMFD(input_str)
    nt = next(blub)
    rules.append(f'{nt}-->{input_str}')
    return ','.join(rules)


def decompress(rules):
    rules = rules.split(',')
    s = rules[-1].split('-->')[1]
    for rule in rules[::-1]:
        nt, digram = rule.split('-->')
        s = s.replace(nt, digram)
    return s


if __name__ == '__main__':
    test_str = 'abcabcbc'
    erg = repair(test_str)
    print(erg)
    decomp = decompress(erg)
    print(decomp)