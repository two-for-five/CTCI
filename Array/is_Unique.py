#ASCII or Unicode
import unittest

def is_unique(string):
    """
    Find out if a string is unique, and try not to use any data structures.
    :param string: str
    :return: boolean
    """
    # assume only ASCII
    if len(string) > 128:
        return False
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

    if len(string) > 128:
        return False
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                return False
    return True

#time_complexity = O(N^2)
#space_complexity = (O(1))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()