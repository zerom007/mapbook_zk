from mapbook.users import users
from mapbook.crud import hello, read_users, add_user, remove_user, update_user


def main():
    hello(users[0]['name'])
    read_users(users)
    # add_user(users)
    # remove_user(users)
    update_user(users)
    read_users(users)


while True:
    print("======MENU=====")
    print("1. Dodaj Znajomego")
    print("2. Wczytaj Znajomego")
    print("3. Aktualoizuj Znajomego")
    print("4. Usuń Znajomego")
    print("5. Generuj mapę z lokalizacją znajomego")
    print("6. Generuj mapę z lokalizacją wszystkoch znajomych")


    menu_option: str=input("Użytkowniku wybierz opcję menu: ")
    print(f'Użytkownik wybrał {menu_option}')
    if menu_option == '1':
        add_user(users)
    if menu_option == '2':
        read_users(users)
    if menu_option == '3':
        update_user(users)
    if menu_option == '4':
      remove_user(users)
    if menu_option == '5':
      pass
    if menu_option == '6':
      pass

if __name__=='__main__':
    main()



