import pytest
from utils import HRDiagram

class TestHRDiagram(): # all below writte by copilot
    def test_init(self):
        myhrd_object = HRDiagram(data='data/6_class.csv')
        assert myhrd_object.data is not None
        assert 'log_T' in myhrd_object.data.columns
        assert 'log_L' in myhrd_object.data.columns
        assert myhrd_object.colors is not None

    def test_init_empty(self): # If start writing this test's name, copilot will give you the code below
        with pytest.raises(ValueError):
            myhrd_object = HRDiagram(data='data/empty.csv')