from math import floor, ceil

def read_numbers():
    file_name = "Data/day18.txt"
    file = open(file_name, "r")
    numbers = []

    for line in file:
        numbers.append(line.strip("\n"))

    return numbers

def magnitude(number):
    if type(number) == int:
        return number

    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def largest_sum(numbers):
    largest = 0

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            number = "[" + str(numbers[i]) + "," + str(numbers[j]) + "]"
            number = reduce(number)
            largest = max(largest, magnitude(eval(number)))

            number = "[" + str(numbers[j]) + "," + str(numbers[i]) + "]"
            number = reduce(number)
            largest = max(largest, magnitude(eval(number)))

    print(f"Part two: {largest}")

def add(numbers):
    number = numbers[0]

    for i in range(1, len(numbers)):
        number = "[" + number + "," + str(numbers[i]) + "]"
        number = reduce(number)

    print(f"Part one: {magnitude(eval(number))}")

def reduce(number):
    while True:
        new_number = explode(number)

        if new_number != number:
            number = new_number
            continue

        new_number = split_nums(new_number)

        if new_number == number:
            return new_number

        number = new_number

def split_nums(number):
    for pos, char in enumerate(number):
        if number[pos] not in ("[", "]", ",") and number[pos + 1] not in ("[", "]", ","):
            end = pos + 1
            while number[end] not in ("[", "]", ","):
                end += 1

            n = int(number[pos:end])
            return number[:pos] + "[" + str(floor(n/2)) + "," + str(ceil(n/2)) + "]" + number[end:]

    return number

def explode(number):
    depth = 0
    
    for pos, char in enumerate(number):
        if char == "[":
            depth += 1

            if depth == 5:
                end = pos + 1
                while number[end] != "]":
                    end += 1

                nums = list(map(int, number[pos + 1:end].split(",")))
                left_num = find_left_number(number, pos)
                right_num = find_right_number(number, end)

                if right_num[0] != 0:
                    number = number[:right_num[0]] + str(nums[1] + right_num[2]) + number[right_num[1]:]

                number = number[:pos] + "0" + number[end + 1:]

                if left_num[0] != 0:
                    number = number[:left_num[0]] + str(nums[0] + left_num[2]) + number[left_num[1]:]

                return number

        elif char == "]":
            depth -= 1

    return number

def find_left_number(number, pos):
    end = pos - 1
    while number[end] in ("[", "]", ","):
        end -= 1

    if end < 0:
        return 0, 0

    start = end - 1
    while number[start] not in ("[", "]", ","):
        start -= 1

    return start + 1, end + 1, int(number[start + 1:end + 1])

def find_right_number(number, pos):
    start = pos + 1
    while number[start] in ("[", "]", ","):
        start += 1
        if start == len(number):
            return 0, 0

    end = start + 1
    while number[end] not in ("[", "]", ","):
        end += 1

    return start, end, int(number[start:end])

if __name__ == "__main__":
    numbers = read_numbers()
    add(numbers)
    largest_sum(numbers)
