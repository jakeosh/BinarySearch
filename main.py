list = [11, 22, 33, 44, 55, 66]
number = int(input("Enter your number: "))


def search(list, number):
    low = 0
    high = len(list) - 1
    position = 0

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == number:
            position = mid

            print("NUMBER FOUND AT", position + 1)

            break

        else:
            if list[mid] < number:
                low = mid
            else:
                high = mid


search(list, number)
