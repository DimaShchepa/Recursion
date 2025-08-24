# ID - 141490654.
from string import digits
DIGITS_SET = set(digits)

OPEN_BRACKET = '['
CLOSE_BRACKET = ']'


def decode(command: str) -> str:
    """Функция принимает на вход зашифрованную команду с Земли. И после
    каждого пройденого цикла рекурсивной функции возвращает результат """
    def decode_recursive(index: int = 0) -> tuple[str, int]:
        """Вспомогательная функция, её задача - разшифровать данные.
        После завершения чтения команды, возвращает result в основную
        функцию, та в свою очередь выводится на печать."""
        result = ''
        num = 0

        while index < len(command):
            char = command[index]

            if char in DIGITS_SET:

                num = num * 10 + int(char)
                index += 1

            elif char == OPEN_BRACKET:

                decode_str, index = decode_recursive(index + 1)
                index + 1
                result += decode_str * num
                num = 0

            elif char == CLOSE_BRACKET:
                return result, index + 1

            else:
                result += char
                index += 1

        return result, index
    return decode_recursive()[0]


if __name__ == '__main__':
    """Здесь выполняется ввод команды в зашифрованном виде,
    а выводится в разшифрованном."""
    print(decode(input()))
