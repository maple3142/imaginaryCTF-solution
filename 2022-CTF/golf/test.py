with open('golf', 'rb') as f:
    ar = f.read().split(b'\x00')

print([hex(len(x)) for x in ar if len(x)!=0])
