import pandas as pd
from django.conf import settings
import os
import sys
import django

# Agrega la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba.settings')
django.setup()
from app_inventario.models import inventario, marca, categoria, estado


def cargar_desde_modelo(model, db_alias):
    """
    Carga todos los registros del modelo especificado usando la base de datos indicada,
    y devuelve un DataFrame con los datos.
    """
    qs = model.objects.using(db_alias).all()
    data = list(qs.values())
    df = pd.DataFrame(data)
    return df

# Bases configuradas en settings.py
bases = ['default', 'mysql', 'postgresql']

# Modelos a cargar
modelos = {
    'inventario': inventario,
    'marca': marca,
    'categoria': categoria,
    'estado': estado
}

# Diccionario para guardar los dataframes por tabla y base de datos
datos = {modelo: {} for modelo in modelos.keys()}

# Cargar los datos
for nombre_modelo, modelo in modelos.items():
    for base in bases:
        df = cargar_desde_modelo(modelo, base)
        datos[nombre_modelo][base] = df
        print(f"Desde {base} - {nombre_modelo}:")
        print(df.head())

# Si quieres concatenar datos de todas las bases para cada modelo:
datos_concatenados = {}
for nombre_modelo in modelos.keys():
    dfs = [datos[nombre_modelo][base] for base in bases]
    df_concat = pd.concat(dfs, ignore_index=True)
    datos_concatenados[nombre_modelo] = df_concat
    print(f"\nDatos concatenados de {nombre_modelo}:")
    print(df_concat.head())
