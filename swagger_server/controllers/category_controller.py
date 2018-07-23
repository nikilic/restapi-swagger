import connexion
import six

from swagger_server.models.category import Category  # noqa: E501
from swagger_server import util
from swagger_server.__main__ import db_session
from connexion import NoContent
from swagger_server import orm


def add_cat(body):  # noqa: E501
    """Dodaj novu kategoriju

     # noqa: E501

    :param body: Objekat za kategoriju koji treba da se doda u bazu
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Category.from_dict(connexion.request.get_json())  # noqa: E501

    db_session.add(orm.Category(body.name))
    db_session.commit()
    return NoContent, 201


def delete_cat(catId):  # noqa: E501
    """Brise kategoriju

     # noqa: E501

    :param catId: Category id to delete
    :type catId: int

    :rtype: None
    """
    return 'do some magic!'


def get_cat():  # noqa: E501
    """Lista kategorija

     # noqa: E501


    :rtype: List[Category]
    """
    q = db_session.query(orm.Category)
    return [p.dump() for p in q]


def update_cat(body):  # noqa: E501
    """Promeni postojecu kategoriju

     # noqa: E501

    :param body: Objekat za kategoriju koji treba da se doda u bazu
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Category.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
