

w = 9
l = 5


def elias_fano(int_list: list):
    
    bit_list = [bin(i)[2:].rjust(w, '0') for i in int_list]
    print(bit_list)
    lower = ''.join([bit[-l:] for bit in bit_list])
    buckets = [bit[:-l] for bit in bit_list]
    buckets = {bit: buckets.count(bit) for bit in list(set(buckets))}
    max_bucket,_ = max(buckets.items(), key=lambda x: x[1])
    
    def fill_buckets():
        for i in range(int(max_bucket,2)):
            if bin(i)[2:].rjust(w-l,'0') not in buckets:
                buckets[bin(i)[2:].rjust(w-l,'0')]=0 

    fill_buckets()
    unary = lambda x: ''.join(['1']*x) + '0'
    upper = ''.join([unary(freq) for bucket, freq in sorted(buckets.items(), key=lambda x: x[1])])
    return upper, lower

if __name__ == "__main__":
    print(elias_fano([5,6,7,8]))