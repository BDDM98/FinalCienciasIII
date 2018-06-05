"""Generador de código con DSL
Bryan David Durán 20152020801
José Alejandro González 20152020105
"""
from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
this_folder = dirname(__file__)
class SimpleType(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
    def __str__(self):
        return self.name
def get_entity_mm(debug=False):
    """
    Construye y genera un modelo de datos Entity.
    """
    #Lo construye como el SimpleType declarado arriba.
    #Cada modelo tendrá sus tipos simples pero no harán parte del EntityModel.
    type_builtins = {
            'integer': SimpleType(None, 'integer'),
            'string': SimpleType(None, 'string'),
            'booleano': SimpleType(None, 'booleano')
    }
    entity_mm = metamodel_from_file(join(this_folder, 'entidad.tx'),
                                    classes=[SimpleType],
                                    builtins=type_builtins,
                                    debug=debug)
    return entity_mm
def main(debug=False):

    entity_mm = get_entity_mm(debug)

    #Exporta el archivo .dot para visualizarlo.
    dot_folder = join(this_folder, 'diagramas')
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)
    metamodel_export(entity_mm, join(dot_folder, 'entidades.dot'))

    #Se construye un modelo person del archivo almacen.ent.
    person_model = entity_mm.model_from_file(join(this_folder, 'almacen.ent'))

    #Exporta el archivo .dot para visualizarlo.
    model_export(person_model, join(dot_folder, 'almacen.dot'))
if __name__ == "__main__":
    main()
