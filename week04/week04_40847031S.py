targets = ["婦人", "土狗", "男"]


def word_counter(str):
    list = []
    for target in targets:
        count = str.count(target)
        list.append((target, count))
    return list


with open('example/dbp.txt', 'r', encoding='utf-8') as f:
    print(('dbp:{}'.format(word_counter(f.read())).replace("\'", '\"').replace(' ', '')), end=',')
with open('example/pbd.txt', 'r', encoding='utf-8') as f:
    print(('pbd:{}'.format(word_counter(f.read()))).replace("\'", '\"').replace(' ', ''))
