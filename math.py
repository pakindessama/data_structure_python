import collections


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def factorial2(n):
    try:
        n = int(n)
        if n == 0:
            return 1
        else:
            return n * factorial2(n - 1)
    except ValueError:
        return "Invalid input"


def gpaCalculator():
    print("""
    welcome to GPA calculator
    Enter all your later grades, one per line
    Enter blank to designate the end""")
    end = False
    points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67,
              "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33, "D": 1.0, "F": 0.0}
    print(sorted(points))
    numberOfCourses = 0
    totalPoints = 0
    while not end:
        grade = input()
        if grade == "":
            end = True
        elif grade not in points:
            print("Invalid input")
        else:
            totalPoints += points[grade]
            numberOfCourses += 1
    try:
        print("GPA:{0:.3}".format(totalPoints / numberOfCourses))
    except ValueError:
        print("Invalid data")


def binarySearch(data, target, low, high):
    try:
        if (data[low] == target) or (data[high] == target):
            return True
    except IndexError:
        print("")
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            return binarySearch(data, target, low, mid - 1)
        else:
            return binarySearch(data, target, mid + 1, high)


# O(n*n) complexity
# def pair_sum(arr, target):
#     counter = 0
#     if len(arr) < 2:
#         return
#     for i in range(0, len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 counter += 1
#                 print(f"({arr[i]}, {arr[j]})")
#     return counter


# O(n) complexity
def pair_sum(arr, target):
    if len(arr) < 2:
        return
    result = set()
    seen = set()
    for value in arr:
        k = target - value
        if k not in seen:
            seen.add(value)
        else:
            result.add((min(value, target), max(value, target)))
    return result



# To be optimized


def find_missing_value(arr1, arr2):
    counter = collections.defaultdict(int)
    for val in arr2:
        counter[val] += 1
    for val in arr1:
        if counter[val] == 0:
            return val
        else:
            counter[val] -= 1
    return


def large_cont_sum(arr):

    current_sum = max_sum = 0
    for num in arr:
        current_sum = max(current_sum, current_sum+num)
        max_sum = max_sum(max_sum, current_sum)
    return max_sum

