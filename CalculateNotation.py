flag = True

while flag:
    # print('i진법에서 j진법으로 변환을 i j로 입력해주세요')
    x, y = map(int, input("i진법에서 j진법으로 변환을 i j로 입력해주세요: ").split())
    # print('{}진법의 수를 입력해주세요'.format(x))
    N = str(input("{}진법의 수를 입력해주세요: ".format(x)))

    N10 = 0
    # x, y = 2, 8       N = 10010 type str
    for i in range(len(N)):
        N10 += int(N[len(N)-i-1])*x**i

    print("10진법으로 바꾼 결과는: {}".format(N10))
    start = 0

    while True:
        if N10 - y**start < 0:
            break
        start += 1

    Ny =''
    transnum = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for j in range(start):
        end = start - j - 1

        numstart = 0

        while True:
            if N10 - y**end < 0:
                break
            N10 -= y**end
            numstart += 1

        Ny += transnum[numstart]

    Ny += '({})'.format(y)
    print("{}진법의 {}을 {}진법으로 바꾼 결과는: {}".format(x, N, y, Ny))
    print("-"*60 + "다음 계산 경계선")
