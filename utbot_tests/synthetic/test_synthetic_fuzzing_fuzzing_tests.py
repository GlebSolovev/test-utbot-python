import sys
sys.path.append('/')
import unittest
import builtins
import synthetic.fuzzing.fuzzing_tests


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable synthetic.fuzzing.fuzzing_tests.check_constants_if_cases
    # region
    def test_check_constants_if_cases(self):
        actual = synthetic.fuzzing.fuzzing_tests.check_constants_if_cases(int('3723ai4h', 20))
        
        self.assertEqual('> 10', actual)
    
    def test_check_constants_if_cases1(self):
        actual = synthetic.fuzzing.fuzzing_tests.check_constants_if_cases(6)
        
        self.assertEqual('default', actual)
    
    def test_check_constants_if_cases2(self):
        actual = synthetic.fuzzing.fuzzing_tests.check_constants_if_cases(5)
        
        self.assertEqual('5', actual)
    
    # endregion
    
    # endregion
    
    # region Test suites for executable synthetic.fuzzing.fuzzing_tests.check_constants_in_called_function
    # region
    def test_check_constants_in_called_function(self):
        actual = synthetic.fuzzing.fuzzing_tests.check_constants_in_called_function(int('535a7988a', 13))
        
        self.assertEqual('> 10', actual)
    
    # endregion
    
    # endregion
    

