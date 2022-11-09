import re

text = (
    "htps://www.youtube.com/watch?v=zI48YAa-Jec&t=1 "

)

result = re.finditer(r"(\w{5}://)(\w{3}\.)?([A-z]+)(.\w{2,3}/)([\w?=_&-]*)(\s)*", text, re.MULTILINE)

count = 0
corr = 0
if (result is not None):
    for item in result:
        count += 1
        print(f'Элемент №{count}')
        print(item.group(0))
        print(item.group(1))
        print(item.group(2))
        print(item.group(3))
        print(item.group(4))
        print(item.group(5))
        print(item.group(6))
        if (
                (item.group(0) is not None) &
                (item.group(1) is not None) &
                (item.group(3) is not None) &
                (item.group(4) is not None)
        ):
            corr = 1
        else:
            corr = 0
if (corr == 1):
    print("Ссылка корректна")
else:
    print("Ссылка некорректна")
