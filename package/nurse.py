from flask_restful import Resource, Api, request
from package.model import conn
class Nurses(Resource):

    def get(self):

        nurses = conn.execute("SELECT * FROM nurse ORDER BY nur_date DESC").fetchall()
        return nurses



    def post(self):

        nurseInput = request.get_json(force=True)
        nur_first_name=nurseInput['nur_first_name']
        nur_last_name = nurseInput['nur_last_name']
        nur_ph_no = nurseInput['nur_ph_no']
        nur_address = nurseInput['nur_address']
        nurseInput['nur_id']=conn.execute('''INSERT INTO nurse(nur_first_name,nur_last_name,nur_ph_no,nur_address)
            VALUES(?,?,?,?)''', (nur_first_name, nur_last_name,nur_ph_no,nur_address)).lastrowid
        conn.commit()
        return nurseInput

class Nurse(Resource):


    def get(self,id):

        nurse = conn.execute("SELECT * FROM nurse WHERE nur_id=?",(id,)).fetchall()
        return nurse

    def delete(self, id):

        conn.execute("DELETE FROM nurse WHERE nur_id=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):

        nurseInput = request.get_json(force=True)
        nur_first_name=nurseInput['nur_first_name']
        nur_last_name = nurseInput['nur_last_name']
        nur_ph_no = nurseInput['nur_ph_no']
        nur_address = nurseInput['nur_address']
        conn.execute(
            "UPDATE nurse SET nur_first_name=?,nur_last_name=?,nur_ph_no=?,nur_address=? WHERE nur_id=?",
            (nur_first_name, nur_last_name, nur_ph_no, nur_address, id))
        conn.commit()
        return nurseInput