class Client:
    next_number = 1

    def __init__(self, name, surname, age, num_of_books=0):
        self.id = self.next_number
        self.name = name
        self.surname = surname
        self.age = age
        self.num_of_books = num_of_books
        Client.next_number += 1