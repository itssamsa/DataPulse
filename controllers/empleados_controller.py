# from bson import ObjectId

# from models.empleados import empleado_to_dict, parse_empleado_payload


# def list_empleados(db):
#     empleados = db.empleados.find()
#     return [empleado_to_dict(empleado) for empleado in empleados]


# def get_empleado(db, empleado_id):
#     if not ObjectId.is_valid(empleado_id):
#         return None

#     empleado = db.empleados.find_one({"_id": ObjectId(empleado_id)})
#     return empleado_to_dict(empleado)


# def create_empleado(db, payload):
#     empleado = parse_empleado_payload(payload)
#     if not empleado:
#         return None

#     result = db.empleados.insert_one(empleado)
#     return get_empleado(db, str(result.inserted_id))


# def update_empleado(db, empleado_id, payload):
#     if not ObjectId.is_valid(empleado_id):
#         return None

#     empleado = parse_empleado_payload(payload)
#     if not empleado:
#         return None

#     result = db.empleados.update_one(
#         {"_id": ObjectId(empleado_id)},
#         {"$set": empleado},
#     )

#     if result.matched_count == 0:
#         return None

#     return get_empleado(db, empleado_id)


# def delete_empleado(db, empleado_id):
#     if not ObjectId.is_valid(empleado_id):
#         return False

#     result = db.empleados.delete_one({"_id": ObjectId(empleado_id)})
#     return result.deleted_count == 1
