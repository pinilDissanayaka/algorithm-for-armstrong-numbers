def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def is_armstrong(num):
    num_digits = count_digits(num)
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    return armstrong_sum == num

def find_armstrong_numbers():
    armstrong_numbers = []
    for i in range(100001):
        if is_armstrong(i):
            armstrong_numbers.append(i)
    return armstrong_numbers

if __name__ == "__main__":
    armstrong_numbers = find_armstrong_numbers()
    print("Armstrong numbers within the range of 0 to 100,000:")
    print(armstrong_numbers)