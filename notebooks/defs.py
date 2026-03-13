import re

def extract_pattern(text, pattern):
    """Извлекает часть строки по регулярному выражению"""
    match = re.search(pattern, text)
    if match:
        return match.group() 
    return None

def cutter(text, cut, index_start = 0, index_end = 1):
    """отрезает начало по разделителю"""
    if type(text) != str:
        return text
    else:
        try:
            a = ''.join(text.split(cut)[index_start:index_end])
            return a
        except:
            return None
    
def re_money(a:str):
    a = a.split(' ')
    if a[-1]=='$':
        return float(a[0])*80
    elif a[-1]=='€':
        return float(a[0])*91
    else:
        return float(a[0])