from unittest import mock
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta

from  services.implementations.customer_service import Customer_Service


testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


# Unit test with Parametrize. This is used in data driven development. Do more of this test.
#@pytest.mark.parametrize("a,b,expected", testdata)
#def test_timedistance_v0(a, b, expected):
 #   diff = a - b
 #   assert diff == expected


# Patch. Object (class, Method)
# Then supply a return value to this class.
# Them execute a dependent method.
# This is mocking framework using unittest.mock. Which is an entirely diffrent framework but pytest encourages it.
# Make more of this. Clean up customer class once perminent solutions are available.
#@patch.object(Customer_Service, 'someAPICall')
#def test_foo(test_some_fn):
 #   test_some_fn.return_value = 1
  #  tmp = Customer_Service().slowTest()
  #  assert tmp == 2