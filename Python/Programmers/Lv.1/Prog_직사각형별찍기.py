a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*' * a)


### 한줄쏘쓰
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b