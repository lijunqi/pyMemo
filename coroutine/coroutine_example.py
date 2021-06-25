
def coroutine_example(name):
    print("start coroutine...name:", name)
    x = yield name
    print("send value:", x)


coro = coroutine_example("Zarten")
print("return value of next:", next(coro))
print("return value of send:", coro.send(6))
