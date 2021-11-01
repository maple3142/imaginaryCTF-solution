from Crypto.Util.number import long_to_bytes

F = GF(2)

state = [F(b) for b in f"{4876348763:0256b}"]


def next_state(state):
    b = 0
    for i in range(0, 250, 2):
        b += state[i]
    return state[1:] + [b]


lhs, rhs = [], []
for _ in range(256):
    lhs.append(state)
    rhs.append(next_state(state)[-1])
    state = next_state(state)
v = matrix(lhs).T.solve_left(vector(rhs))


def nxt(state):
    return state[1:] + [v * vector(state)]


for _ in range(30):
    print(vector(nxt(state)) == vector(next_state(state)))
    state = next_state(state)

state = [F(b) for b in f"{4876348763:0256b}"]

lhs, rhs = [], []
for _ in range(256):
    lhs.append(next_state(state))
    rhs.append(state[0])
    state = next_state(state)
v = matrix(lhs).T.solve_left(vector(rhs))


def prev(state):
    return [v * vector(state)] + state[:-1]


for _ in range(20):
    print(prev(next_state(state)) == state)
    state = prev(state)

M = matrix(v).stack(matrix.identity(255).augment(vector([0] * 255)))


target = bytes.fromhex(
    "98cb7f18bb2e8f0fdc857d6bac4878f4be43b6c4ac87ad212e3e1566929736c0"
)

state = vector(state)

for _ in range(20):
    print(M * vector(next_state(list(state))) == state)
    state = M * state

state = vector([F(b) for b in f'{int.from_bytes(target, "big"):0256b}'[::-1]])
suffix = vector([F(b) for b in f'{int.from_bytes(b"ictf", "big"):032b}'[::-1]])

for _ in range(256 * 500):
    if state[-len(suffix) :] == suffix:
        s = long_to_bytes(int("".join(map(str, state[::-1])), 2))
        print(s)
        break
    state = M * state

# ictf{I_hop3_I_get_g00d_feedback}
