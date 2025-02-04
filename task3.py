def are_brackets_symmetrical(line):
    """Gets a string and checks the symmetry of the parentheses in it."""
    stack = []
    left_brackets = ["(", "[", "{"]
    right_brackets = [")", "]", "}"]

    for char in line:
        if char in left_brackets:
            stack.append(char)

        if char in right_brackets:
            last_unclosed_bracket = stack[-1]
            if left_brackets.index(last_unclosed_bracket) == right_brackets.index(char):
                stack.pop()

    return len(stack) == 0


strings = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]


for string in strings:
    print(f"{string}: {"Symmetrical" if are_brackets_symmetrical(string) else "Unsymmetrical"}")
