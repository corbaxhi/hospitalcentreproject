from flask_restful import Resource, Api, request
from package.model import conn



class Procedures(Resource):

    def get(self):

        procedure = conn.execute("SELECT * from procedure").fetchall()
        return procedure

    def post(self):

        procedure = request.get_json(force=True)
        code = procedure['code']
        name = procedure['name']
        cost = procedure['cost']
        conn.execute('''INSERT INTO procedure(code, name, cost) VALUES(?,?,?)''', (code, name, cost))
        conn.commit()
        return procedure



class Procedure(Resource):

    def get(self,code):

        procedure = conn.execute("SELECT * FROM procedure WHERE code=?",(code,)).fetchall()
        return procedure


    def delete(self,code):

        conn.execute("DELETE FROM procedure WHERE code=?",(code,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,code):

        procedure = request.get_json(force=True)
        name = procedure['name']
        cost = procedure['cost']
        conn.execute("UPDATE procedure SET name=?,cost=? WHERE code=?", (name, cost, code))
        conn.commit()
        return procedure