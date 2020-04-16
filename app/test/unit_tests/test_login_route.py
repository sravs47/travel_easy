# # from unittest.mock import Mock,MagicMock,patch
# # from flask import request
# # import unittest
# #
# #
# # class test_login(unittest.TestCase):
# #
# #     @patch.object(request, 'POST')
# #     def test_login(self):
#
# from unittest.mock import Mock, patch
# from unittest import TestCase
# from app.routes.login.login_route import login
#
#
#
# class TestLogin(TestCase):
#
#     # @patch('app.routes.login.login_route.login')
#     @patch('flask.request')
#     def test_login(self,mock_request):
#
#         mock_request.method.side_effect = 'POST'
#
#         response_mock = Mock()
#         response_mock.form = {'username':'sravani','password':'sravani'}
#         mock_request.side_effect = response_mock
#         users = {'username':'sravs47','password':'sravani'}
#         response = login()
#         self.assertEqual(response,'index')
#



from unittest.mock import Mock

mock_obj = Mock(name='Thing',return_value=None)
print(mock_obj.sravani)
mock_obj(3)
mock_obj.assert_called_once_with(2)


# class Numbers:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a+self.b
#
# num_obj = Numbers(10,10)
# print(num_obj)
