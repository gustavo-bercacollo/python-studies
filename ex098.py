# Python Exercise #098 - Counter Function

from time import sleep

def counter(start, end, step):
    if step == 0:
        print("Step cannot be zero. Using step = 1.")
        step = 1 if start < end else -1

    if start > end and step > 0:
        step = -step
    elif start < end and step < 0:
        step = -step

    print(f'Counting from {start} to {end} by {abs(step)}')

    for i in range(start, end + (1 if step > 0 else -1), step):
        print(i, end=' ', flush=True)
        sleep(0)

    print('END!')
    print('-=-' * 20)


counter(1, 10, 1)
counter(10, 0, -2)

print("Now it's your turn to customize the count.")

start = int(input('Start: '))
end = int(input('End: '))
step = int(input('Step: '))

counter(start, end, step)
