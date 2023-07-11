import dis

def run_bytecode(bytecode):
    code_obj = compile(bytecode, '<string>', 'exec')
    dis.dis(code_obj)
    exec(code_obj)

bytecode = """
print("Hello, world!")
x = 10
y = 20
print(x + y)
"""

run_bytecode(bytecode)