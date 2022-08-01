#!/usr/bin/env python3
import dis

print("Welcome to the python calculator!", "Due to hardware restrictions we allow only one variable.", sep='\n')

if __name__ == '__main__':
    try:
        math = input('> ')
        info = dis.code_info(math).split('\n')
        assert 'code object' not in ''.join(info)

        if 'Names:' in info:
            for line in info[info.index('Names:'):]:
                assert '1:' not in line

        exec(math, { '__builtins__': None }, results := {})
        for var, res in results.items():
            print(f"{var} = {res}")

    except Exception as e:
        raise e
        print("smh")
