import pprint
message = "писать само сообщение"

b = 0
count = {}
for chrem in message:
    count.setdefault(chrem, 0)
    count[chrem] = count[chrem] + 1
pprint.pprint(count)  # подсчет каждого символа с в виде словаря "{}"


for v in count.values():
    b = v + b
print(b)  # сколько всего символов в "message"

