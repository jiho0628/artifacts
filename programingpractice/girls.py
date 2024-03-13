import random
from time import sleep


num = random.randint(0,5)
num2 = random.randint(0,5)
num3 = random.randint(0,5)


def rand_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns




def what_to_eat():
    girllist = []
    list = rand_nodup(1,5,num)
    for i in range(0,num):
        dinner = list[i]
        if dinner == 1:
            girllist.append('なつき')

        elif dinner == 2:
            girllist.append('めい')

        elif dinner == 3:
            girllist.append('みく')

        elif dinner == 4:
            girllist.append('ゆう')

        else:
            girllist.append('新しい子')


    return girllist

def what_to_eat2():
    girllist2 = []
    list = rand_nodup(1,5,num2)
    for i in range(0,num2):
        dinner = list[i]
        if dinner == 1:
            girllist2.append('なつき')

        elif dinner == 2:
            girllist2.append('なかむらめい')

        elif dinner == 3:
            girllist2.append('みく')

        elif dinner == 4:
            girllist2.append('ゆう')

        else:
            girllist2.append('新しい子')

    return girllist2


def what_to_eat3():
    girllist3 = []
    list = rand_nodup(1,5,num3)
    for i in range(0,num3):
        dinner = list[i]
        if dinner == 1:
            girllist3.append('なつき')

        elif dinner == 2:
            girllist3.append('めい')

        elif dinner == 3:
            girllist3.append('みく')

        elif dinner == 4:
            girllist3.append('ゆう')

        else:
            girllist3.append('新しい子')

    return girllist3





print('2023付き合える女の子は')
sleep(1)
print(str(what_to_eat()) + 'です!!')
sleep(1)

print('')

print('2023フェラしてくれる女の子は')
sleep(1)
print(str(what_to_eat2()) + 'です!!')
sleep(1)
print('')


print('2023せふれになる女の子は')
sleep(1)
print(str(what_to_eat3()) + 'です!!')
