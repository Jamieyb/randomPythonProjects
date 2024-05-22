#ROT13 mechanism (right shift 13)

def rot13(message):
    order = 'abcdefghijklmnopqrstuvwxyz'
    idx = []
    for i in message:
        if order.find(i)>-1 and order.find(i)+13<26:
            idx.append(order[order.find(i)+13])
        elif order.find(i)>-1 and order.find(i)+13>26:
            idx.append(order[order.find(i)+13-26])
        elif i.isupper() and order.find(i.lower())+13<26:
            idx.append(order[order.find(i.lower())+13].upper())
        elif i.isupper() and order.find(i.lower())+13>26:
            idx.append(order[order.find(i.lower())+13-26].upper())
        else:
            idx.append(i)


    return ''.join(idx)

#print(rot13('what'))
print('cwybfeckwuvybcku4v'.find('I'))
