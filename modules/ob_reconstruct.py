from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

def ob_reconstruct(disassembled):
    print(f"{Fore.GREEN}[INFO]: Starting reconstruction of disassembled code...")
    code_lines = disassembled.strip().split('\n')
    code = []
    
    for line in code_lines:
        parts = line.split()
        if len(parts) < 3:  # Changed from 2 to 3 to avoid index errors
            continue
        
        op = parts[2]
        print(f"{Fore.GREEN}[INFO]: Processing operation: {op}")

        if op.startswith('LOAD_CONST'):
            const_index = int(parts[4].strip('()'))
            code.append(f'const_{const_index}' if const_index != 0 else '0')
        
        elif op.startswith('LOAD_NAME'):
            name_index = int(parts[4].strip('()'))
            code.append(f'var_{name_index}')
        
        elif op.startswith('IMPORT_NAME'):
            module = parts[4].strip('()')
            code.append(f'import {module}')
        
        elif op.startswith('IMPORT_FROM'):
            name = parts[4].strip('()')
            code.append(f'from {parts[3]} import {name}')
        
        elif op.startswith('STORE_NAME'):
            name_index = int(parts[4].strip('()'))
            code.append(f'var_{name_index} = {code.pop()}')
        
        elif op.startswith('CALL_FUNCTION'):
            args = [code.pop() for _ in range(int(parts[4]))]
            func = code.pop()
            code.append(f'{func}({", ".join(args)})')
        
        elif op.startswith('RETURN_VALUE'):
            code.append('return ' + code.pop())
        
        elif op.startswith('MAKE_FUNCTION'):
            code.append(f'def function_{len(code)}(): pass')
        
        elif op.startswith('POP_TOP'):
            code.append('pass')
        
    reconstructed_code = '\n'.join(code)
    print(f"{Fore.GREEN}[SUCCESS]: Reconstruction completed.")
    return reconstructed_code
