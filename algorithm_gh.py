

def calc_fn(x, y) -> tuple[int, int]:
    return (x - 1) * (y - 1), x * y


def calc_d(e, fn) -> int:
    for i in range(1000):
        if e * i % fn == 1:
            return i

    # PK = (e, func_fi), SK = (func_fi)


def main():
    maps = zip([chr(ord('a') + x) for x in range(0, 26)], range(1, 27))
    c2i = {x[0]: x[1] for x in maps}
    print(c2i)

    maps = zip(range(1, 27), [chr(ord('a') + x) for x in range(0, 26)])
    i2c = {x[0]: x[1] for x in maps}
    print(i2c)

    # s = [3, 5, 7, 11, 13, 17, 19]
    # p, q = random.choice(s), random.choice(s)
    # e = random.choice(s)
    # for i in range(1, 100):
    #     if (p * q + 1) * i % e == 0:
    #         print(f'times: {i}')
    #         break
    p, q, e = 13, 11, 11
    print(f'p: {p}, q: {q}, e: {e}')

    # 1 确认公钥和私钥
    # p和q都不能选1
    # e的选取和pq有关，不然计算不出来d，必须要p*q + 1是e的倍数
    pk = calc_fn(p, q)
    fn, n = pk
    print(f'n = {pk[1]}, fn = {pk[0]}')

    d = calc_d(e, fn)
    print(f'pk = ({e}, {n}); sk = ({d}, {n})')

    # 2 计算密文
    bs = 'iaminalgorithmclass'
    print(f'明文: {bs}')

    encrypts = [c2i[x] ** e % n for x in bs]
    print(f'密文: {[x for x in encrypts]}')

    # 3 计算明文
    bs = [x ** d % n for x in encrypts]
    print(f'明文: {[x for x in bs]}')
    print(f'明文: {[i2c[x] for x in bs]}')

    '''
    4 如果这真的是一个加密算法，
        质数选择太小，可以暴力迭代质数
        质数选择太大，计算Θn可能溢出
        
    5 暂时不能处理汉字
    
    6 如果怕p和q非常大的情况下，解密过程中的次方运算会很大，可能会导致溢出。容忍的极限只有整数的上限
    
    7 
    '''


if __name__ == '__main__':
    main()
