from client import Client
from books import Books


class Bookstore:
    client_list = []
    book_list = []
    operation_history = []

    def __init__(self):
        self.main()


    def print_menu(self):
        print('wybierz opcje: ')
        print(10 * '*')
        print('1. Załóż konto klienta')
        print('2. Pokaż konta klientów')
        print('3. Sprawdź ile klient zakupił książek i czy otrzyma gratis')
        print('4. Ustaw listę dostępnych książek')
        print('5. Ustaw stany magazynowe książki')
        print('6. Pokaż listę książek')
        print('7. Sprzedaj książki klientowi i pokaż kwotę do zapłaty po uwzględnieniu promocji')
        print('0. Wyjdź z programu')

        # pokaz liste dostepnych ksiazek
        # print('8. Zareklamuj książkę i zwróć pieniądze klientowi')
        # print('11. Sprawdź czy klienta obowiązuje promocja "Senior')

    def set_client_account(self):
        name = input('Podaj imie klienta: ')
        surname = input('Podaj nazwisko: ')
        age = int(input('Podaj wiek: '))
        client = Client(name, surname, age)
        Bookstore.client_list.append(client)


    def show_client_accounts(self):
        for client in Bookstore.client_list:
            print(vars(client))


    def bought_books(self):
        def check_if_account_exists(client_id):
            for bookstore_client in Bookstore.client_list:
                if bookstore_client.id == client_id:
                    return bookstore_client
                else:
                    continue
            return False

        client_id = int(input('podaj id klienta: '))
        client = check_if_account_exists(client_id)
        if client:
            print(f'klient zakupił {client.num_of_books} książek')
            if client.num_of_books >= 10:
                print('klient otrzymuje gratis')
            else:
                print('klient nie otrzymuje gratisu')
        else:
            print('wybrane konto nie istnieje')


    def set_books(self):
        title = input('Podaj tytuł książki: ')
        author_name = input('Podaj nazwisko autora: ')
        publication_year = int(input('Podaj rok publikacji: '))
        price = int(input('Podaj cenę książki: '))
        book = Books(title, author_name, price, publication_year)
        Bookstore.book_list.append(book)
        print(vars(book))


    def set_stock_levels_of_books(self):
        def check_if_book_exists(book_id):
            for bookstore_book in Bookstore.book_list:
                if bookstore_book.id == book_id:
                    return bookstore_book
                else:
                    continue
            return False

        book_id = int(input('podaj id książki do ustawienia stanu magazynowego: '))
        book = check_if_book_exists(book_id)
        if book:
            new_num_of_copies = int(input('podaj ilość stanu magazynowego '))
            book.set_num_of_copies(new_num_of_copies)
            print(f'Dla ksiazki {book.title} mamy dostępnych {book.num_of_copies} egzemplarzy')
            print(vars(book))
        else:
            print('wybrana książka nie istnieje')

    def show_books(self):
        for element in Bookstore.book_list:
            print(vars(element))


    def sell_book(self):
        def check_if_book_exists(book_id):
            for bookstore_book in Bookstore.book_list:
                if bookstore_book.id == book_id:
                    return bookstore_book
                else:
                    continue
            return False

        def check_if_account_exists(client_id):
            for bookstore_client in Bookstore.client_list:
                if bookstore_client.id == client_id:
                    return bookstore_client
                else:
                    continue
            return False

        book_id = int(input('podaj id książki, którą chce kupić klient: '))
        book = check_if_book_exists(book_id)
        if book:
            new_num_of_copies = int(input('podaj ile egzemplarzy klient chce kupić: '))
            if book.num_of_copies >= new_num_of_copies:
                print(f'książka dostępna w cenie {book.price}')

                client_id = int(input('podaj id klienta, który chce kupić książkę: '))
                client = check_if_account_exists(client_id)

                if client:
                    client.num_of_books += new_num_of_copies
                    book.num_of_copies -= new_num_of_copies

                    print(f'książka sprzedana, klient ma {client.num_of_books} zakupionych książek.')
                    pay_amount = book.price * new_num_of_copies
                    if pay_amount <= 100:
                        print(f'klient ma do zapłaty {pay_amount} zl.')
                    else:
                        pay_amount *= 0.9
                        print(f'klient uzyskał 10% rabatu, ma do zapłaty {pay_amount}.')
                else:
                    print('konto klienta nie istnieje')

            else:
              print(f'książka niedostępna, mamy jedynie {book.num_of_copies} egzemplarzy')
        else:
            print('wybrana książka nie istnieje')

    def main(self):
        while True:
            self.print_menu()
            option = input('podaj opcje: ')
            if option == '1':
                self.set_client_account()
                input('nacisnij enter, aby wrocic do głównego menu ')
            elif option == '2':
                self.show_client_accounts()
                input('nacisnij enter, aby wrocic do głównego menu ')
            elif option == '3':
                self.bought_books()
                input('nacisnij enter, aby wrocic do głównego menu ')
            elif option == '4':
                self.set_books()
                input('nacisnij enter, aby wrocic do głównego menu ')
            elif option == '5':
                self.set_stock_levels_of_books()
                input('nacisnij enter, aby wrocic do głównego menu ')
            elif option == '6':
                self.show_books()
            elif option == '7':
                self.sell_book()
            elif option == '0':
                break


Bookstore()
