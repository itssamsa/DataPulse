
import pytest
from pydantic import ValidationError

from app.models.usuario import Usuario


def usuario_valido():
    return {
        "cedula": "1234567890",
        "nombre": "Juan Pérez",
        "correo": "juan@example.com",
        "password": "ClaveSegura123",
        "rol": "Administrador",
        "empresa_id": "EMP001"
    }


def test_crear_usuario_valido():
    datos = usuario_valido()

    usuario = Usuario(**datos)

    assert usuario.cedula == "1234567890"
    assert usuario.nombre == "Juan Pérez"
    assert usuario.correo == "juan@example.com"
    assert usuario.password == "ClaveSegura123"
    assert usuario.rol == "Administrador"
    assert usuario.empresa_id == "EMP001"


def test_estado_por_defecto():
    usuario = Usuario(**usuario_valido())

    assert usuario.estado is True


@pytest.mark.parametrize(
    "rol",
    ["Administrador", "Analista", "Usuario general"]
)
def test_aceptar_roles_validos(rol):
    datos = usuario_valido()
    datos["rol"] = rol

    usuario = Usuario(**datos)

    assert usuario.rol == rol


def test_rechazar_rol_invalido():
    datos = usuario_valido()
    datos["rol"] = "Invitado"

    with pytest.raises(ValidationError):
        Usuario(**datos)


def test_rechazar_correo_invalido():
    datos = usuario_valido()
    datos["correo"] = "correo_invalido"

    with pytest.raises(ValidationError):
        Usuario(**datos)


def test_rechazar_campo_obligatorio_ausente():
    datos = usuario_valido()
    del datos["nombre"]

    with pytest.raises(ValidationError):
        Usuario(**datos)


def test_permitir_estado_inactivo():
    datos = usuario_valido()
    datos["estado"] = False

    usuario = Usuario(**datos)

    assert usuario.estado is False


def test_rechazar_correo_vacio():
    datos = usuario_valido()
    datos["correo"] = ""

    with pytest.raises(ValidationError):
        Usuario(**datos)
