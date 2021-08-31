"""
CID Procedimientos, formularios
"""
from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from plataforma_web.blueprints.cid_procedimientos.models import CIDProcedimiento


class CIDProcedimientoForm(FlaskForm):
    """Formulario CID Procedimiento"""

    titulo_procedimiento = StringField("Título", validators=[DataRequired(), Length(max=256)])
    codigo = StringField("Código", validators=[DataRequired(), Length(max=16)])
    revision = IntegerField("Revisión", validators=[DataRequired()])
    fecha = DateField("Fecha de elaboración", validators=[DataRequired()])
    objetivo = StringField("Objetivo", validators=[DataRequired()])
    alcance = StringField("Alcance", validators=[DataRequired()])
    documentos = StringField("Documentos", validators=[DataRequired()])
    definiciones = StringField("Definiciones", validators=[DataRequired()])
    responsabilidades = StringField("Responsabilidades", validators=[DataRequired()])
    desarrollo = StringField("Desarrollo", validators=[DataRequired()])
    registros = StringField("Registros", validators=[DataRequired()])
    cambios = StringField("Cambios", validators=[DataRequired()])
    guardar = SubmitField("Guardar")