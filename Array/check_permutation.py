#space and case sensitive
import unittest
def check_permutation(str1, str2):
    """
    Check if str1 is permutation of str2
    :param str1:
    :param str2:
    :return: boolean
    """
    if len(str1) != len(str2):
        return False
    dictionary = {}
    for i in range(len(str2)):
        if str2[i] not in dictionary:
            dictionary[str2[i]] = 1
        else:
            dictionary[str2[i]] += 1
    for i in range(len(str1)):
        if str1[i] not in dictionary:
            return False
        else:
            dictionary[str1[i]] -= 1
            if dictionary[str1[i]] == 0:
                del dictionary[str1[i]]
    if dictionary:
        return False
    return True

#time complexity(M + N)
#space complexity(N)

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )
    def test(self):
        for str1, str2 in self.dataT:
            actual = check_permutation(str1, str2)
            self.assertTrue(actual)
        for str1, str2 in self.dataF:
            actual = check_permutation(str1, str2)
            self.assertFalse(actual)

if __name__ =="__main__":
    unittest.main()
