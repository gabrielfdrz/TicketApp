# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class TicketForm(FlaskForm):
    ds_tipo = StringField('Tipo', validators=[DataRequired(), Length(max=20)])
    nm_usuario = StringField('Nome do Usuário', validators=[DataRequired(), Length(max=100)])
    cd_matricula = IntegerField('Matrícula', validators=[DataRequired()])
    ds_area = StringField('Área', validators=[DataRequired(), Length(max=50)])
    ds_posto = IntegerField('Posto', validators=[Optional()])
    ds_origem = StringField('Origem', validators=[Optional(), Length(max=10)])
    ds_classificacao = StringField('Classificação', validators=[Optional(), Length(max=20)])
    ds_problema = TextAreaField('Problema', validators=[DataRequired(), Length(max=2000)])
    ds_acao = TextAreaField('Ação', validators=[Optional(), Length(max=2000)])
    ds_solucao = TextAreaField('Solução', validators=[Optional(), Length(max=2000)])
    nm_responsavel = StringField('Nome do Responsável', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Criar Ticket')
