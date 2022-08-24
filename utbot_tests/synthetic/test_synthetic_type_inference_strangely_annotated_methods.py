import sys
sys.path.append('/')
import unittest
import builtins
import synthetic.type_inference.strangely_annotated
import types


class TestDummyWithMethodsToTest(unittest.TestCase):
    # region Test suites for executable synthetic.type_inference.strangely_annotated.__init__
    # region
    def test__init__(self):
        dummy_with_methods_to_test = synthetic.type_inference.strangely_annotated.DummyWithMethodsToTest(int('0123', 10))
        
        actual = dummy_with_methods_to_test.__init__(int('4000001', 32))
        
        self.assertEqual(None, actual)
    
    # endregion
    
    # endregion
    
    # region Test suites for executable synthetic.type_inference.strangely_annotated.inc_by_with_future_annotation
    # region
    def test_inc_by_with_future_annotation(self):
        dummy_with_methods_to_test = synthetic.type_inference.strangely_annotated.DummyWithMethodsToTest(int('0123', 10))
        self1 = synthetic.type_inference.strangely_annotated.DummyWithMethodsToTest(int('-1'))
        
        actual = dummy_with_methods_to_test.inc_by_with_future_annotation(self1)
        
        self.assertEqual(122, actual)
    
    # endregion
    
    # endregion
    

