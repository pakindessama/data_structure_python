from math import factorial, factorial2, gpaCalculator, binarySearch, pair_sum, find_missing_value
from sequences import checkAnagrams, checkAnagram2, sentence_reversal, string_compression, uniqueCharacters
from stack import Stack
from queue import Queue
from balancedParentheses import balanced

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("Type a real number to compute its factorial:")
    # number = input()
    # n = factorial2(number)
    # print(f'Result: {n}')
    # gpaCalculator()
    # data = range(0, 1000001)
    # print(max(data))
    # print(binarySearch(data, 1000000, 0, len(data)-1))
    # print(checkAnagram2("publics relation", "crap built on lies"))
    # print(checkAnagram2("d o g", "God"))
    data = [1, 2, 3, 4, 5]
    counter = pair_sum(data, 5)
    print(counter)
    # data = [1, 2, 3, 4, 5, 5, 1]
    # data2 = [1, 2, 3, 4, 5, 5]
    # print(find_missing_value(data, data2))
    # print(sentence_reversal("   This is the best   "))
    # print(string_compression("AAAaaaV"))
    # print(uniqueCharacters("abce dfj;"))
    # s = Stack()
    # print(s.isEmpty())
    # s.add("HELLO")
    # s.add("World")
    # print(s.size())
    # s.remove()
    # print(s.size())

    # q = Queue()
    # print(q.isEmpty())
    # q.enqueue("HELLO")
    # q.enqueue("World")
    # print(q.dequeue())
    # print(q.dequeue())
    # q.dequeue()
    # print(q.size())
    # print(balanced("}{({})"))
