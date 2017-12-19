
# O(N)
import unittest

def string_compression(string):
    
    i = 0
    j = 1
    res = ""
    while j < len(string):
        if string[i] == string[j]:
            j += 1
        else:
            res += (string[i] + str(j - i))
            i = j
            j = j + 1

    res += (string[i] + str(j - i))
    return res if len(res) < len(string) else string


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()