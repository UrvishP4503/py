def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def selection_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        if i != minimum:
            arr[i], arr[minimum] = arr[minimum], arr[i]


def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        is_sorting = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorting = True
        if not is_sorting:
            break


# arr1 = [45, 23, 67, 12, 89, 34, 56, 90, 78, 9, 32, 76, 21, 54, 87]
arr2 = [65, 43, 87, 10, 56, 29, 76, 98, 54, 21, 43, 67, 89, 32, 12]
arr1 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr2 = [34, 12, 56, 78, 23, 45, 89, 67, 21, 43, 87, 10, 54, 32, 98]


print(f'Before sorting : {arr1}')
# insertion_sort(arr1)
# selection_sort(arr1)
bubble_sort(arr1)
print(f'After sorting : {arr1}\n')

print(f'Before sorting : {arr2}')
# insertion_sort(arr2)
# selection_sort(arr2)
bubble_sort(arr2)
print(f'After sorting : {arr2}')
