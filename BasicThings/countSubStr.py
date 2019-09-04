st = 'MQTQTQTQM'
pt = 'QTQ'
sb = st.find(pt)
count = 0
while sb != -1:
    count += 1
    sb = st.find(pt, sb + 1)
print(count)
# for i in range(len(st)):
#     if st[i:i + len(pt)] == pt:
#         count += 1
# print(count)
