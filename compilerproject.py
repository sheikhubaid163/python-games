import re

# ========== PHASE 1: LEXICAL ANALYSIS ==========
def lexical_analysis(code):
    token_spec = [
        ('NUMBER',    r'\d+'),
        ('ID',        r'[a-zA-Z_]\w*'),
        ('ASSIGN',    r'='),
        ('OP',        r'[+\-*/]'),
        ('SEMI',      r';'),
        ('SKIP',      r'[ \t]+'),
        ('MISMATCH',  r'.'),
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', value))
        elif kind == 'ID':
            if value == "int":
                tokens.append(('KEYWORD', value))
            else:
                tokens.append(('ID', value))
        elif kind == 'ASSIGN':
            tokens.append(('ASSIGN', value))
        elif kind == 'OP':
            tokens.append(('OP', value))
        elif kind == 'SEMI':
            tokens.append(('SEMI', value))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
    return tokens

# ========== PHASE 2: SYNTAX ANALYSIS ==========
def syntax_analysis(tokens):
    if len(tokens) == 7:
        types = [t[0] for t in tokens]
        expected = ['KEYWORD', 'ID', 'ASSIGN', 'NUMBER', 'OP', 'NUMBER', 'SEMI']
        return types == expected
    return False

# ========== PHASE 3: SEMANTIC ANALYSIS ==========
def semantic_analysis(tokens):
    # Check identifier isn't a number, and numbers are valid
    return tokens[1][0] == 'ID' and tokens[3][0] == 'NUMBER' and tokens[5][0] == 'NUMBER'

# ========== PHASE 4: INTERMEDIATE CODE ==========
def intermediate_code(tokens):
    var = tokens[1][1]
    num1 = tokens[3][1]
    op = tokens[4][1]
    num2 = tokens[5][1]
    return [f"t1 = {num1} {op} {num2}", f"{var} = t1"]

# ========== PHASE 5: CODE GENERATION ==========
def code_generation(tokens):
    num1 = tokens[3][1]
    num2 = tokens[5][1]
    var = tokens[1][1]
    op = tokens[4][1]

    assembly = [
        f"MOV R1, {num1}",
        f"MOV R2, {num2}"
    ]
    op_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
    if op in op_map:
        assembly.append(f"{op_map[op]} R1, R2")
    assembly.append(f"MOV {var}, R1")
    return assembly

# ========== MAIN ==========
def main():
    code = input("Enter code (e.g., int a = 3 + 5 ;): ")

    print("\n=== Lexical Analysis ===")
    tokens = lexical_analysis(code)
    for t in tokens:
        print(t)

    print("\n=== Syntax Analysis ===")
    if syntax_analysis(tokens):
        print("Syntax is correct.")
    else:
        print("Syntax Error!")
        return

    print("\n=== Semantic Analysis ===")
    if semantic_analysis(tokens):
        print("Semantic check passed.")
    else:
        print("Semantic Error!")
        return

    print("\n=== Intermediate Code ===")
    ic = intermediate_code(tokens)
    for line in ic:
        print(line)

    print("\n=== Code Generation (Assembly) ===")
    ac = code_generation(tokens)
    for line in ac:
        print(line)

if __name__ == "__main__":
    main()
