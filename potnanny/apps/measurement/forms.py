from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, BooleanField
from wtforms.validators import DataRequired, ValidationError, NumberRange, \
            InputRequired
from .models import MeasurementType


def unique_name_check(form, field):
    if form.id.data:
        o = MeasurementType.query.filter(
                MeasurementType.id != int(form.id.data), 
                MeasurementType.name == field.data).first()
    else:
        o = MeasurementType.query.filter_by(name=field.data).first()
    
    if o:
        raise ValidationError('Name must be unique')


class MeasurementTypeForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('name', 
                validators=[InputRequired(),
                            unique_name_check])
    active = BooleanField('measurement type enabled', default="1")








