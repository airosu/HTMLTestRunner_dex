from unittest import TestCase, TestLoader, TestSuite
import HTMLTestRunner_dex



x = 1
y = 2
arr = [1, 2, 3]


# ===================================== CREATING TESTS ====================================

class Test1(TestCase):
    """ Test Group 1 - This test has passed """
    
    def test_01_pass(self):
        """ Test 1 - This step has passed"""
        if x==1:
            pass
    
    def test_02_pass(self):
        """ Test 2 - This step has also passed """
        if x==1:
            pass
    

    def test_03_pass_print(self):
        """ Test 3 - This step printed a stirng """
        print('Hello World!')
    
    
    def test_04_this_step_does_not_have_docstring(self):
        if x + y == 3:
            pass
    


class Test2(TestCase):
    """ Test Group 2 - This test has failed """

    def test_01_pass(self):
        """ Test 1 - This step has passed"""
        if x==1:
            pass

    def test_02_this_step_will_fail(self):
        """ Test 2 - This step has failed"""

        self.assertIn(5, arr)
    
    def test_03_pass(self):
        """ Test 3 - This step has passed"""
        if x==1:
            pass
    
    def test_04_fail(self):
        """ Test 4 - This step has also failed """
        if y == 2:
            self.fail('This is a custom fail message')


class Test3(TestCase):
    """ Test Group 3 - This test has returned an error """

    def test_01_pass(self):
        """ Test 1 - This step has returned an error"""
        
        print(arr / x)
  




# ===================================== RUNNER SET-UP ====================================

tc_test1 = TestLoader().loadTestsFromTestCase(Test1)
tc_test2 = TestLoader().loadTestsFromTestCase(Test2)
tc_test3 = TestLoader().loadTestsFromTestCase(Test3)

suite = TestSuite([
    tc_test1,
    tc_test2,
    tc_test3
])


runner = HTMLTestRunner_dex.HTMLTestRunner(
    title='HTML Test Runner Sample',
    description='This is an example of the generated file.',
    verbosity=1
)








# ====================================== RUN COMMAND ======================================

runner.run(suite)

