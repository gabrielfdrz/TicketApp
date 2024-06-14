from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField,DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

class TicketForm(FlaskForm):
    tipo = RadioField('Tipo', choices=[('Segurança', 'Segurança'), ('Meio Ambiente', 'Meio Ambiente'), ('Energia', 'Energia')], validators=[DataRequired()])
    usuario = StringField('Nome', validators=[DataRequired()])
    matricula = StringField('Matrícula', validators=[DataRequired()])
    area = StringField('Área do Problema', validators=[DataRequired()])
    posto = SelectField('Posto de Trabalho', choices=[('Conferência', 'Conferência'),('Embalagem', 'Embalagem'),('Faturamento', 'Faturamento'),('Insumos', 'Insumos'),('Inventário', 'Inventário'),('Logistica', 'Logistica'),('Packed', 'Packed'),('Picking', 'Picking'),('Pré Embalagem', 'Pré Embalagem'),('Putaway', 'Putaway'),('Qualidade', 'Qualidade'),('Recebimento', 'Recebimento')], validators=[DataRequired()])
    origem = SelectField('Origem', choices=[('Acidente', 'Acidente'), ('Qa', 'QA'), ('ESMAT', 'ESMAT'), ('CIPA', 'CIPA'), ('Outros', 'Outros')], validators=[DataRequired()])
    classificacao = RadioField('Classificação', choices=[('Ato Inseguro', 'Ato Inseguro'), ('Condição Insegura', 'Condição Insegura')], validators=[DataRequired()])
    problema = TextAreaField('Descrição do Problema', validators=[DataRequired()])
    acao = TextAreaField('Ação Imediata')
    solucao = TextAreaField('Solução Proposta')
    responsavel = StringField('Responsável', validators=[DataRequired()])
    data_emissao = DateTimeField('Data de Emissão', default=datetime.now(), format='%Y-%m-%d %H:%M:%S')
