from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

class AddPetForm(FlaskForm):
    '''Form to add a new pet'''
    name = StringField('Pet Name', validators=[InputRequired(message="Name cannot be blank.")])
    species = StringField('Species', validators=[InputRequired(message="Species cannot be blank."), AnyOf(values=["cat", "dog", "porcupine"])])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message="Not a valid URL.")])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = StringField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    '''Form to edit pet'''
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message="Not a valid URL.")])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField("Available?")

