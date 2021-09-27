class Books:
    next_number = 1

    def __init__(self, title, author_name, publication_year, price, num_of_copies=0):
        self.id = self.next_number
        self.title = title
        self.author_name = author_name
        self.publication_year = publication_year
        self.price = price
        self.num_of_copies = num_of_copies
        Books.next_number += 1

    def set_num_of_copies(self, new_num_of_copies):
        if isinstance(new_num_of_copies, (int, float)):
            self.num_of_copies = new_num_of_copies
        else:
            print('nowy balans musi byc intem')