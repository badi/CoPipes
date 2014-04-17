from copipes import coroutine, pipeline, null
from copipes.macros.pipe import pipe
from functools import wraps
import inspect
import ast
from macropy.core import real_repr


def make_pipe(fn):
    new_fn = pipe(fn, remove=['make_pipe'])

    @wraps(new_fn)
    @coroutine
    def wrapper(*args, **kws):
        return new_fn(*args, **kws)

    return wrapper

@make_pipe
def putStrLn():
    [x]
    print x
    send(x)

@make_pipe
def replicate(n):
    [x]
    for i in xrange(n):
        send(x)

if __name__ == '__main__':
    pipeline(
        putStrLn,
        replicate.params(3),
        putStrLn,
        ).feed(range(10))