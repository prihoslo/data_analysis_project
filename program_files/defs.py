import re

def extract_pattern(text, pattern):
    """Извлекает часть строки по регулярному выражению"""
    match = re.search(pattern, text)
    return match

def cutter(text, cut):
    """отрезает начало по разделителю"""
    if type(text) != str:
        return text
    else:
        a = text.split(cut)[0]
        return a