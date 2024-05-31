from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CloseTicketForm(FlaskForm):
    relatorio = TextAreaField('Relatório de Solução', validators=[DataRequired()])
    submit = SubmitField('Encerrar')
