import unittest

from iching import cast, changed, draw


class ReadingTests(unittest.TestCase):
    def test_coin_extremes_and_line_order(self):
        bits = iter([0, 0, 0, 1, 1, 1] * 3)
        lines = cast(lambda _: next(bits))
        self.assertEqual(lines, (6, 9, 6, 9, 6, 9))
        self.assertEqual(changed(lines), (7, 8, 7, 8, 7, 8))
        self.assertEqual(draw(lines).splitlines()[0], "--------- *")


if __name__ == "__main__":
    unittest.main()
