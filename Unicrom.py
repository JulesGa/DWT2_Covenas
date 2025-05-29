import pandas as pd
import unicodedata
import re
from rapidfuzz import fuzz

# Función para normalizar texto
def normalizar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Función para agrupar direcciones similares y asignar guía por grupo
def agrupar_direcciones_similares(df, col_cliente, col_direccion, umbral=60):
    df['direccion_normalizada'] = df[col_direccion].apply(normalizar_texto)
    direccion_guia_col = []

    for cliente, grupo in df.groupby(col_cliente):
        grupo = grupo.copy()
        grupo['grupo'] = -1  # Inicialmente sin asignar grupo
        grupo_idx = grupo.index.tolist()
        grupo_counter = 0

        for idx in grupo_idx:
            if grupo.at[idx, 'grupo'] != -1:
                continue  # Ya está asignado a un grupo
            grupo.at[idx, 'grupo'] = grupo_counter
            base_normalizada = grupo.at[idx, 'direccion_normalizada']
            for jdx in grupo_idx:
                if idx == jdx or grupo.at[jdx, 'grupo'] != -1:
                    continue
                comparada = grupo.at[jdx, 'direccion_normalizada']
                similitud = fuzz.ratio(base_normalizada, comparada)
                if similitud >= umbral:
                    grupo.at[jdx, 'grupo'] = grupo_counter
            grupo_counter += 1

        # Para cada grupo de direcciones similares, obtener la más larga
        for g, subgrupo in grupo.groupby('grupo'):
            idx_guia = subgrupo[col_direccion].str.len().idxmax()
            direccion_guia = df.loc[idx_guia, col_direccion]
            for idx in subgrupo.index:
                direccion_guia_col.append((idx, direccion_guia))

    # Asignamos la columna de dirección guía
    direccion_guia_final = pd.Series(index=df.index, dtype=str)
    for idx, direccion in direccion_guia_col:
        direccion_guia_final.at[idx] = direccion

    df['direccion_guia'] = direccion_guia_final
    df.drop(columns='direccion_normalizada', inplace=True)
    return df

# === Configuración ===
archivo_entrada = 'clientes_direcciones.xlsx'
archivo_salida = 'clientes_direcciones_con_grupos.xlsx'
columna_cliente = 'CLIENTE'
columna_direccion = 'DIRECCIONES'
umbral_similitud = 60

# === Ejecución ===
df = pd.read_excel(archivo_entrada)
df_resultado = agrupar_direcciones_similares(df, columna_cliente, columna_direccion, umbral_similitud)
df_resultado.to_excel(archivo_salida, index=False)

print(f'Archivo exportado correctamente a: {archivo_salida}')