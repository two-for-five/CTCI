#find out if a string is unique, and try not to use any data structures.

#ASCII or Unicode
def is_unique(string):
    """
    :param string: str
    :return: boolean
    """
    hashset = set()
    for i in range(len(string)):
        if string[i] not in hashset:
            hashset.add(string[i])
        else:
            return False
    return True

#time_complexity = O(N)
#space_complexity = (O(N))

def is_unique_without_memory(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return False
    return True

#time_complexity = O(N^2)
#space_complexity = (O(1))

print(is_unique("abcd"))
print(is_unique("aa"))

print(is_unique_without_memory("abcd"))
print(is_unique_without_memory("aa"))