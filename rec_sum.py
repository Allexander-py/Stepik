n, k = map(int, input().split())


def rec_sum(amount_of_elements: int, combination: int):
    """Функиця выводит количество комбинаций из количества комбинаций (amount_of_elements)
       и количества элеементов для комбинаций(combination) """
    if amount_of_elements < combination:
        return 0
    elif combination == 0:
        return 1
    else:
        return rec_sum(amount_of_elements - 1, combination) + rec_sum(amount_of_elements - 1, combination - 1)


print(rec_sum(n, k))
