# Raad Barnett 1231583
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_smallest]:
                index_smallest = j
    
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        for n in numbers:
            print(n,end=' ')
        print()
numbers = input().split()
numbers = [int(x) for x in numbers]
selection_sort_descend_trace(numbers)
