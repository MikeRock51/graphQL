#!/usr/bin/env python3

from graphene import ObjectType, String, Schema

class Query(ObjectType):
    greet = String(firstName=String(default_value="Mike Rock"))
    later = String()

    def resolve_greet(root, info, firstName):
        return f"What's rocking {firstName}!"

    def resolve_later(root, info):
        return "Rock On!"

schema = Schema(query=Query)

print(schema.execute('{greet(firstName:"Ola")}').data['greet'])
