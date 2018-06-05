"""Generador de código con DSL
Bryan David Durán 20152020801
José Alejandro González 20152020105
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from generadorDOT import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    #Se construye un modelo person del archivo almacen.ent.
    person_model = entity_mm.model_from_file(join(this_folder, 'almacen.ent'))

    def is_entity(n):
        """
        Prueba para saber si es un tipo de entidad.
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    def javatype(s):
        """
        Estructuras para los tipos de nombres de un tipo primitivo a python.
        """
        return {
                'integer': 'int',
                'string': 'String',
                'booleano':'booleano'
        }.get(s.name, s.name)

    #Se crea una carpeta de salida.
    srcgen_folder = join(this_folder, 'codigoGenerado')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    #Se inicializa el motor de plantillas.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    #Se filtra para convertir los tipos de la entidad en tipos de Python.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javatype'] = javatype

    #Se carga la plantilla
    template = jinja_env.get_template('python.template')

    for entity in person_model.entities:
        #Para cada entidad creada se crea el archivo .py.
        #Direccion.py
        #Persona.py
        #Telefono.py
        with open(join(srcgen_folder,"%s.py" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))


if __name__ == "__main__":
    main()
