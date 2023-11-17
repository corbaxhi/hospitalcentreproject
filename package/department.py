
from flask_restful import Resource, Api, request
from package.model import conn



class Departments(Resource):

    def get(self):

        department = conn.execute("SELECT department_id, name, head_id, doc_first_name, doc_last_name FROM department INNER JOIN doctor ON doctor.doc_id = department.head_id").fetchall()
        return department

    def post(self):

        department = request.get_json(force=True)
        department_id = department['department_id']
        name = department['name']
        head_id = department['head_id']
        conn.execute('''INSERT INTO department(department_id, name, head_id) VALUES(?,?,?)''', (department_id, name, head_id))
        conn.commit()
        return department



class Department(Resource):

    def get(self,department_id):

        department = conn.execute("SELECT * FROM department WHERE department_id=?",(department_id,)).fetchall()
        return department

    def put(self,department_id):

        department = request.get_json(force=True)
        name = department['name']
        head_id = department['head_id']
        conn.execute("UPDATE department SET name=?,head_id=? WHERE department_id=?", (name, head_id, department_id))
        conn.commit()
        return department