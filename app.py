from ariadne import ObjectType, QueryType, gql, make_executable_schema, MutationType
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        students(sid:Int!): Student!
        classes(cid:Int!): Class!
    }

    type Student {
        name:String!
        id:Int!
    }

    type Class{ 
        id:Int!
        name:String!
        studentinfo:[Student!]!
    }

    type Mutation{
        students(name:String!):String!
        classes(name:String!):String!
        enroll(sid:Int!, cid:Int!):String!
    }
""")

student_id = 1238125
student_list = {}

def resolve_students(_, info, name):
    global student_id
    global student_list

    student_list[str(student_id)] = name
    student_id =+ 1
    return name
mutation = MutationType()
mutation.set_field("students", resolve_students)

query = QueryType()
def resolve_student(_, info, sid):
    global student_list
    return{"id": sid, "name": student_list.get(str(sid))}
query.set_field("students", resolve_student)

class class_info:
    def __init__(self, course_name):
        self.course_name = course_name
        self.student_list = []


class_id = 1122334
class_list = {}

def resolve_classes(_, info, name):
    global class_id
    global class_list
    new_class = class_info(name)
    class_list[str(class_id)] = new_class
    return name
mutation.set_field("classes", resolve_classes)

def resolve_classname(_, info, cid):
    global class_list
    return {"id": cid, "name": class_list.get(str(cid)).course_name, "studentinfo": class_list.get(str(cid)).student_list}
query.set_field("classes", resolve_classname)

def resolve_enroll(_, info,sid, cid):
    global student_id
    global class_id
    global student_list
    global class_list
    class_info = class_list.get(str(cid))
    student_name = student_list[str(sid)]
    class_info.student_list.append({"name": student_name, "id": sid})
    return class_info.course_name
mutation.set_field("enroll", resolve_enroll)

schema = make_executable_schema(type_defs, [query, mutation])
app = GraphQL(schema, debug=True)