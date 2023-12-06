numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

def rep_average(numbers_list):
    i = numbers.index(None) #Ищем индекс пустого значения
    average = (sum(numbers_list[:i]) + sum(numbers_list[i + 1:])) / len(numbers_list) #Выполняем расчет
    numbers_list[i] = average #Перезаписываем значение по найденному ранее индексу
    return numbers_list

print(f"Измененный список: {rep_average(numbers)}")