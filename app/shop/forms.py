from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class Order(Form):
    name = TextField('Ваше имя', validators = [Required()])
    adress = TextField('Ваш адрес', validators = [Required()])
    description = TextField('Дополнительная информация')
    submit = SubmitField('Подтвердить заказ')

class AddItem(Form):
    name = TextField('name', validators = [Required()])
    category = TextField('category', validators = [Required()])
    cost = TextField('cost', validators = [Required()])
    photo_hash = TextField('photo')
    description = TextField('descr')
    submit = SubmitField('add')
