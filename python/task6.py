def remove_short(names, min_len):
    names_copy = names.copy()
    # Remove elements from copy to continue iterating through original list as normal
    # .remove() shrinks the list so when an element is remove the next element takes its index so it is not iterated over again
    for n in names:              
        if len(n) < min_len:
            names_copy.remove(n)      
    return names_copy


if __name__ == "__main__":
    data = ["A", "B", "Cat", "Do"]
    print(remove_short(data, 2))
