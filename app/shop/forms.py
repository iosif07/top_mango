from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class AddItem(Form):
    name = TextField('Название', validators = [Required()])
    category = TextField('Категория', validators = [Required()])
    cost = TextField('Стоимость', validators = [Required()])
    photo_hash = TextField('Изображение')
    description = TextField('Описание')
    submit = SubmitField('добавить')

class Order(Form):
    name = TextField('name', validators = [Required()])
    adress = TextField('adress', validators = [Required()])
    description = TextField('description')
    submit = SubmitField('Order')
