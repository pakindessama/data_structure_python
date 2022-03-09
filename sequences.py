import collections


def checkAnagrams(text1, text2):
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    return sorted(text1) == sorted(text2)


def checkAnagram2(text1, text2):
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    counter = {}

    for c in text1:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    print(counter)
    for c in text2:
        if c in counter:
            counter[c] -= 1
        else:
            counter[c] = 1
    print(counter)
    for c in counter:
        if counter[c] > 0:
            return False
    return True


def sentence_reversal(text):
    # return " ".join(reversed(text.split()))

    reverse = ""
    text = text.split()
    i = len(text) - 1
    while i >= 0:
        reverse += text[i] + " "
        i -= 1
    return reverse


def string_compression(text):
    compressed = ""
    count = 0
    for i in range(0, len(text)):
        if i == 0:
            count += 1
        elif text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + "" + (str(count) if count > 1 else "")
            count = 1
        if i == len(text) - 1:
            compressed += text[i] + "" + (str(count) if count > 1 else "")
    return compressed


def uniqueCharacters(text):
    count = []
    text = text.replace(" ", "")
    for c in text:
        if c in count:
            return False
        else:
            count.append(c)
    return True
