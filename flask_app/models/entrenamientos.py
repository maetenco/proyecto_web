from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from .mascotas import Mascota

class Entrenamiento:
    def __init__(self, data):
        self.tuvo_entrenamiento = data['tuvo_ entrenamiento']
        self.motivo_entrenamiento = data['motivo_entrenamiento']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.mascota_id = data['mascota_id']

    @staticmethod
    def validate_entrenamiento(form):
        #Aquí recibe el request.form
        is_valid = True

        if len(form['motivo_entrenamiento']) < 3:
            is_valid = False
            flash("Ingrese el motivo de entrenamiento a su mascota", "form_entrenamiento")


        return is_valid
    
    @classmethod
    def save(cls, form,mascota):

        nuevo_form= {'tuvo_entrenamiento': form['tuvo_entrenamiento'],
                    'motivo_entrenamiento': form['motivo_entrenamiento'], 
                    'mascota_id': mascota,                     
                    }
        
        query = "INSERT INTO entrenamientos (tuvo_entrenamiento, motivo_entrenamiento,mascota_id) VALUES (%(tuvo_entrenamiento)s, %(motivo_entrenamiento)s,%(mascota_id)s)"
        result = connectToMySQL('esquema_etologia').query_db(query, nuevo_form) #como respuesta me traerá el ID del registro que se acaba de crear 
        return result
        
    @classmethod
    def update(cls, form):
        query = "UPDATE entrenamientos SET tuvo_entrenamiento=%(tuvo_entrenamiento)s, motivo_entrenamiento=%(motivo_entrenamiento)s WHERE mascota_id=%(mascota_id)s" 
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls,form):
        query = "DELETE FROM entrenamientos WHERE mascota_id = %(id)s"
        result = connectToMySQL('esquema_etologia').query_db(query, form)
        return result   