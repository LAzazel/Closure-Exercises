def seq(func=None):

    funcs = []

    def inner(value):
        if callable(value):
            funcs.append(value)
            return inner
        else:
            for f in funcs[::-1]:
                value = f(value)
            return value

    if func is not None:
        inner(func)
    return inner

def arr():

    lst = []

    def inner(index=None):
        if index is None:
            return None
        if isinstance(index, int):
            if 0 <= index < len(lst):
                return lst[index]
            else:
                return None
        else:
            raise TypeError('Id must be an integer.')

    def push(value):
        lst.append(value)

    def pop():
        if lst:
            return lst.pop()
        return None

    inner.push = push
    inner.pop = pop

    return inner


print(seq(lambda x: x + 7)(lambda x: x * 2)(5))
print(seq(lambda x: x * 2)(lambda x: x + 7)(5))
print(seq(lambda x: x + 1)(lambda x: x * 2)(lambda x: x / 3)(lambda x: x - 4)(7))

arr = arr()
arr.push('first')
arr.push('second')
arr.push('third')

print(arr(0))
print(arr(1))
print(arr(2))

print(arr.pop())
print(arr.pop())
print(arr.pop())
print(arr.pop())