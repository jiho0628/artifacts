
#バビロニアンメソッドで平方根を算出する。

print('数値を入力してください')

x = float(input())

rnew = x

i = 0
while i < 3:

    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(rnew)
    i+=1



