import csv
with open('music_by_Nautilus.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Song': 'Люди на холме',
                     'Year': '1997'})
    writer.writerow({'Song': 'Во время дождя',
                     'Year': '1997'})
    writer.writerow({'Song': 'Крылья',
                     'Year': '1996'})
    writer.writerow({'Song': 'Сёстры печали',
                     'Year': '1997'})
    writer.writerow({'Song': 'Нежный вампир',
                     'Year': '1996'})
    writer.writerow({'Song': 'Небо и трава',
                     'Year': '1995'})
    writer.writerow({'Song': 'Дыхание',
                     'Year': '1996'})
    writer.writerow({'Song': 'На берегу безымянной реки',
                     'Year': '1996'})
print('my favourite music!')
print('\n------------------------------')
with open('music_by_Nautilus.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['Song'], row['Year'])
print('\n------------------------------')
