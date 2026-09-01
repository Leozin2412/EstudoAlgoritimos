def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        menores=[i for i in array[1:] if i<= pivot]
        maiores=[i for i in array[1:] if i> pivot]

        return quicksort(menores) + [pivot] + quicksort(maiores)



print(quicksort([5,4,3,2,1]))
