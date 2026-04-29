# from flask import Blueprint, current_app, jsonify, request

# from controllers.empleados_controller import (
#     create_empleado,
#     delete_empleado,
#     get_empleado,
#     list_empleados,
#     update_empleado,
# )

# empleados_bp = Blueprint("empleados", __name__, url_prefix="/empleados")


# @empleados_bp.route("", methods=["GET"])
# def obtener_empleados():
#     empleados = list_empleados(current_app.db)
#     return jsonify(empleados), 200


# @empleados_bp.route("/<empleado_id>", methods=["GET"])
# def obtener_empleado(empleado_id):
#     empleado = get_empleado(current_app.db, empleado_id)
#     if empleado is None:
#         return jsonify({"error": "Empleado no encontrado"}), 404
#     return jsonify(empleado), 200


# @empleados_bp.route("", methods=["POST"])
# def crear_empleado():
#     payload = request.get_json(silent=True)
#     if not payload:
#         return jsonify({"error": "JSON inválido o cuerpo vacío"}), 400

#     empleado = create_empleado(current_app.db, payload)
#     if empleado is None:
#         return jsonify({"error": "Datos de empleado inválidos"}), 400

#     return jsonify(empleado), 201


# @empleados_bp.route("/<empleado_id>", methods=["PUT"])
# def actualizar_empleado(empleado_id):
#     payload = request.get_json(silent=True)
#     if not payload:
#         return jsonify({"error": "JSON inválido o cuerpo vacío"}), 400

#     empleado = update_empleado(current_app.db, empleado_id, payload)
#     if empleado is None:
#         return jsonify({"error": "Empleado no encontrado o datos inválidos"}), 404

#     return jsonify(empleado), 200


# @empleados_bp.route("/<empleado_id>", methods=["DELETE"])
# def eliminar_empleado(empleado_id):
#     eliminado = delete_empleado(current_app.db, empleado_id)
#     if not eliminado:
#         return jsonify({"error": "Empleado no encontrado"}), 404
#     return jsonify({"message": "Empleado eliminado correctamente"}), 200
