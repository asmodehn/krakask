
def dosmthg():

    Monoid().this().that().thisagain()

    "<=>"

    m = Monoid()
    m.this()
    m.that()
    m.this()

    "AND"

    with Monoid() as m:

        m.this()
        m.that()
        m.this()

    "<=>"

    async with Monoid() as m:
        m.this().that().this()






class NoopApi(metaclass=AsyncApi):
    """

    """

    def __init__(self):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()