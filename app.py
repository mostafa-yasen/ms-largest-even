from typing import List

def solution(A: List[int], K: int) -> int:
    if K > len(A):
        return -1

    total = 0

    even_numbers = []
    odd_numbers = []

    # even_numbers = list(filter(lambda x: x % 2 == 0, A))
    # odd_numbers = list(filter(lambda x: x % 2 == 1, A))

    for num in A:
        if num % 2:
            odd_numbers.append(num)
        else:
            even_numbers.append(num)

    odd_numbers.sort(reverse=False)
    even_numbers.sort(reverse=False)

    j = len(odd_numbers) - 1
    i = len(even_numbers) - 1

    while K > 0:
        if K % 2:

            if i >= 0:
                total += even_numbers[i]
                i -= 1

            else:
                return -1

            K -= 1

        elif i >= 1 and j >= 1:
            
            if even_numbers[i] + even_numbers[i-1] <= odd_numbers[j] + odd_numbers[j-1]:
                total += odd_numbers[j] + odd_numbers[j-1]
                j -= 2
            else:
                total += even_numbers[i] + even_numbers[i-1]
                i -= 2

            K -= 2

        elif i >= 1:
            total += even_numbers[i] + even_numbers[i-1]
            i -= 2
            K -= 2
        
        elif j >= 1:
            total += odd_numbers[j] + odd_numbers[j-1]
            j -= 2
            K -= 2

    return total
