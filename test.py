class tst:
    def __init__(self):
        "constructor to initiate this object"
        
        self.head = None
        self.tail = None
        return

    def abc(self):
        self.head = "Head"
        self.tail = "Tail"
        self.tail.next = "Tail Next"

        print(self.head)
        print(self.tail)
        print(self.tail.next)

x = tst()

x.abc()