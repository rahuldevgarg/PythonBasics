d = [[1, 2, [10], 2], [2, 4], 4, [1, [1, [0]]]]
li = []


def flatten(v):
    for i in v:
        if type(i) == list:
            flatten(i)
        else:
            li.append(i)


flatten(d)
# flatten = []
# while 1:
#     for i in li:
#         if type(i) is list:
#             flatten.extend(i)
#         else:
#             flatten.append(i)
#     li = flatten[:]
#     flatten.clear()
#     bd = [type(l) is list for l in li]
#     if not any(bd):
#         break
print(li)

