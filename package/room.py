from flask_restful import Resource, Api, request
from package.model import conn



class Rooms(Resource):

    def get(self):

        room = conn.execute("SELECT * from room").fetchall()
        return room

    def post(self):

        room = request.get_json(force=True)
        room_no = room['room_no']
        room_type = room['room_type']
        available = room['available']
        conn.execute('''INSERT INTO room(room_no, room_type, available) VALUES(?,?,?)''', (room_no, room_type, available))
        conn.commit()
        return room



class Room(Resource):

    def get(self,room_no):

        room = conn.execute("SELECT * FROM room WHERE room_no=?",(room_no,)).fetchall()
        return room


    def delete(self,room_no):

        conn.execute("DELETE FROM room WHERE room_no=?",(room_no,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,room_no):

        room = request.get_json(force=True)
        room_type = room['room_type']
        available = room['available']
        conn.execute("UPDATE room SET room_type=?,available=? WHERE room_no=?", (room_type, available, room_no))
        conn.commit()
        return room