

class No:
    def __init__(self, v):
        self.value = v
        self.next = None


class ListaEncadenada:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, v):
        no = No(v)
        no.next = self.head
        self.head = no
        self.tail = no

    def append(self, v):
        final = self.tail
        no = No(v)
        final = no
        tail = no

    def tail(self):
        if self.head is None:
            return None

        iter = self.head
        while iter.next is not None:
            iter = iter.next
        return iter
