all = [{'length': 8, 'tag': '<strong>', 'offset': 7}, {'length': 9, 'tag': '</strong>', 'offset': 25}, {'length': 4, 'tag': '<em>', 'offset': 7}]

def modify(all):
    rev = reversed(all)
    for i in rev:
        for i2 in rev:
            import ipdb; ipdb.set_trace()
            if i == i2:
                continue
            elif (i2['offset'] >= i['offset']):
                i2['offset'] += i['length']
        break
    print all

modify(all)
