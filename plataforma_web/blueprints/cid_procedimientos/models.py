"""
CID Procedimientos, modelos
"""
from collections import OrderedDict
from plataforma_web.extensions import db
from lib.universal_mixin import UniversalMixin


class CIDProcedimiento(db.Model, UniversalMixin):
    """CIDProcedimiento"""

    ETAPAS = OrderedDict(
        [
            ("ELABORADO", "Elaborado"),
            ("REVISADO", "Revisado"),
            ("APROBADO", "Aprobado"),
            ("ARCHIVADO", "Archivado"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "cid_procedimientos"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Columnas
    titulo_procedimiento = db.Column(db.String(256), nullable=False)  # Título del Procedimiento
    codigo = db.Column(db.String(16), nullable=False)
    revision = db.Column(db.Integer(), nullable=False)
    fecha = db.Column(db.Date(), nullable=False)  # Fecha Elaboración
    objetivo = db.Column(db.Text(), nullable=False)  # OBJETIVO
    alcance = db.Column(db.Text(), nullable=False)  # ALCANCE
    documentos = db.Column(db.Text(), nullable=False)  # DOCUMENTOS DE REFERENCIA
    definiciones = db.Column(db.Text(), nullable=False)  # DEFINICIONES
    responsabilidades = db.Column(db.Text(), nullable=False)  # RESPONSABILIDADES
    desarrollo = db.Column(db.Text(), nullable=False)  # DESARROLLO
    registros = db.Column(db.Text(), nullable=False)  # REGISTROS
    cambios = db.Column(db.Text(), nullable=False)  # REGISTROS
    # elaboro = db.Column(db.Text(), nullable=False)
    # reviso = db.Column(db.Text(), nullable=False)
    # aprobo = db.Column(db.Text(), nullable=False)
    # etapa = db.Column(
    #    db.Enum(*ETAPAS, name="etapas", native_enum=False),
    #    index=True,
    #    nullable=False,
    # )
    # contenido = db.Column(db.Text(), nullable=False)

    # Hijos
    formatos = db.relationship("CIDFormato", back_populates="procedimiento")

    def __repr__(self):
        """Representación"""
        return "<CIDProcedimiento>"
