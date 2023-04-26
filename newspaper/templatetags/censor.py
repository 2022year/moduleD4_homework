from django import template


register = template.Library()

@register.filter(name='censor')
def censor(value, arg):
    cList = ['дур', 'коз']
    cEdit = value
    result = ''

    for w in cList:
        cTemp = cEdit.lower().replace(w, arg * len(w))
        cEdit = cTemp

    for i in range(0, len(value)):
        if (value[i] != cEdit[i]):
            result += cEdit[i].upper()
        else:
            result += cEdit[i]

    return result
