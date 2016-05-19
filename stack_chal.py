link =(
 'http://stackoverflow.com/questions/37306771/python-find-distance-between-identical-elements-within-a-list')

'''Say I have a list such as [a, b, c, c, b, a, b, c, a].

What function will return [-, -, -, 1, 3, 5, 2, 4, 3]?

[Note that I only need distance to (most proximal) previous occurrence, hence the initial dashes in the output]

Thanks much!

-AY'''
original_list = ['a', 'b', 'c', 'c', 'b', 'a', 'b', 'c', 'a']
first_val = '-'

def distance_list(original_list, first_val):
    last_occurence = {}
    distances = []

    for pos, elem in enumerate(original_list):
        if elem in last_occurence:
            distances.append(pos - last_occurence[elem])
        else:
            distances.append(first_val)
        last_occurence[elem] = pos
        import ipdb; ipdb.set_trace()
    print distances
    return distances
distance_list(original_list,first_val)
