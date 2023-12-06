list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_p = len(list_players)
half_p = num_p // 2
ft = list_players[:half_p]
st = list_players[half_p:]

print(f"{ft}\n{st}")
