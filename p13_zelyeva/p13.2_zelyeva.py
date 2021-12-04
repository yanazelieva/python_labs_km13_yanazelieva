x = []

for i in range(1880, 2020):
    with open(f'archive\yob{i}.txt', 'r') as file:
        data = file.readlines()

        for el in data:
            el = el.split(',')
            if el[1] == 'M':
                x.append(data[0].split(','))
                x.append(el)
                break
Female = []
Male = []
[Female.append(el[0]) if el[1] == 'F' else Male.append(el[0]) for el in x]


print('\nFemale:')
list_d = list({i: Female.count(i) for i in Female}.items())
list_d.sort(key=lambda i: i[1], reverse=True)
for i in list_d:
    print(i[0], i[1])
print('Male:')
list_d = list({i: Male.count(i) for i in Male}.items())
list_d.sort(key=lambda i: i[1], reverse=True)
for i in list_d:
    print(i[0], i[1])


