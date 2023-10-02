#!/usr/bin/env python3
"""Creates a GraphQL and GraphiQL views in flask"""

from flask import Flask
from flask_graphql import GraphQLView
from models import storage
from schema import User, Post, schema
from os import getenv

app = Flask(__name__)

app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
)

@app.teardown_appcontext
def removeSession(exception=None):
    """Removes the current db session"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=getenv('DEBUG', False), host='0.0.0.0', port=5000)
