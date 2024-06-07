from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired

class TicketForm(FlaskForm):
    tipo = RadioField('Tipo', choices=[('seguranca', 'Segurança'), ('meio-ambiente', 'Meio Ambiente'), ('energia', 'Energia')], validators=[DataRequired()])
    nome_usuario = StringField('Nome', validators=[DataRequired()])
    matricula = IntegerField('Matrícula', validators=[DataRequired()])
    area = StringField('Área do Problema', validators=[DataRequired()])
    posto = SelectField('Posto de Trabalho', choices=[('analista de qualidade', 'Analista de Qualidade'), ('engenheiro de projetos mecanicos', 'Engenheiro de Projetos Mecânicos'), ('gerente de producao', 'Gerente de Produção'), ('operador de maquina', 'Operador de Máquina'), ('rescursos humanos', 'Recursos Humanos'), ('supervisor de linha de producao', 'Supervisor de Linha de Produção'), ('tecnico de manutencao', 'Técnico de Manutenção')], coerce=int, validators=[DataRequired()])
    origem = SelectField('Origem', choices=[('acidente', 'Acidente'), ('qa', 'QA'), ('esmat', 'ESMAT'), ('cipa', 'CIPA'), ('outros', 'Outros')], validators=[DataRequired()])
    classificacao = RadioField('Classificação', choices=[('alta', 'Condição Insegura'), ('baixa', 'Ato Inseguro')], validators=[DataRequired()])
    problema = TextAreaField('Descrição do Problema', validators=[DataRequired()])
    acao_imediata = TextAreaField('Ação Imediata')
    solucao_proposta = TextAreaField('Solução Proposta')
    responsavel = StringField('Responsável', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])

class TicketStatusForm(FlaskForm):
    status = RadioField('Status', choices=[('ABERTO', 'Aberto'), ('ENCERRADO', 'Encerrado')], default='ABERTO')
