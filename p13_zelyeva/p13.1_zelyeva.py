File = open("gadsby.txt")
lines = [line.upper() for line in File]
lst = []
for li in lines:
    for el in li:
        if el.isalpha():
            lst.append(el)
eng_letters = []
for i in range(ord("A"), ord("Z") + 1):
        eng_letters.append(chr(i))
diction = {}
def nb_let(lisd, letter):
    n = 0
    for el in lisd:
        if el == letter:
            n += 1
    diction ["Number of letters " + letter + " :"] = n
for element in eng_letters:
    nb_let(lst, element)
for key in diction:
    print(key, diction[key])
values = diction.values()
keys = diction.keys()
summary = sum(values)
percent = []
for element in values:
    percent.append(element)
out = []
for i in percent:
    out.append((i*100)/summary)
for i in range(len(out)):
    out[i] = str(round(out[i],2)) + "%"
print(out)