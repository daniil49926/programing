import sys


def create_list(length, start, step):
    num_list = [start + (step * i) for i in range(length) if i < length]
    return num_list


def sort(num_list):
    for i in range(1, len(num_list)):
        count = num_list[i]
        j = i - 1
        while j >= 0 and count < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = count
    return num_list


def like_print(*args, sep=' ', end='\n', file=sys.stdout):   # Называть функцию "print" - это уже неуважение к pep8,
    file.write(sep.join(map(str, args)))                     # поэтому будет like_print
    file.write(end)


def main():
    length_list = int(input("Введите длину: "))
    start_point = int(input("Введите начальную точку: "))
    step = int(input("Введите шаг: "))
    like_print(sort(create_list(length_list, start_point, step)))


main()
