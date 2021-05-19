import unittest
from unittest.mock import Mock, patch

from termProject import TermProject
from recommend import Recommend

class TermProjectTest(unittest.TestCase):
    def test_eng_and_kor(self):
        mock = Mock(return_value=['유선마우스) 3M마우스 사용후기', '제닉스 TITAN GM AIR WIRELESS (화이트) 마우스 사용 후기', '마이크로소프트 스컬프트 마우스 한 달이상 사용후기', '로지텍 G603 무선 마우스 사용후기'])
        term = TermProject()
        reco = Recommend()
        term.search('마우스')
        result_1 = reco.titleList
        
        self.assertEqual(result_1[0], mock()[0])

if __name__ == "__main__":
    unittest.main()