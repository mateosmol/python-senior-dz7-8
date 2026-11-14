def generator(i):
    yield i+1
    yield i+24
    yield i+369

iterable = [generator(1), generator(8), generator(25), generator(436), generator(2)]
iterable = iter(iterable)
while True:
    try:
        print(next(iterable))
    except StopIteration:
        print("всьо")
        break
print("впринципі воно вертає генератор алее")