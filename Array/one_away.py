import unittest


def one_away(str1, str2):
    """
    3 operations: add, remove, and replace to check if its one edit or zero edit from str1 to str2
    :param str1:
    :param str2:
    :return: boolean
    """
    if len(str1) == len(str2):
        return replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return insert(str2, str1)
    return False

def replace(str1, str2):
    edit = False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if edit:
                return False
            edit = True
    return True

def insert(str1, str2):
    i = j = 0
    edit = False
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edit:
                return False
            edit = True
            j += 1
        else:
            i += 1
            j += 1
    return True




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
