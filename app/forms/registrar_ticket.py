# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class TicketForm(FlaskForm):
    DS_TIPO = RadioField('Tipo', choices=[('seguranca', 'Segurança'), ('meio-ambiente', 'Meio ambiente'), ('energia', 'Energia')], validators=[DataRequired()])
    NM_USUARIO = StringField('Nome', validators=[DataRequired()])
    CD_MATRICULA = StringField('Matrícula', validators=[DataRequired()])
    DS_AREA = StringField('Área do Problema', validators=[DataRequired()])
    DS_POSTO = SelectField('Posto de trabalho', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], validators=[DataRequired()])
    DS_ORIGEM = SelectField('Origem', choices=[('acidente', 'Acidente'), ('qa', 'QA'), ('esmat', 'ESMAT'), ('cipa', 'CIPA'), ('outros', 'Outros')], validators=[DataRequired()])
    DS_CLASSIFICACAO = RadioField('Classificação', choices=[('alta', 'Alta'), ('baixa', 'Baixa')], validators=[DataRequired()])
    DS_PROBLEMA = TextAreaField('Descrição do Problema', validators=[DataRequired()])
    DS_ACAO = TextAreaField('Ação Imediata')
    DS_SOLUCAO = TextAreaField('Solução Proposta')
    NM_RESPONSAVEL = StringField('Responsável', validators=[DataRequired()])
    submit = SubmitField('Enviar')
