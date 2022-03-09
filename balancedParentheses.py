from stack import Stack


def balanced(text):
    print(text)
    if len(text) % 2 != 0:
        return False

    s = Stack()
    openings = ["[", "(", "{"]
    closing = ["]", ")", "}"]

    for t in text:
        if t in openings:
            temp = openings.index(t)
            s.add(closing[temp])
        elif s.size() == 0:
            return False
        else:
            temp = s.remove()
            if temp != t:
                return False

    return True
