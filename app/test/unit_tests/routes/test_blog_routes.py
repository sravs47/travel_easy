from app.routes.blog.blog_routes import testimonals, is_logged_in,render_template,request,session,db,datetime,blog
from unittest import TestCase
from unittest.mock import patch, Mock


class testBlogRoutes(TestCase):

    @patch('app.routes.blog.blog_routes.request')
    @patch('app.routes.blog.blog_routes.testimonals')
    def test_blog(self,mock_request,mock_testimonals):
        mock_request.method = 'POST'
        mock_request.form.return_value = {'comment':'some comment', 'rate':'2'}
        response =blog()




