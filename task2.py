from collections import deque

def is_palindrome(line: str):
    """
    The function takes a string and determines whether it is a palindrome. 
    Returns True or False.
    """

    dq = deque()
    for char in line.lower():
        dq.append(char)

    for _ in range(len(dq) // 2):
        start = dq.popleft()
        end = dq.pop()
        if start != end:
            return False

    return True

strings = ["радар", "mother", "Anna", "Hello", "AnsSna"]

for string in strings:
    print(f"String \"{string}\" is {"" if is_palindrome(string) else "NOT "}a palindrome")
