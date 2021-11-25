dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2',
                [
                    'file2',
                    'file3'
                ]
            ),
            ( 'folder3',
                [
                    'file3',
                    'file4',
                    ('folder4', ['file3'])
                ]
            ),
            'file5'
        ]
    )
]


def search(dirs, file_name):

        folder = []
        if type(dirs) == tuple:
            path = dirs[0]
            subnotes = dirs[1]

            for x in subnotes:
                if type(x) == str:
                    if x==file_name:
                        folder = folder + ['/' + path +'/' + file_name]
                else:
                    folder = folder + [''.join(['/'+ path +'/']+[x]) for x in search(x, file_name)]
            return folder
        else:
            for x in dirs:
                if type(x) == str:
                    if x==file_name:
                        return folder+['/' + file_name]
                    else:
                        return folder
                else:
                    return search(x, file_name)


# Перевірка
print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')