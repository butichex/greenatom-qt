"""Какие ты видишь проблемы в следующем коде? 
Как его следует исправить? 
Исправь ошибку и перепиши код с использованием типизации"""


"""Проблема в том, что все lambda-функции, 
добавленные в список handlers, ссылаются на одну и ту же 
переменную step. Поэтому когда запускается execute_handlers, 
вызывается последнее значение step (в данном случае 4).

Чтобы исправить эту ошибку, 
мы можем объявить параметр 's' в lambda-функции, 
в которую передадим аргумент 'step', 
чтобы значение 'step', переданное в lambda-функцию всегда соответствовало значению step в цикле for"""


from typing import Callable, List


def create_handlers(callback: Callable):
    handlers = []
    for step in range(5):
        handlers.append(lambda s=step: callback(s)) # h̶a̶n̶d̶l̶e̶r̶s̶.̶a̶p̶p̶e̶n̶d̶(̶l̶a̶m̶b̶d̶a̶:̶ ̶c̶a̶l̶l̶b̶a̶c̶k̶(̶s̶t̶e̶p̶)̶)̶
    return handlers


def execute_handlers(handlers: List[Callable]):
    for handler in handlers:
        handler()


def print_step(step: int):
    print("Step:", step)


handlers = create_handlers(print_step)
execute_handlers(handlers)
