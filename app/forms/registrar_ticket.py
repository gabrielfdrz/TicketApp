from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField,DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

class TicketForm(FlaskForm):
    tipo = RadioField('Tipo', choices=[('seguranca', 'Segurança'), ('meio-ambiente', 'Meio Ambiente'), ('energia', 'Energia')], validators=[DataRequired()])
    usuario = StringField('Nome', validators=[DataRequired()])
    matricula = StringField('Matrícula', validators=[DataRequired()])
    area = StringField('Área do Problema', validators=[DataRequired()])
    posto = SelectField('Posto de Trabalho', choices=[('analista de qualidade', 'Analista de Qualidade'), ('engenheiro de projetos mecanicos', 'Engenheiro de Projetos Mecânicos'), ('gerente de producao', 'Gerente de Produção'), ('operador de maquina', 'Operador de Máquina'), ('rescursos humanos', 'Recursos Humanos'), ('supervisor de linha de producao', 'Supervisor de Linha de Produção'), ('tecnico de manutencao', 'Técnico de Manutenção')], validators=[DataRequired()])
    origem = SelectField('Origem', choices=[('acidente', 'Acidente'), ('qa', 'QA'), ('esmat', 'ESMAT'), ('cipa', 'CIPA'), ('outros', 'Outros')], validators=[DataRequired()])
    classificacao = RadioField('Classificação', choices=[('alta', 'Alta'), ('baixa', 'Baixa')], validators=[DataRequired()])
    problema = TextAreaField('Descrição do Problema', validators=[DataRequired()])
    acao = TextAreaField('Ação Imediata')
    solucao = TextAreaField('Solução Proposta')
    responsavel = StringField('Responsável', validators=[DataRequired()])
    data_emissao = DateTimeField('Data de Emissão', default=datetime.now(), format='%Y-%m-%d %H:%M:%S')
