# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommentController(BaseTestCase):
    """CommentController integration test stubs"""

    def test_add_com(self):
        """Test case for add_com

        Dodaj novi komentar
        """
        body = Comment()
        response = self.client.open(
            '/v2/comment',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_com(self):
        """Test case for get_com

        Lista komentara
        """
        response = self.client.open(
            '/v2/comment',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
