flag = [0] * 52


class SS:
    def __init__(self, i):
        self.i = i

    def __eq__(self, other):
        print(self.i, other)
        flag[self.i] = other
        return True


class S:
    def __init__(self, l):
        self.x = [SS(i) for i in range(l)]

    def pop(self):
        return self.x.pop()

    def reverse(self):
        self.x.reverse()


(
    lambda: print(
        [
            s := S(52),
            a := lambda z: [z.pop(), z.reverse()][0],
            [
                "no",
                [
                    "no",
                    [
                        "no",
                        [
                            "no",
                            [
                                "no",
                                [
                                    "no",
                                    [
                                        "no",
                                        [
                                            "no",
                                            [
                                                "no",
                                                [
                                                    "no",
                                                    [
                                                        "no",
                                                        [
                                                            "no",
                                                            [
                                                                "no",
                                                                [
                                                                    "no",
                                                                    [
                                                                        "no",
                                                                        [
                                                                            "no",
                                                                            [
                                                                                "no",
                                                                                [
                                                                                    "no",
                                                                                    [
                                                                                        "no",
                                                                                        [
                                                                                            "no",
                                                                                            [
                                                                                                "no",
                                                                                                [
                                                                                                    "no",
                                                                                                    [
                                                                                                        "no",
                                                                                                        [
                                                                                                            "no",
                                                                                                            [
                                                                                                                "no",
                                                                                                                [
                                                                                                                    "no",
                                                                                                                    [
                                                                                                                        "no",
                                                                                                                        [
                                                                                                                            "no",
                                                                                                                            [
                                                                                                                                "no",
                                                                                                                                [
                                                                                                                                    "no",
                                                                                                                                    [
                                                                                                                                        "no",
                                                                                                                                        [
                                                                                                                                            "no",
                                                                                                                                            [
                                                                                                                                                "no",
                                                                                                                                                [
                                                                                                                                                    "no",
                                                                                                                                                    [
                                                                                                                                                        "no",
                                                                                                                                                        [
                                                                                                                                                            "no",
                                                                                                                                                            [
                                                                                                                                                                "no",
                                                                                                                                                                [
                                                                                                                                                                    "no",
                                                                                                                                                                    [
                                                                                                                                                                        "no",
                                                                                                                                                                        [
                                                                                                                                                                            "no",
                                                                                                                                                                            [
                                                                                                                                                                                "no",
                                                                                                                                                                                [
                                                                                                                                                                                    "no",
                                                                                                                                                                                    [
                                                                                                                                                                                        "no",
                                                                                                                                                                                        [
                                                                                                                                                                                            "no",
                                                                                                                                                                                            [
                                                                                                                                                                                                "no",
                                                                                                                                                                                                [
                                                                                                                                                                                                    "no",
                                                                                                                                                                                                    [
                                                                                                                                                                                                        "no",
                                                                                                                                                                                                        [
                                                                                                                                                                                                            "no",
                                                                                                                                                                                                            [
                                                                                                                                                                                                                "no",
                                                                                                                                                                                                                [
                                                                                                                                                                                                                    "no",
                                                                                                                                                                                                                    [
                                                                                                                                                                                                                        "no",
                                                                                                                                                                                                                        "yes",
                                                                                                                                                                                                                    ][
                                                                                                                                                                                                                        a(
                                                                                                                                                                                                                            s
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                        == "}"
                                                                                                                                                                                                                    ],
                                                                                                                                                                                                                ][
                                                                                                                                                                                                                    a(
                                                                                                                                                                                                                        s
                                                                                                                                                                                                                    )
                                                                                                                                                                                                                    == "i"
                                                                                                                                                                                                                ],
                                                                                                                                                                                                            ][
                                                                                                                                                                                                                a(
                                                                                                                                                                                                                    s
                                                                                                                                                                                                                )
                                                                                                                                                                                                                == "p"
                                                                                                                                                                                                            ],
                                                                                                                                                                                                        ][
                                                                                                                                                                                                            a(
                                                                                                                                                                                                                s
                                                                                                                                                                                                            )
                                                                                                                                                                                                            == "c"
                                                                                                                                                                                                        ],
                                                                                                                                                                                                    ][
                                                                                                                                                                                                        a(
                                                                                                                                                                                                            s
                                                                                                                                                                                                        )
                                                                                                                                                                                                        == "u"
                                                                                                                                                                                                    ],
                                                                                                                                                                                                ][
                                                                                                                                                                                                    a(
                                                                                                                                                                                                        s
                                                                                                                                                                                                    )
                                                                                                                                                                                                    == "t"
                                                                                                                                                                                                ],
                                                                                                                                                                                            ][
                                                                                                                                                                                                a(
                                                                                                                                                                                                    s
                                                                                                                                                                                                )
                                                                                                                                                                                                == "t"
                                                                                                                                                                                            ],
                                                                                                                                                                                        ][
                                                                                                                                                                                            a(
                                                                                                                                                                                                s
                                                                                                                                                                                            )
                                                                                                                                                                                            == "f"
                                                                                                                                                                                        ],
                                                                                                                                                                                    ][
                                                                                                                                                                                        a(
                                                                                                                                                                                            s
                                                                                                                                                                                        )
                                                                                                                                                                                        == "e"
                                                                                                                                                                                    ],
                                                                                                                                                                                ][
                                                                                                                                                                                    a(
                                                                                                                                                                                        s
                                                                                                                                                                                    )
                                                                                                                                                                                    == "{"
                                                                                                                                                                                ],
                                                                                                                                                                            ][
                                                                                                                                                                                a(
                                                                                                                                                                                    s
                                                                                                                                                                                )
                                                                                                                                                                                == "g"
                                                                                                                                                                            ],
                                                                                                                                                                        ][
                                                                                                                                                                            a(
                                                                                                                                                                                s
                                                                                                                                                                            )
                                                                                                                                                                            == "h"
                                                                                                                                                                        ],
                                                                                                                                                                    ][
                                                                                                                                                                        a(
                                                                                                                                                                            s
                                                                                                                                                                        )
                                                                                                                                                                        == "t"
                                                                                                                                                                    ],
                                                                                                                                                                ][
                                                                                                                                                                    a(
                                                                                                                                                                        s
                                                                                                                                                                    )
                                                                                                                                                                    == "e"
                                                                                                                                                                ],
                                                                                                                                                            ][
                                                                                                                                                                a(
                                                                                                                                                                    s
                                                                                                                                                                )
                                                                                                                                                                == "n"
                                                                                                                                                            ],
                                                                                                                                                        ][
                                                                                                                                                            a(
                                                                                                                                                                s
                                                                                                                                                            )
                                                                                                                                                            == "l"
                                                                                                                                                        ],
                                                                                                                                                    ][
                                                                                                                                                        a(
                                                                                                                                                            s
                                                                                                                                                        )
                                                                                                                                                        == "a"
                                                                                                                                                    ],
                                                                                                                                                ][
                                                                                                                                                    a(
                                                                                                                                                        s
                                                                                                                                                    )
                                                                                                                                                    == "p"
                                                                                                                                                ],
                                                                                                                                            ][
                                                                                                                                                a(
                                                                                                                                                    s
                                                                                                                                                )
                                                                                                                                                == "c"
                                                                                                                                            ],
                                                                                                                                        ][
                                                                                                                                            a(
                                                                                                                                                s
                                                                                                                                            )
                                                                                                                                            == "s"
                                                                                                                                        ],
                                                                                                                                    ][
                                                                                                                                        a(
                                                                                                                                            s
                                                                                                                                        )
                                                                                                                                        == "i"
                                                                                                                                    ],
                                                                                                                                ][
                                                                                                                                    a(
                                                                                                                                        s
                                                                                                                                    )
                                                                                                                                    == "o"
                                                                                                                                ],
                                                                                                                            ][
                                                                                                                                a(
                                                                                                                                    s
                                                                                                                                )
                                                                                                                                == "d"
                                                                                                                            ],
                                                                                                                        ][
                                                                                                                            a(
                                                                                                                                s
                                                                                                                            )
                                                                                                                            == "m"
                                                                                                                        ],
                                                                                                                    ][
                                                                                                                        a(
                                                                                                                            s
                                                                                                                        )
                                                                                                                        == "n"
                                                                                                                    ],
                                                                                                                ][
                                                                                                                    a(
                                                                                                                        s
                                                                                                                    )
                                                                                                                    == "e"
                                                                                                                ],
                                                                                                            ][
                                                                                                                a(
                                                                                                                    s
                                                                                                                )
                                                                                                                == "a"
                                                                                                            ],
                                                                                                        ][
                                                                                                            a(
                                                                                                                s
                                                                                                            )
                                                                                                            == "o"
                                                                                                        ],
                                                                                                    ][
                                                                                                        a(
                                                                                                            s
                                                                                                        )
                                                                                                        == "s"
                                                                                                    ],
                                                                                                ][
                                                                                                    a(
                                                                                                        s
                                                                                                    )
                                                                                                    == "n"
                                                                                                ],
                                                                                            ][
                                                                                                a(
                                                                                                    s
                                                                                                )
                                                                                                == "r"
                                                                                            ],
                                                                                        ][
                                                                                            a(
                                                                                                s
                                                                                            )
                                                                                            == "e"
                                                                                        ],
                                                                                    ][
                                                                                        a(
                                                                                            s
                                                                                        )
                                                                                        == "a"
                                                                                    ],
                                                                                ][
                                                                                    a(s)
                                                                                    == "s"
                                                                                ],
                                                                            ][
                                                                                a(s)
                                                                                == "h"
                                                                            ],
                                                                        ][a(s) == "t"],
                                                                    ][a(s) == "c"],
                                                                ][a(s) == "o"],
                                                            ][a(s) == "g"],
                                                        ][a(s) == "l"],
                                                    ][a(s) == "n"],
                                                ][a(s) == "e"],
                                            ][a(s) == "i"],
                                        ][a(s) == "a"],
                                    ][a(s) == "c"],
                                ][a(s) == "l"],
                            ][a(s) == "a"],
                        ][a(s) == "l"],
                    ][a(s) == "p"],
                ][a(s) == "m"],
            ][a(s) == "s"],
            "no",
        ][::-1][a(s) == "y"]
    )
)()
print("".join(flag))
