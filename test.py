import unittest



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()


def test_distance():
    result = pretendProductionCode.simple_distance
    assert result == 5


def test_show_output():
    with open("test.txt", "w") as test:
        pretendProductionCode.testable_show_output(1000, .1, test)
    test_file = open("test.txt")
    everything = test_file.readlines()
    str_everything = str(everything)
    assert '1100' in str_everything


def test_interests():
    with pytest.raises(TypeError):
        pretendProductionCode.add_interest("too much Money", .1)

