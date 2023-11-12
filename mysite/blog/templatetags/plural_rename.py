from django import template

register = template.Library()


@register.filter
def ru_plural(value: int, variants: str) -> str:
    """Тег для отображения числа в правильном множественном виде"""

    variants = variants.split(",")
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return f"{value} {variants[variant]}"
