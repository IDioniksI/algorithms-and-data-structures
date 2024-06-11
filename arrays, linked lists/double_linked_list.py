import time


class Item:
    def __init__(self, next_item=None, prev_item=None, elem=None):
        self.next_item = next_item
        self.prev_item = prev_item
        self.elem = elem


class DoubleLinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def insert_to_end(self, elem):
        if self.tail is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(None, self.tail, elem)
            self.tail.next_item = item
            self.tail = item
            self.length += 1

    def delete_from_end(self):
        if self.tail is None:
            print(f'{red}The list is empty{end}')
            pass
        else:
            self.tail = self.tail.prev_item
            if self.tail is not None:
                self.tail.next_item = None
            self.length -= 1

    def insert_at_middle(self, new_elem):
        index = self.length // 2
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")
        cur = self.head
        position = 0
        while position < index:
            cur = cur.next_item
            position += 1
        new_item = Item(cur, cur.prev_item, new_elem)
        if cur.prev_item is not None:
            cur.prev_item.next_item = new_item
        else:
            self.head = new_item
        cur.prev_item = new_item
        self.length += 1

    def delete_from_middle(self):
        index = self.length // 2
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")
        cur = self.head
        position = 0
        while position < index:
            cur = cur.next_item
            position += 1
        if cur.prev_item is not None:
            cur.prev_item.next_item = cur.next_item
        else:
            self.head = cur.next_item
        if cur.next_item is not None:
            cur.next_item.prev_item = cur.prev_item
        else:
            self.tail = cur.prev_item
        self.length -= 1

    def insert_to_begin(self, elem):
        if self.head is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(self.head, None, elem)
            self.head.prev_item = item
            self.head = self.head.prev_item
            self.length += 1

    def delete_from_begin(self):
        if self.head is None:
            print(f'{red}The list is empty{end}')
            pass
        else:
            self.head = self.head.next_item
            if self.head is not None:
                self.head.prev_item = None
            self.length -= 1

    def len(self):
        return self.length

    def contains(self, elem):
        if self.head is None:
            return False
        elif self.head.elem == elem:
            return True
        else:
            cur = self.head.next_item
            while cur is not None:
                if cur.elem == elem:
                    return True
                else:
                    cur = cur.next_item
            return False

    def delete_all_by_value(self, value):
        cur = self.head
        while cur is not None:
            if cur.elem == value:
                if cur == self.head:
                    self.head = cur.next_item
                else:
                    cur.prev_item.next_item = cur.next_item
                if cur == self.tail:
                    self.tail = cur.prev_item
                else:
                    cur.next_item.prev_item = cur.prev_item
                self.length -= 1
            cur = cur.next_item

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def display(self, title='Double linked list'):
        cur = self.head
        print(cyan, title, end)
        i = 0
        while cur is not None:
            print(str(i) + ": " + str(cur.elem))
            i += 1
            cur = cur.next_item
        print('-' * 30)

    def display_words_not_first_letter(self, title='Double linked list'):
        cur = self.head
        first_letters = double_link_words.first().elem[0]
        print(cyan, title, end)
        i = 0
        while cur is not None:
            if str(cur.elem)[0] == first_letters:
                cur = cur.next_item
            else:
                print(str(i) + ": " + str(cur.elem))
                i += 1
                cur = cur.next_item
        if i == 0:
            print('\nThere are no words that start with a different letter from the first word')
        print('-' * 30)

    def capitalize_all_words(self):
        cur = self.head
        while cur is not None:
            cur.elem = str(cur.elem.capitalize())
            cur = cur.next_item

    def display_reversed(self, title='Double linked list'):
        cur = self.head
        print(cyan, title, end)
        i = 0
        while cur is not None:
            print(str(i) + ": " + str(cur.elem)[::-1])
            i += 1
            cur = cur.next_item
        print('-' * 30)


cyan = '\033[36m'
red = '\033[31m'
purple = '\033[35m'
yellow = '\033[33m'
bold = '\033[1m'
end = '\033[0m'

double_link_words = DoubleLinkedList()

while True:
    text = str(input('\nWrite the text, the text must end with a period and contain lowercase letters,'
                     ' with at least one space between words: '))

    if text.islower() and text.endswith('.'):
        start = time.time()
        print(f'\n{cyan}Our initial text:{end}\n', text)

        text_finally = text.replace(",", "").replace(".", "").lower().split(" ")

        for word in text_finally:
            double_link_words.insert_to_end(word)

        double_link_words.display('Initial linked list')

        if double_link_words.len() == 0 or double_link_words.len() == 1:
            print(f'\n{red}Your text does not pass verification.\n'
                  f'You may be submitting an empty value or just one word{end}')
            continue

        first_letter = double_link_words.first().elem[0]
        # print(first_letter)

        if double_link_words.contains(''):
            double_link_words.delete_all_by_value('')
            double_link_words.display('\nA double linked list without empty values')

        double_link_words.display_words_not_first_letter('\nA double linked list of only words that begin with any'
                                                         ' letter other than the letter of the first word')

        double_link_words.capitalize_all_words()
        double_link_words.display('\nDouble linked list where all words are capitalized')

        double_link_words.display_reversed('\nDouble linked list where all words reversed')

        double_link_words.insert_at_middle('dogs')
        double_link_words.display('\nDouble linked list where the element "dog" was added inside')

        double_link_words.delete_from_middle()
        double_link_words.display('\nA double linked list where an element was removed from the middle')

        double_link_words.insert_to_begin('dogs')
        double_link_words.display('\nA double linked list where the element was added to the beginning')

        double_link_words.delete_from_begin()
        double_link_words.display('\nA double linked list where the element was deleted from the beginning')

        double_link_words.insert_to_end('dogs')
        double_link_words.display('\nA double linked list where an element was added to the end')

        double_link_words.delete_from_end()
        double_link_words.display('\nA double linked list where the element was removed from the end')

        double_link_empty = DoubleLinkedList()

        double_link_empty.display('\nEmpty double linked list')
        double_link_empty.delete_from_end()
        double_link_empty.delete_from_begin()

        end_time = (time.time() - start) * 1000
        print(f'\n{yellow}It took us {end_time} milliseconds{end}')
        break
    else:
        print(f'\n{red}Your text does not pass verification.\n'
              f'Check for yourself that all words are in lowercase letters and the text ends with a period'
              f'You may be submitting an empty value or just one word{end}')

print(f'\n{purple}{bold}Thank you!{end}')
