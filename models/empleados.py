# EMPLOYEE_FIELDS = [
#     "nombre",
#     "apellido",
#     "email",
#     "telefono",
#     "puesto",
#     "salario",
#     "area_id",
# ]


# def empleado_to_dict(document):
#     if not document:
#         return None

#     empleado = {field: document.get(field) for field in EMPLOYEE_FIELDS}
#     empleado["id"] = str(document.get("_id"))
#     return empleado


# def parse_empleado_payload(payload):
#     if not isinstance(payload, dict):
#         return {}

#     empleado = {
#         field: payload[field]
#         for field in EMPLOYEE_FIELDS
#         if field in payload and payload[field] is not None
#     }
#     return empleado
