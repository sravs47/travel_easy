# @app.route('/index')
# def index():
#     return render_template('index.html')

from flask_testing import TestCase
import flask_testing
import unittest

class TestNotRenderTemplates(TestCase):
    render_templates = False

    def test_assert_mytemplate_used(self):
        response = self.client.get("/templates/")
        assert "" == response.data

if __name__ == '__main__':
    unittest.main()