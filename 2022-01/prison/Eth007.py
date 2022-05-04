def main():
    try:
        caught = False
        cmd = input("> ")
        for x in cmd:
            if not(33<=ord(x) and ord(x)<=126) or ord(x)==43:
                caught = True
        with open("ContrabandWords.txt","r") as c:
            Contrabands = c.readlines()
        for Contraband in Contrabands:
            if Contraband.rstrip("\n") in cmd.lower():
                caught = True
        if (caught==False):
            try:
                print(eval(cmd,{"__builtins__": None}))
            except:
                pass
        else:
            print("And you were caught...")
        Continue = input("Try again [y/n]: ")
        if Continue == "y":
            main()
        else:
            print("Bye")
    except:
        print("Huh you broke my code")
        main()
print("Welcome to your jail cell")
main()
