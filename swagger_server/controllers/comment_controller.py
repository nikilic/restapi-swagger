import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server import util


def add_com(body):  # noqa: E501
    """Dodaj novi komentar

     # noqa: E501

    :param body: Objekat za komentar koji treba da se doda u bazu
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_com():  # noqa: E501
    """Lista komentara

     # noqa: E501


    :rtype: List[Comment]
    """
    return 'do some magic!'
