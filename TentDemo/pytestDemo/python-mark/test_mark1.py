import sys

import pytest

a=11
#
# @pytest.mark.skipif(sys.platform=='darwin',reason=" does not run on mac")
# def test_case1():
#     assert  True
#
# @pytest.mark.skipif(sys.platform=='win',reason=" does not run on win")
# def test_case2():
#     assert  True

@pytest.mark.skipif(a==11,reason=" does not run on mac")
def test_case1():
    assert  True

@pytest.mark.skipif(a==12,reason=" does not run on win")
def test_case2():
    assert  False