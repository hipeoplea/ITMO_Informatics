def num(x):
    answ = [1, 2]
    fib1 = 2
    while fib1 < x:
        fib1 = fib1 + answ[-2]
        answ.append(fib1)
    return answ if answ[-1] <= x else answ[0:-1]


a = int(input())
number = num(a)
starts = '0' * len(number)
for i in reversed(number):
    if a - i >= 0:
        starts = starts[:number.index(i)] + '1' + starts[number.index(i)+1:]
        a -= i
starts = starts[::-1]
while '11' in starts:
    if starts[:2] == '11': starts = '100' + starts[2:]
    starts = starts.replace('011', '100')
print(starts)
