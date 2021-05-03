def num_translate(eng):
    nums = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восеиь',
            'nine': 'девять',
            'ten': 'десять'}
    return nums.get(eng)


print(num_translate('eleven'))
