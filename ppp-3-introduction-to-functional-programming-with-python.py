

def flatten_dict(dictionary):
    flattened = dict()

    for key in dictionary.keys():
        if type(dictionary[key]) == dict:
            for k, v in dictionary[key].items():
                new_key = key + "." + k
                flattened[new_key] = v
        else:
            flattened[key] = dictionary[key]

    return flattened


print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))


def unflatten_dict(dictionary):
    unflattened = dict()

    iterator = iter(dictionary.items())

    while (True):
        current = next(iterator, "end")

        if current == "end":
            break

        current_key = current[0]

        if current_key.find(".") != -1:
            key, sub_key = current_key.split(".")

            if not key in unflattened:
                unflattened[key] = dict()

            unflattened[key][sub_key] = dictionary[current_key]
        else:
            unflattened[current_key] = dictionary[current_key]

    return unflattened


print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))  #  {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}


def treemap(map_function, the_list):
    new_list = []

    for item in the_list:
        if type(item) == list:
            new_list.append(treemap(map_function, item))
        else:
            new_list.append(map_function(item))
    return new_list


print(treemap(lambda x: x*x, [2, 4, 5, 8, [9, 19]]))  #  [4, 16, 25, 64, [81, 361]]
print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]], [1, 4, [9, 16, [25]]]]))  #  [1, 4, [9, 16, [25]], [1, 16, [81, 256, [625]]]]
