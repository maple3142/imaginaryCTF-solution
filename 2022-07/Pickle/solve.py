import pickle

class FlagPrinter:
    pass


with open('out.pickle', 'rb') as f:
    r = pickle.load(f)
    print(bytes(r.flag))

# cat out.pickle -A | sed 's/K//g' | grep -Po 'ictf{.*?}'
# ictf{cucumbers_or_pickles?}
