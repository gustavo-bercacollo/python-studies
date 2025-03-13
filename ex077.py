names = (
    'Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda',
    'Fernando', 'Gabriela', 'Henrique', 'Isabela', 'João',
    'Karen', 'Leonardo', 'Mariana', 'Nathan', 'Olivia'
)

for i in names:
    print(f'\nIn the name {i} we have the vowels: ', end='' )
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')

