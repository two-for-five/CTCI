
import unittest
def palindrome_permutation(string):
    """
    check if a string has a permutation which is a palindrome
    :param string:
    :return: boolean
    """
    string = string.lower()
    dictionary = {}
    for i in range(len(string)):
        if string[i] != " ":
            if string[i] not in dictionary:
                dictionary[string[i]] = 1
            else:
                dictionary[string[i]] += 1
    odd_char = 0
    for key in dictionary:
        if dictionary[key] % 2 != 0:
            odd_char += 1
            if odd_char > 1:
                return False
    return True

#time complexity = O(N)
class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    def test(self):
        for string, expected in self.data:
            actual = palindrome_permutation(string)
            self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()
