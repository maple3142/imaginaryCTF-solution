import dis
del __builtins__.__dict__['breakpoint']
del __builtins__.__dict__['help']

print("Welcome to the python calculator!", "Pls No Steal My Flag Which Is In An Environment Variable :<", sep='\n')

if __name__ == '__main__':
    try:
        math = input('> ')
        info = dis.code_info(math).split("\n")
        assert "Stack size:        1" in info

        exec(math, {}, results := {})
        for var, res in results.items():
            print(f"{var} = {res}")
    except:
        print("smh")

# Server: python 3.8
