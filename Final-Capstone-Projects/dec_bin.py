def dec_to_bin(num):
    if not num/2 == 0:
        return '{1}{0}'.format(str(num%2),dec_to_bin(num/2))
    return str(num%2)

def bin_to_dec(num):
    return sum(map(lambda x: 2**x[0] * int(x[1]),enumerate(num[::-1])))


binary = dec_to_bin(156)
print binary
dec = bin_to_dec(binary)
print dec