class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.all.append(self)

    def contracts(self):
        return self.contracts_list

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        self.all.append(self)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.author.contracts_list.append(self)
        self.book.contracts_list.append(self)
        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
