import sys
import os
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI') or 'mongodb://mongo'
client = MongoClient(MONGO_URI)
db = client.application
student_col = db.students

id = db.info.find_one()
if not id:
    db.info.insert_one({ 'id_counter': 0 })

def get_id():
  id = db.info.find_one()['id_counter'] + 1
  db.info.update_many({}, { '$set': { 'id_counter': id } })
  return id


def add(student=None):
    res = student_col.find_one({ 'first_name': student.first_name, 'last_name': student.last_name })
    if res:
        return 'already exists', 409

    student.student_id = get_id()
    rec = student_col.insert_one(student.to_dict())
    return str(student.student_id)


def get_by_id(student_id=None, subject=None):
    student = student_col.find_one({ 'student_id': student_id })
    print(student, file=sys.stderr)
    if not student:
        return 'not found', 404
    student['student_id'] = student_id
    del student['_id']
    return student


def delete(student_id=None):
    student = student_col.find_one_and_delete({ 'student_id': student_id })
    if not student:
        return 'not found', 404
    return student_id
