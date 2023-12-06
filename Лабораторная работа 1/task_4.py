users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

users_dct = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}


unique_u = len(set(users))
number_u = len(users)

users_dct["Общее количество"] = number_u
users_dct["Уникальные посещения"] = unique_u

print(users_dct)
