TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = (
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
)

def find_where(books, query):
    result = {}
    for i in books:
        if set(i.items()) & set(query.items()) == set(query.items()):
            return i
    return None
        


find_where(
        BOOKS, {YEAR: 4444},
    ) #{TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}
find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )#[TITLE] == 'Cymbeline'
