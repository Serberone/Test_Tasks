global ni
ni = {}
def partition(number):
    answer = {(number,), }
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    ni[number] = answer
    return answer

n = int(input('Введите число: '))
ans = 0
for r in sorted(partition(n)):
    ans += 1
print('К-во разделов числа: ' + str(ans))