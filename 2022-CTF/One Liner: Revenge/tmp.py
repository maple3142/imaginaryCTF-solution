# class G(dict):
#     def __call__(*a):
#         return {
#             **{},
#             a.__reduce__: a[0]
#         }.popitem()[len(a) % 2 * 2 - 1]

g = type(
            "",
            (dict,),
            {
                '__call__': lambda *a: {
                    **{
                        _: getattr(a[0], '__setitem__')(
                            *[
                                (i % 8 if type(i) is (1).__class__ else i)
                                for (i) in _[::-1]
                            ]
                        )
                        for (_) in a[1:]
                    },
                    a.__reduce__: a[0],
                }.popitem()[len(a) % 2 * 2 - 1],
                '__getitem__': lambda *a: dict.__getitem__(
                    *[(i % 8 if type(i) is (4).__class__ else i) for (i) in a]
                ),
            },
        )()
print(g()()() == g)
print(g((lambda: 1, 8)))
print(g((9, 7)))
print(g[16])
print(g[15])

