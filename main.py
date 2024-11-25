users: list = [
    {'name': 'Żerom', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},

]
print (f'Witaj {users[0]['name']}!')
for user in users[1:]:
    print(f'Twój znajomy {user['name']} z miasta {user['city']} opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[0:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
