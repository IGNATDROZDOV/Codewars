def first_non_repeating_letter(string):
    if string:
        for i in list(dict.fromkeys(list(string))):
            if string.lower().count(i.lower()) == 1:
                return i
    return ''