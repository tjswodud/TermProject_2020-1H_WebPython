import unittest

from termProject import TermProject
from recommend import Recommend

class TermProjectTest(unittest.TestCase):
    def test_eng_and_kor(self):
        term = TermProject()
        reco = Recommend()
        term.search('마우스')
        result_1 = reco.titleList
        reco.titleList.clear()
        term.search('mouse')
        result_2 = reco.titleList

        self.assertEqual(result_1, result_2)

if __name__ == "__main__":
    unittest.main()