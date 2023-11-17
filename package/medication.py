
from flask_restful import Resource, Api, request
from package.model import conn



class Medications(Resource):

    def get(self):

        medication = conn.execute("SELECT * from medication").fetchall()
        return medication

    def post(self):

        medication = request.get_json(force=True)
        code = medication['code']
        name = medication['name']
        brand = medication['brand']
        description = medication['description']
        conn.execute('''INSERT INTO medication(code, name, brand, description) VALUES(?,?,?,?)''', (code, name, brand, description))
        conn.commit()
        return medication



class Medication(Resource):

    def get(self,code):

        medication = conn.execute("SELECT * FROM medication WHERE code=?",(code,)).fetchall()
        return medication


    def delete(self,code):

        conn.execute("DELETE FROM medication WHERE code=?",(code,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,code):

        medication = request.get_json(force=True)
        name = medication['name']
        brand = medication['brand']
        description = medication['description']
        conn.execute("UPDATE medication SET name=?,brand=?,description=? WHERE code=?", (name, brand, description, code))
        conn.commit()
        return medication