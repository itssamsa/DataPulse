from openpyxl import Workbook

def generar_excel(usuarios, empresa_id):

    archivo = f"reporte_usuarios_{empresa_id}.xlsx"

    libro = Workbook()

    hoja = libro.active
    hoja.title = "Usuarios"

    hoja.append(
        [
            "Cedula",
            "Nombre",
            "Correo",
            "Rol",
            "Estado",
            "Empresa"
        ]
    )

    for usuario in usuarios:

        hoja.append(
            [
                usuario.get("cedula"),
                usuario.get("nombre"),
                usuario.get("correo"),
                usuario.get("rol"),
                usuario.get("estado"),
                usuario.get("empresa_id")
            ]
        )

    libro.save(archivo)
    return archivo