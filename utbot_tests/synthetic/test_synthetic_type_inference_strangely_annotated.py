import sys
sys.path.append('/')
import unittest
import builtins
import synthetic.type_inference.strangely_annotated


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable synthetic.type_inference.strangely_annotated.call_len_with_partially_quoted_annotation
    # region
    def test_call_len_with_partially_quoted_annotation(self):
        actual = synthetic.type_inference.strangely_annotated.call_len_with_partially_quoted_annotation([int('9ba461594', 12), int('535a7988a', 13), int('000', 0), int('000', 0), int(' 0O123   ', 0), int('535a7988a', 13), int('-1'), int('535a7988a', 13)])
        
        self.assertEqual(8, actual)
    
    # endregion
    
    # endregion
    
    # region Test suites for executable synthetic.type_inference.strangely_annotated.inc_with_turned_off_mypy
    # region
    def test_inc_with_turned_off_mypy(self):
        actual = synthetic.type_inference.strangely_annotated.inc_with_turned_off_mypy(int('100000001', 16))
        
        self.assertEqual(4294967298, actual)
    
    # endregion
    
    # endregion
    

