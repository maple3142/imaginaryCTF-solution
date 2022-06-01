#!/usr/bin/env python3

from copy import deepcopy
import asyncio

class MemoryException(Exception):
    pass

class Memory():
    def __init__(self, max_addr=4096):
        self.cache = {}
        self.mem = [0]*max_addr
        self.backup_mem = [0]*max_addr
        self.max_addr = max_addr

    def flush_cache(self):
        self.cache = {}

    def backup(self):
        self.backup_mem = deepcopy(self.mem)

    def rollback(self):
        self.mem = deepcopy(self.backup_mem)

    async def read(self, addr):
        if not(0 <= addr < self.max_addr):
            raise MemoryException(f"addr {addr} not in memory range (0, {self.max_addr})")
        if addr in self.cache:
            return self.cache[addr]
        self.cache[addr] = self.mem[addr]
        # main memory read is slow
        await asyncio.sleep(.1)
        return self.cache[addr]

    async def write(self, addr, char):
        val = abs(char)&0xFF
        self.mem[addr] = val
        self.cache[addr] = val
        # main memory write is slow
        await asyncio.sleep(.1)


class Parser():
    def __init__(self):
        self.commands = {
            "FLUSH": self.flush,
            "READ": self.read,
            "WRITE": self.write,
            "HELP": self.help,
            "SOURCE": self.source
        }

        # forgive the formatting here, python hates multiline strings
        self.help_text = {
            "FLUSH": '''Usage: FLUSH

Flushes the memory cache.''',
            "READ": '''Usage: READ [expr]

Reads the byte stored at address [expr].
[expr] is an expression of an address which can use indexing.
An int, such as 1 or 1024, is a valid address.
Additionally, you can provide an index in square brackets.
An example would be 1000[3], which would correspond to 1000+3 = 1003.
Indices can be nested - inner indices correspond to memory reads.
For example, 1000[100[5]] is the address 1000 + the memory at 105.''',
            "WRITE": '''Usage: WRITE [expr] [byte]

Writes [byte] to address [expr].
[expr] is an expression of an address which can use indexing.
An int, such as 1 or 1024, is a valid address.
Additionally, you can provide an index in square brackets.
An example would be 1000[3], which would correspond to 1000+3 = 1003.
Indices can be nested - inner indices correspond to memory reads.
For example, 1000[100[5]] is the address 1000 + the memory at 105.''',
            "HELP": f'''USAGE: HELP [command]

Displays help about a given command. If no command is provided, displays this text.

Valid commands:
{chr(10).join(' '*4+i for i in self.commands)}''',
"SOURCE": '''Usage: SOURCE

Displays the source of this file.'''
        }

        self.vars = {}
        self.mem = Memory()
        self.min_addr = 0
        self.max_addr = 1024

        self.needed_admin = False

        asyncio.run(self.write_flag())

        self.flush()

    async def write_flag(self):
        flag = open("flag.txt").read()
        addr = 2048
        tasks = []
        for c in flag:
            task = asyncio.create_task(self.mem.write(addr, ord(c)))
            tasks.append(task)
            addr += 1
        await asyncio.gather(*tasks)

    def flush(self, *args):
        self.mem.flush_cache()
        return "Flushed cache."

    def parse_addr(self, expr):
        expr = expr.replace(']', '')
        if any(i not in '1234567890[' for i in expr):
            raise MemoryException(f"Invalid characters in address expression {expr}")
        if '[[' in expr:
            raise MemoryException(f"Invalid indexing syntax in address expression {expr}")
        nums = [int(i) for i in expr.split('[')]
        while len(nums) > 1:
            temp_addr = nums[-1] + nums[-2]
            nums = nums[:-2]
            nums.append(self.read(str(temp_addr), privileged=True))
        return nums[0]

    def read(self, *args, privileged=False):
        if len(args) != 1:
            raise MemoryException('Incorrect args passed to READ - try HELP READ for usage details')
        try:
            addr = self.parse_addr(args[0])
        except ValueError:
            raise MemoryException(f"Unable to parse address '{args[0]}'")
        ret = asyncio.run(self.read_helper(addr, privileged=privileged))
        if not privileged and (ret == -1 or self.needed_admin):
            raise MemoryException("You don't have permission to read there!")
        return ret

    async def read_helper(self, addr, privileged=False):
        # memory read can be slow, so we start it now just in case it's needed later
        read_task = asyncio.create_task(self.mem.read(addr))
        if not(self.min_addr <= addr < self.max_addr):
            if not privileged:
                return -1
            else:
                self.needed_admin = True
        return await read_task

    def write(self, *args):
        if len(args) != 2:
            raise MemoryException('Incorrect args passed to WRITE - try HELP WRITE for usage details')
        try:
            addr = self.parse_addr(args[0])
        except ValueError:
            raise MemoryException(f"Unable to parse address '{args[0]}'")
        try:
            char = abs(int(args[1]))&0xFF
        except ValueError:
            raise MemoryException(f"Unable to parse byte '{args[1]}'")
        ret = asyncio.run(self.write_helper(addr, char))
        if ret == -1:
            raise MemoryException("You don't have permission to write there!")
        return ret

    async def write_helper(self, addr, char):
        self.mem.backup()
        # memory write can be slow, so we start it now just in case it's needed later
        write_task = asyncio.create_task(self.mem.write(addr, char))
        if not(self.min_addr <= addr < self.max_addr):
            self.mem.rollback()
            return -1
        await write_task
        return f"Wrote {char} to address {addr} successfully."

    def help(self, *args):
        if len(args) == 0 or args[0] not in self.help_text:
            return self.help_text['HELP']
        else:
            return self.help_text[args[0]]

    def source(self, *args):
        return open(__file__).read()

    def parse_command(self, cmd):
        self.needed_admin = False
        args = cmd.split()
        if len(args) == 0:
            raise MemoryException("No command entered.")
        if args[0] not in self.commands:
            raise MemoryException(f"Unrecognized command '{args[0]}'.")
        return self.commands[args[0]](*args[1:])

    def run(self):
        print("Enter 'HELP' for help.")
        while True:
            try:
                cmd = input(">>> ")
                print(self.parse_command(cmd))
            except MemoryException as e:
                print("Error: "+str(e))

if __name__ == '__main__':
    Parser().run()
