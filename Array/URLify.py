import unittest


def URLify(string):
    """
    replace every space to %20
    :param string:
    :return: new_string
    """
    string = string.strip()
    string = string.split(" ")
    return "%20".join(string)


class Test(unittest.TestCase):
    data = [
        ('much ado about nothing      ',
         'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 'Mr%20John%20Smith')]

    def test(self):
        for old_str, expected in self.data:
            actual = URLify(old_str)
            self.assertEqual(actual, expected)


if __name__ == "main":
    unittest.main()
