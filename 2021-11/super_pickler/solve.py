import pickle
import marshal
import types
import io

with open("pick", "rb") as f:
    data = f.read()


def super_unpickle(pkl):
    try:
        dt = pickle.loads(pkl)
        return {
            k: super_unpickle(v) if isinstance(v, bytes) else v for k, v in dt.items()
        }
    except:
        try:
            return marshal.loads(pkl)
        except:
            return pkl


dt = super_unpickle(data)


def code2fn(co, name):
    return types.FunctionType(co, globals(), name)


class Tree:
    __init__ = code2fn(dt["__init__"], "__init__")
    __len__ = code2fn(dt["__len__"], "__len__")
    depth = code2fn(dt["depth"], "depth")


class XUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "tree":
            return Tree
        return super().find_class(module, name)


def xloads(s):
    """Helper function analogous to pickle.loads()."""
    return XUnpickler(io.BytesIO(s)).load()


tree = xloads(dt["__"])


def traverse(t):
    if t is None:
        return
    if t.data is not None:
        yield t.data
    a, b = traverse(t.left), traverse(t.right)

    try:
        while True:
            yield next(a)
            a, b = b, a
    except:
        pass


print("".join(traverse(tree)))
