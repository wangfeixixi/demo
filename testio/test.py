def consumer():
    r = False
    while True:
        print("1.r-------%s" % r)
        a = yield r
        print("3.n-------%s" % r)
        if not a:
            print('a阿斯大法是大法师大法啊撒旦发生')
            return
        print('4.[CONSUMER] Consuming %s...' % a)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 10:
        n = n + 1
        print('2.[PRODUCER] Producing %s...' % n)
        r = c.send(0)
        print('5[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
