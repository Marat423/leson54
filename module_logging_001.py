# Импорт модуля логирования для записи событий
import logging
    # Базовый класс для пользовательских исключений, связанных с числами
class NumbersError(Exception):
    pass
    # Специализированное исключение для отрицательных чисел
class NegativeError(NumbersError):
    pass
    # Проверка на неотрицательное число
def negative_number(a):
    if a >= 0:
        return True
    # Выбрасываем кастомное исключение с сообщением
    raise NegativeError("You can't take the root of a negative number")
    # Функция вычисления квадратного корня с обработкой ошибок
def sqrt(a):

    try:
        # Проверка валидности числа перед вычислением
        if negative_number(a):
            # Логирование успешной операции
            logging.info(f'Successful square root {a} ** 0.5')
        return a ** 0.5
        # Обработка кастомных исключений
    except NumbersError as e:  # обращение к исключению как к объекту
        # Логирование ошибки с полной информацией об исключении
        logging.error('Negative number', exc_info=True)
        print(f"You can't take the root of a negative number: {e}.")
        # Общий обработчик непредвиденных ошибок
    except Exception as e:
        print(f'An unexpected error occurred: {e}.')
    #except ArithmeticError:
        #logging.error('Корень нельзя извлечь из отрицательного числа', exc_info=True)

    # Точка входа в программу
if __name__ == '__main__':
    # Настройка логирования:
    # - уровень INFO
    # - режим перезаписи файла (filemode='w')
    # - вывод в файл py.log
    # - формат записи: время | уровень | сообщение
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    print(sqrt(4))
    print(sqrt(16))
    print(sqrt(-20))
    print(sqrt('a'))
