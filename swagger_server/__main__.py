#!/usr/bin/env python3

import connexion
import swagger_server.orm
from swagger_server import encoder

db_session = swagger_server.orm.init_db('sqlite:///:memory:')


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Kategorije i komentari'})
    db_session = swagger_server.orm.init_db('sqlite:///:memory:')
    application = app.app
    app.run(port=8080)
