prod = 1
contor = 0
while True:
    n = int(input("Zahl:"))
    if n == 0:
        break
    prod *= n
while prod != 0:
    letzte_ziffer = prod % 10
    if letzte_ziffer == 0:
            contor += 1
    prod /= 10
print(contor)



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_longest_prime_sum_subsequence(arr):
    max_length = 0
    start_index = 0

    for i in range(len(arr)):
        current_sum = arr[i]
        current_length = 1

        for j in range(i + 1, len(arr)):
            current_sum += arr[j]
            current_length += 1

            if is_prime(current_sum) and current_length > max_length:
                max_length = current_length
                start_index = i

    if max_length > 1:
        return arr[start_index : start_index + max_length]
    else:
        return []

# Beispiel-Vektor
vector = [1, 2, 3, 5, 4, 7, 11, 10, 9]
result = find_longest_prime_sum_subsequence(vector)
print(result)