import unittest

from day3_pt2_new import main, parse_grid_from_file


class Day3(unittest.TestCase):
    def test_file1(self):
        grid = parse_grid_from_file('./inputs/day3.txt')
        self.assertEqual(main(grid), 6756)

    def test_file2(self):
        grid = parse_grid_from_file('./inputs/day3-1.txt')        
        self.assertEqual(main(grid), 467835)
        
if __name__ == '__main__':
    unittest.main()