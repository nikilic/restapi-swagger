# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.category import Category  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCategoryController(BaseTestCase):
    """CategoryController integration test stubs"""

    def test_add_cat(self):
        """Test case for add_cat

        Dodaj novu kategoriju
        """
        body = Category()
        response = self.client.open(
            '/v2/category',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cat(self):
        """Test case for delete_cat

        Brise kategoriju
        """
        response = self.client.open(
            '/v2/category'.format(catId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cat(self):
        """Test case for get_cat

        Lista kategorija
        """
        response = self.client.open(
            '/v2/category',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_cat(self):
        """Test case for update_cat

        Promeni postojecu kategoriju
        """
        body = Category()
        response = self.client.open(
            '/v2/category',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
