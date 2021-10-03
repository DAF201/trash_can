import json
import graphene

class Query(graphene.ObjectType):
    name = graphene.String(value=graphene.String(default_value="B"))
    age =graphene.String(value=graphene.String(default_value="25"))


    def resolve_name(root,info,value):
        return value
    def resolve_age(root,into,value):
        return value

schema=graphene.Schema(query=Query)        

query='''
query thatQuery{
    name
    age
}
'''
result=schema.execute(query)
result=json.dumps(result.data, indent=3)
# print(type(result))
# result=result.split(':')
# result=str(result[1])
# result=result.split('}')
# result=str(result[0])
# result=result.replace('\n','')
# result=result.replace('"','')
# result=result.replace(' ','')
# result=result.split(',')
# print(result)
# # result=json.load(result)
# # print(result['name'])

