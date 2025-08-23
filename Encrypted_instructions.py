# ID - 141465541.
def decode(command: str) -> str:
    """Функция принимает на вход зашифрованную команду с Земли. И после
    каждого пройденого цикла рекурсивной функции возвращает результат """
    def decode_recursive(command, index=0):
        """Вспомогательная функция, её задача разшифровать данные.
        После завершения чтения команды, возвращает result в основную
        функцию, та в свою очередь выводится на печать."""
        result = ''
        while index < len(command):

            if command[index].isdigit():
                num = 0

                while index < len(command) and command[index].isdigit():
                    num = num * 10 + int(command[index])
                    index += 1

                index += 1
                decode_str, index = decode_recursive(command, index)
                index += 1
                result += decode_str * num

            elif command[index].isalpha():
                result += command[index]
                index += 1

            elif command[index] == ']':
                return result, index

        return result, index
    return decode_recursive(command)[0]


if __name__ == '__main__':
    """Здесь выполняется ввод команды в зашифрованном виде,
    а выводится в разшифрованном."""
    command = input()
    print(decode(command))
