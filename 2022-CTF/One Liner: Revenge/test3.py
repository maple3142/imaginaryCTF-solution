# input_len = 24
[
    # globals().__setitem__(chr(0x67), globals()),
    g := globals(),
    # g.__setitem__(chr(0x74), lambda *a: bytes.fromhex("{:x}".format(a[0])).decode()),
    t := lambda *a: bytes.fromhex("{:x}".format(a[0])).decode(),
    g.__setitem__(
        'g',
        type(
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
        )(),
    ),
    [
        g((lambda *a: (print(*a), exit()), 13463))(
            (
                type(
                    "",
                    ([].__class__,),
                    {
                        '__hash__': lambda *a: 1,
                        '__call__': lambda *a: g(
                            ([a[0].insert(0, list.pop(a[0])), a[0]][1][a[-1]], 14701)
                        ),
                        'append': lambda *a: [
                            list.append(a[0], _) for (_) in a[1:]
                        ],
                        'pop': lambda *a: (list.pop(a[0]), a[0].reverse())[0],
                    },
                )(),
                10397,
            )
        )[5].append(*[g()[5], *[lambda *a: g[7]('no')] * 15]),
        g((open('revenge.py').read(), 14122)),
        g()[7],
    ][
        any(
            any(_ in '#\n#\n#\n#\n' for (_) in (i))
            for (i) in open('revenge.py')
        )
        + 1
    ](
        ('no', 'newlines!')
    ),
    [
        g(
            (
                g((lambda *a: int("".join(str(1 * i) for (i) in (a)), 2), 12614))[
                    15301
                ].__getattribute__('__class__')(),
                13195,
            )
        )[3].append(
            *(
                lambda *a: (
                    51 * a[2] + 56 * a[0] + 12 * a[6] + 91 * a[3] + 9 * a[6]
                    == 96 * a[3]
                    + 96 * a[1]
                    + 83 * a[1]
                    + 91 * a[1]
                    + 43 * a[6]
                    - 11543,
                    88 * a[7] + 51 * a[7] + 27 * a[1] + 77 * a[1] + 45 * a[4]
                    == 53 * a[7]
                    + 6 * a[6]
                    + 92 * a[5]
                    + 15 * a[1]
                    + 86 * a[6]
                    + 7184,
                    63 * a[3] + 76 * a[0] + 93 * a[5] + 64 * a[3] + 17 * a[6]
                    == 74 * a[7]
                    + 30 * a[3]
                    + 21 * a[1]
                    + 63 * a[0]
                    + 66 * a[7]
                    + 405,
                    33 * a[6] + 47 * a[6] + 10 * a[7] + 97 * a[2] + 86 * a[2]
                    == 85 * a[0]
                    + 92 * a[5]
                    + 45 * a[3]
                    + 68 * a[7]
                    + 15 * a[2]
                    - 9791,
                ),
                lambda *a: (
                    67 * a[0] + 13 * a[5] + 16 * a[3] + 17 * a[4] + 44 * a[1]
                    == 36 * a[6]
                    + 38 * a[7]
                    + 72 * a[7]
                    + 89 * a[3]
                    + 43 * a[1]
                    - 13909,
                    36 * a[3] + 8 * a[5] + 43 * a[7] + 73 * a[7] + 78 * a[3]
                    == 31 * a[0]
                    + 15 * a[6]
                    + 66 * a[4]
                    + 48 * a[5]
                    + 5 * a[4]
                    + 9943,
                    23 * a[3] + 68 * a[7] + 10 * a[0] + 59 * a[1] + 34 * a[1]
                    == 20 * a[2]
                    + 55 * a[1]
                    + 20 * a[1]
                    + 32 * a[6]
                    + 39 * a[2]
                    + 3539,
                    5 * a[0] + 69 * a[2] + 25 * a[2] + 61 * a[1] + 97 * a[6]
                    == 64 * a[2]
                    + 29 * a[2]
                    + 39 * a[2]
                    + 93 * a[0]
                    + 23 * a[7]
                    - 5075,
                ),
                lambda *a: (
                    2 * a[4] + 47 * a[0] + 80 * a[0] + 37 * a[4] + 60 * a[7]
                    == 29 * a[5]
                    + 21 * a[3]
                    + 4 * a[7]
                    + 83 * a[1]
                    + 55 * a[0]
                    + 10561,
                    28 * a[4] + 42 * a[0] + 39 * a[0] + 3 * a[4] + 63 * a[1]
                    == 11 * a[2]
                    + 31 * a[3]
                    + 9 * a[3]
                    + 30 * a[0]
                    + 74 * a[0]
                    + 2148,
                    78 * a[5] + 4 * a[7] + 62 * a[2] + 84 * a[7] + 96 * a[0]
                    == 24 * a[7]
                    + 23 * a[6]
                    + 94 * a[3]
                    + 46 * a[2]
                    + 67 * a[1]
                    + 7330,
                    74 * a[4] + 66 * a[0] + 92 * a[2] + 73 * a[0] + 62 * a[2]
                    == 18 * a[2]
                    + 28 * a[3]
                    + 40 * a[1]
                    + 60 * a[5]
                    + 54 * a[1]
                    + 19097,
                ),
                lambda *a: (
                    49 * a[5] + 62 * a[4] + 39 * a[3] + 6 * a[2] + 33 * a[2]
                    == 65 * a[6]
                    + 40 * a[3]
                    + 51 * a[3]
                    + 38 * a[6]
                    + 61 * a[1]
                    + 1787,
                    72 * a[2] + 41 * a[1] + 17 * a[2] + 94 * a[1] + 64 * a[6]
                    == 53 * a[0]
                    + 69 * a[7]
                    + 30 * a[1]
                    + 27 * a[3]
                    + 17 * a[0]
                    + 13621,
                    76 * a[4] + 52 * a[6] + 42 * a[4] + 32 * a[5] + 15 * a[4]
                    == 93 * a[0]
                    + 45 * a[2]
                    + 76 * a[7]
                    + 30 * a[0]
                    + 97 * a[6]
                    - 8576,
                    49 * a[5] + 5 * a[0] + 66 * a[6] + 6 * a[0] + 15 * a[4]
                    == 58 * a[3]
                    + 78 * a[7]
                    + 41 * a[2]
                    + 3 * a[7]
                    + 41 * a[5]
                    - 14144,
                ),
                lambda *a: (
                    81 * a[7] + 15 * a[6] + 83 * a[5] + 51 * a[2] + 25 * a[7]
                    == 78 * a[0]
                    + 36 * a[2]
                    + 89 * a[0]
                    + 74 * a[1]
                    + 28 * a[7]
                    - 5576,
                    22 * a[4] + 69 * a[7] + 43 * a[6] + 22 * a[4] + 88 * a[4]
                    == 92 * a[6]
                    + 40 * a[2]
                    + 13 * a[5]
                    + 93 * a[4]
                    + 69 * a[0]
                    - 14574,
                    5 * a[4] + 55 * a[7] + 38 * a[7] + 79 * a[2] + 73 * a[2]
                    == 7 * a[6]
                    + 68 * a[5]
                    + 46 * a[3]
                    + 56 * a[7]
                    + 84 * a[7]
                    - 1064,
                    63 * a[5] + 3 * a[7] + 54 * a[3] + 53 * a[1] + 39 * a[6]
                    == 90 * a[5]
                    + 58 * a[7]
                    + 80 * a[6]
                    + 43 * a[4]
                    + 1 * a[2]
                    - 9663,
                ),
                lambda *a: (
                    33 * a[4] + 85 * a[6] + 88 * a[3] + 11 * a[3] + 65 * a[3]
                    == 2 * a[4]
                    + 83 * a[7]
                    + 51 * a[3]
                    + 53 * a[2]
                    + 4 * a[7]
                    + 2150,
                    16 * a[5] + 6 * a[5] + 19 * a[7] + 49 * a[5] + 48 * a[1]
                    == 96 * a[4]
                    + 60 * a[7]
                    + 73 * a[3]
                    + 79 * a[1]
                    + 67 * a[5]
                    - 17330,
                    32 * a[6] + 25 * a[6] + 36 * a[4] + 96 * a[3] + 74 * a[7]
                    == 65 * a[6]
                    + 97 * a[3]
                    + 22 * a[5]
                    + 82 * a[6]
                    + 58 * a[4]
                    - 15919,
                    58 * a[6] + 91 * a[6] + 48 * a[7] + 60 * a[5] + 84 * a[1]
                    == 81 * a[6]
                    + 3 * a[2]
                    + 3 * a[7]
                    + 17 * a[5]
                    + 28 * a[3]
                    + 23080,
                ),
                lambda *a: (
                    8 * a[3] + 13 * a[7] + 70 * a[4] + 4 * a[6] + 25 * a[0]
                    == 47 * a[5]
                    + 56 * a[1]
                    + 14 * a[0]
                    + 14 * a[5]
                    + 47 * a[3]
                    - 2509,
                    56 * a[0] + 35 * a[7] + 71 * a[7] + 82 * a[3] + 43 * a[2]
                    == 89 * a[1]
                    + 5 * a[4]
                    + 38 * a[2]
                    + 16 * a[1]
                    + 16 * a[0]
                    + 13008,
                    60 * a[6] + 16 * a[2] + 79 * a[3] + 5 * a[6] + 99 * a[7]
                    == 22 * a[4]
                    + 75 * a[3]
                    + 31 * a[6]
                    + 4 * a[7]
                    + 53 * a[3]
                    + 1557,
                    22 * a[4] + 36 * a[3] + 84 * a[0] + 6 * a[6] + 44 * a[7]
                    == 94 * a[2]
                    + 46 * a[0]
                    + 7 * a[1]
                    + 16 * a[5]
                    + 69 * a[7]
                    - 5508,
                ),
                lambda *a: (
                    15 * a[6] + 37 * a[4] + 89 * a[3] + 1 * a[5] + 40 * a[5]
                    == 58 * a[7]
                    + 84 * a[2]
                    + 95 * a[1]
                    + 88 * a[7]
                    + 58 * a[0]
                    - 13680,
                    21 * a[2] + 72 * a[0] + 92 * a[6] + 29 * a[0] + 94 * a[0]
                    == 60 * a[5]
                    + 90 * a[0]
                    + 64 * a[1]
                    + 66 * a[2]
                    + 45 * a[2]
                    - 7275,
                    85 * a[4] + 56 * a[5] + 39 * a[4] + 5 * a[1] + 86 * a[5]
                    == 46 * a[3]
                    + 85 * a[2]
                    + 79 * a[4]
                    + 84 * a[3]
                    + 87 * a[2]
                    - 3608,
                    98 * a[5] + 9 * a[0] + 94 * a[5] + 81 * a[0] + 92 * a[0]
                    == 18 * a[0]
                    + 30 * a[0]
                    + 18 * a[1]
                    + 17 * a[1]
                    + 9 * a[2]
                    + 32955,
                ),
                lambda *a: (
                    99 * a[5] + 17 * a[0] + 43 * a[6] + 35 * a[7] + 63 * a[3]
                    == 75 * a[7]
                    + 65 * a[3]
                    + 44 * a[1]
                    + 68 * a[6]
                    + 71 * a[6]
                    - 6000,
                    96 * a[7] + 77 * a[3] + 70 * a[6] + 36 * a[5] + 40 * a[4]
                    == 92 * a[0]
                    + 78 * a[5]
                    + 18 * a[5]
                    + 27 * a[3]
                    + 64 * a[3]
                    - 2898,
                    64 * a[1] + 94 * a[1] + 20 * a[0] + 57 * a[6] + 76 * a[5]
                    == 57 * a[2]
                    + 66 * a[5]
                    + 82 * a[0]
                    + 95 * a[7]
                    + 70 * a[3]
                    - 16423,
                    35 * a[1] + 43 * a[6] + 7 * a[5] + 88 * a[1] + 72 * a[3]
                    == 79 * a[6]
                    + 66 * a[1]
                    + 43 * a[1]
                    + 80 * a[6]
                    + 13 * a[6]
                    - 16177,
                ),
                lambda *a: (
                    15 * a[6] + 72 * a[0] + 60 * a[2] + 66 * a[1] + 57 * a[6]
                    == 43 * a[5] + 79 * a[2] + 3 * a[0] + 17 * a[1] + 64 * a[6] + 4715,
                    46 * a[0] + 93 * a[3] + 59 * a[4] + 15 * a[6] + 84 * a[6]
                    == 49 * a[2]
                    + 46 * a[6]
                    + 41 * a[6]
                    + 37 * a[1]
                    + 98 * a[5]
                    + 3571,
                    50 * a[4] + 62 * a[5] + 24 * a[1] + 91 * a[7] + 59 * a[0]
                    == 52 * a[4]
                    + 37 * a[5]
                    + 60 * a[2]
                    + 59 * a[2]
                    + 25 * a[3]
                    + 6503,
                    19 * a[3] + 96 * a[3] + 38 * a[6] + 34 * a[5] + 27 * a[6]
                    == 61 * a[5]
                    + 74 * a[2]
                    + 1 * a[2]
                    + 86 * a[1]
                    + 62 * a[5]
                    - 14623,
                ),
                lambda *a: (
                    94 * a[5] + 46 * a[0] + 21 * a[6] + 46 * a[0] + 49 * a[1]
                    == 81 * a[0] + 97 * a[0] + 82 * a[4] + 4 * a[6] + 67 * a[0] - 10410,
                    65 * a[1] + 26 * a[7] + 14 * a[7] + 51 * a[6] + 20 * a[4]
                    == 19 * a[2]
                    + 87 * a[0]
                    + 27 * a[5]
                    + 57 * a[2]
                    + 88 * a[6]
                    - 10505,
                    83 * a[1] + 89 * a[5] + 57 * a[5] + 19 * a[3] + 42 * a[3]
                    == 12 * a[0] + 7 * a[0] + 83 * a[1] + 8 * a[2] + 79 * a[5] + 20536,
                    30 * a[3] + 67 * a[1] + 10 * a[1] + 13 * a[2] + 47 * a[1]
                    == 87 * a[2]
                    + 95 * a[3]
                    + 9 * a[7]
                    + 41 * a[3]
                    + 80 * a[0]
                    - 11542,
                ),
                lambda *a: (
                    98 * a[4] + 29 * a[0] + 91 * a[0] + 25 * a[5] + 94 * a[4]
                    == 41 * a[1]
                    + 63 * a[3]
                    + 61 * a[7]
                    + 28 * a[2]
                    + 89 * a[7]
                    + 17506,
                    28 * a[0] + 90 * a[0] + 12 * a[4] + 65 * a[6] + 69 * a[5]
                    == 87 * a[3]
                    + 33 * a[4]
                    + 20 * a[6]
                    + 10 * a[7]
                    + 23 * a[7]
                    + 11861,
                    52 * a[3] + 99 * a[3] + 62 * a[1] + 69 * a[4] + 36 * a[3]
                    == 71 * a[0]
                    + 25 * a[7]
                    + 49 * a[6]
                    + 56 * a[0]
                    + 87 * a[2]
                    - 3286,
                    95 * a[0] + 24 * a[2] + 11 * a[5] + 40 * a[3] + 85 * a[2]
                    == 37 * a[1]
                    + 49 * a[3]
                    + 15 * a[2]
                    + 51 * a[3]
                    + 71 * a[6]
                    + 8832,
                ),
                lambda *a: (
                    22 * a[7] + 92 * a[5] + 66 * a[5] + 16 * a[3] + 89 * a[1]
                    == 45 * a[6]
                    + 26 * a[1]
                    + 88 * a[2]
                    + 78 * a[6]
                    + 29 * a[3]
                    + 11656,
                    53 * a[3] + 77 * a[2] + 61 * a[7] + 81 * a[0] + 30 * a[7]
                    == 70 * a[0]
                    + 89 * a[6]
                    + 4 * a[5]
                    + 23 * a[7]
                    + 94 * a[2]
                    + 9747,
                    90 * a[4] + 70 * a[2] + 53 * a[0] + 26 * a[5] + 29 * a[4]
                    == 73 * a[6]
                    + 21 * a[5]
                    + 6 * a[7]
                    + 88 * a[1]
                    + 43 * a[1]
                    + 3403,
                    62 * a[3] + 59 * a[2] + 88 * a[0] + 77 * a[1] + 37 * a[5]
                    == 88 * a[4]
                    + 81 * a[1]
                    + 49 * a[1]
                    + 81 * a[0]
                    + 28 * a[2]
                    - 2875,
                ),
                lambda *a: (
                    22 * a[7] + 44 * a[2] + 18 * a[6] + 73 * a[1] + 51 * a[4]
                    == 40 * a[6]
                    + 97 * a[5]
                    + 27 * a[4]
                    + 70 * a[7]
                    + 66 * a[7]
                    - 10554,
                    18 * a[7] + 76 * a[4] + 94 * a[2] + 1 * a[0] + 87 * a[5]
                    == 90 * a[1]
                    + 20 * a[5]
                    + 86 * a[2]
                    + 28 * a[4]
                    + 89 * a[0]
                    - 7968,
                    14 * a[1] + 38 * a[4] + 4 * a[2] + 63 * a[6] + 54 * a[6]
                    == 48 * a[3]
                    + 69 * a[6]
                    + 60 * a[7]
                    + 35 * a[6]
                    + 87 * a[7]
                    - 11706,
                    68 * a[2] + 78 * a[7] + 31 * a[2] + 45 * a[1] + 73 * a[5]
                    == 23 * a[7] + 14 * a[7] + 91 * a[4] + 99 * a[4] + 8 * a[0] - 445,
                ),
                lambda *a: (
                    50 * a[1] + 66 * a[4] + 19 * a[4] + 56 * a[5] + 22 * a[7]
                    == 77 * a[2]
                    + 76 * a[2]
                    + 79 * a[3]
                    + 87 * a[0]
                    + 65 * a[5]
                    - 19932,
                    90 * a[3] + 11 * a[1] + 61 * a[5] + 27 * a[0] + 43 * a[3]
                    == 11 * a[0]
                    + 41 * a[3]
                    + 4 * a[5]
                    + 57 * a[3]
                    + 54 * a[7]
                    + 7163,
                    24 * a[2] + 7 * a[0] + 81 * a[7] + 42 * a[6] + 30 * a[4]
                    == 35 * a[2]
                    + 4 * a[6]
                    + 87 * a[2]
                    + 88 * a[5]
                    + 46 * a[2]
                    - 1649,
                    27 * a[5] + 34 * a[4] + 16 * a[0] + 39 * a[7] + 89 * a[2]
                    == 58 * a[1]
                    + 22 * a[4]
                    + 6 * a[6]
                    + 20 * a[4]
                    + 1 * a[6]
                    + 7194,
                ),
                lambda *a: (
                    39 * a[5] + 95 * a[0] + 29 * a[4] + 35 * a[4] + 2 * a[7]
                    == 52 * a[3]
                    + 36 * a[5]
                    + 72 * a[4]
                    + 47 * a[2]
                    + 27 * a[4]
                    - 837,
                    37 * a[5] + 78 * a[1] + 79 * a[7] + 73 * a[6] + 96 * a[6]
                    == 51 * a[2]
                    + 71 * a[4]
                    + 79 * a[2]
                    + 60 * a[0]
                    + 32 * a[6]
                    + 3156,
                    95 * a[1] + 8 * a[1] + 35 * a[0] + 22 * a[7] + 89 * a[7]
                    == 26 * a[4]
                    + 50 * a[2]
                    + 67 * a[1]
                    + 70 * a[2]
                    + 30 * a[6]
                    + 1114,
                    87 * a[7] + 56 * a[2] + 41 * a[7] + 22 * a[3] + 44 * a[3]
                    == 81 * a[6]
                    + 79 * a[4]
                    + 40 * a[6]
                    + 37 * a[7]
                    + 66 * a[4]
                    - 10364,
                ),
            )
        ),
        g((input('>>> ').encode(), 15553)),
        g[7],
    ][('f\n'[1] in g()[2]) + 1](
        ('stop trying to debug me', 'fool!')
    ),
    [
        g[5](g()[6](*g()[3].pop()(*g()[(3).__class__(g[2][2])])))
        for (i) in iter(g()[3].__len__, 0)
    ],
    g[7]('yes'),
]


