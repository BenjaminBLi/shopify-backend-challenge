import graphene

import products.schema

class Query(products.schema.Query, graphene.ObjectType):
    pass

class Mutation(products.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
