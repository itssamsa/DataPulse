from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generar_pdf(usuarios, empresa_id):

    archivo = f"reporte_usuarios_{empresa_id}.pdf"

    documento = SimpleDocTemplate(
        archivo
    )

    estilos = getSampleStyleSheet()
    contenido = []

    contenido.append(
        Paragraph(
            "Reporte de Usuarios DataPulse",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(1, 20)
    )

    for usuario in usuarios:

        texto = f"""
        Cedula: {usuario.get('cedula')}<br/>
        Nombre: {usuario.get('nombre')}<br/>
        Correo: {usuario.get('correo')}<br/>
        Rol: {usuario.get('rol')}<br/>
        Estado: {usuario.get('estado')}<br/>
        Empresa: {usuario.get('empresa_id')}
        """
        contenido.append(
            Paragraph(
                texto,
                estilos["Normal"]
            )
        )

        contenido.append(
            Spacer(1, 15)
        )

    documento.build(contenido)
    return archivo