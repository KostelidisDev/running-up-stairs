def calculate(stairs: int) -> int:
    if stairs == 0:
        return 0
    if stairs == 1 or stairs == 2:
        return 1

    previous_min_1 = 0
    previous_min_2 = 1

    current = previous_min_1 + previous_min_2

    for i in range(3, stairs + 1):
        previous_min_1 = previous_min_2
        previous_min_2 = current
        current = previous_min_1 + previous_min_2

    return current

def main():
    for test_case in range(int(input())):
        print(calculate(int(input())+1))

if __name__ == '__main__':
    main()