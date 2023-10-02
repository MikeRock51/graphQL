#!/usr/bin/env python3
"""Defines Graphql schema for the app"""

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.user import User as UserModel
from models.post import Post as PostModel
from models import storage


class User(SQLAlchemyObjectType):
    """Defines a GraphQL type for a user"""
    class Meta:
        """Defines metadata and configuration for a user"""
        model = UserModel
        interfaces = (relay.Node, )

class Post(SQLAlchemyObjectType):
    """Defines a GraphQL type for a post"""
    class Meta:
        """Defines metadata and configuration for a user"""
        model = PostModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    """Defines the entry point for querying data from the API"""
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User.connection)
    posts = SQLAlchemyConnectionField(Post.connection)

schema = graphene.Schema(query=Query)
