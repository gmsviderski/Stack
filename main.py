### Реализация стека
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        print("Текущий стек:", self.items)

    def push(self, item):
        self.items.append(item)
        self.print_stack()  # Вывод состояния стека после добавления нового элемента

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стек пуст!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стек пуст!"

### Реализация очереди
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Очередь пуста!"

    def size(self):
        return len(self.items)



# Пример использования стека
stack = Stack()
print("Пример использования стека")
print(f'Проверка стека на пустоту: {stack.is_empty()}')  # True

print(f'Добавление нового значения: 1 ')
stack.push(1)
print(f'Добавление нового значения: 2 ')
stack.push(2)
print(f'Добавление нового значения: 3 ')
stack.push(3)

print(f'Проверка стека на пустоту: {stack.is_empty()}')  # False
print(stack.peek())      # 3
print(stack.pop())       # 3
print(stack.peek())      # 2


# Пример использования очереди
queue = Queue()
print ('Пример использования очереди')
print(f'Проверка очереди на пустоту: {queue.is_empty()}')  # True
print(f'Размер очереди: {queue.size()}')

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(f'Проверка очереди на пустоту: {queue.is_empty()}')  # False
print(f'Размер очереди: {queue.size()}')      # 4
print(f'Извлениение из очереди: {queue.dequeue()}')    # "действие 1"
print(f'Размер очереди: {queue.size()}')      # 3
