def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

while True:
    user_input = input("Enter numbers separated by spaces (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        arr = list(map(int, user_input.split()))
        sorted_arr = bubble_sort(arr)
        print("Sorted array:", sorted_arr)
    except ValueError:
        print("Please enter valid integers.")