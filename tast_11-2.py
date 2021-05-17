class UserDivZeroError(Exception):
    def __init__(self, message):
        self.message = message


def main():
    while True:
        dividend = input('Введите делимое или "q" для выхода:')
        if dividend == 'q':
            break
        divisor = input('Введите делитель или "q" для выхода:')
        if divisor == 'q':
            break
        try:
            if float(divisor) == 0:
                raise UserDivZeroError('На ноль делить нельзя!')
            else:
                print(f'Частное: {float(dividend) / float(divisor):.2f}')
        except UserDivZeroError as ex:
            print(ex)
        except ValueError as ex:
            print(ex)


if __name__ == '__main__':
    main()
