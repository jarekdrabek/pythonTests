import mock
import unittest
from function import square, main


class TestNotMockedFunction(unittest.TestCase):

    @mock.patch('__main__.square', return_value=1)
    def test_function(self, mocked_square):
        # because you need to patch in exact place where function that has to be mocked is called
        self.assertEquals(square(5), 1)

    @mock.patch('function.square')
    @mock.patch('function.cube')
    @mock.patch('function.quad')
    def test_main_function(self, mocked_quad, mocked_cube, mocked_square):
        # undeling function are mocks so calling main(5) will return mock
        mocked_square.return_value = 1
        mocked_cube.return_value = 0
        mocked_quad.return_value = 5
        self.assertEquals(main(5), 6)
        mocked_square.assert_called_once_with(5)
        mocked_cube.assert_called_once_with(10)
        mocked_quad.assert_called_once_with(20)

if __name__ == '__main__':
    unittest.main()

