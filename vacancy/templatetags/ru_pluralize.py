from typing import Union

from django import template


register = template.Library()


@register.filter()
def ru_pluralize(number: Union[int, str], arg: str = 'вакансия, вакансии, вакансий'):
    nominative_signular, genitive_signular, genitive_plural = arg.split(',')
    number = abs(int(number))
    if 10 <= number <= 20 or (number % 10 in [5, 6, 7, 8, 9, 0]):
        return f'{number} {genitive_plural}'
    if number == 1:
        return f'{number} {nominative_signular}'
    if number % 10 in [2, 3, 4]:
        return f'{number} {genitive_signular}'
