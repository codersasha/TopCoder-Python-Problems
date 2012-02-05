def match(param0):
    stack = []
    bracket_pairs = {'}': '{', ']': '[', ')': '('}
    for char in param0:
        if char in bracket_pairs.values():
            # opening a brace
            stack.append(char)
        elif char in bracket_pairs.keys():
            # closing a brace
            if stack[-1] == bracket_pairs[char]:
                # closed OK
                stack.pop(-1)
            else:
                # unbalanced
                return False
    if len(stack) == 0:
        return True
    return False
