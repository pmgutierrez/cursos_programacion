import sqlite3
import re

def convertir_pg_a_sqlite(input_file, output_file):
    print(f"Leyendo {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    # 1. Eliminar comandos específicos de PostgreSQL que SQLite no entiende
    # SET statements, comentarios de dump, etc.
    lines = sql_content.split('\n')
    clean_lines = []
    
    for line in lines:
        # Ignorar líneas que empiezan con SET, DROP TABLE IF EXISTS (lo manejaremos manual si hace falta), 
        # o comentarios de cabecera de PG
        upper_line = line.strip().upper()
        if upper_line.startswith("SET ") or \
           upper_line.startswith("--") and "PostgreSQL database dump" in line:
            continue
        
        # SQLite no usa 'DROP TABLE IF EXISTS' de la misma forma segura con dependencias, 
        # pero para una creación nueva está bien. Sin embargo, el script original tira las tablas al inicio.
        # Vamos a filtrar los DROP TABLE para evitar errores si la DB ya existe vacía, 
        # o simplemente dejarlos si creamos la DB desde cero.
        # Para simplificar, dejaremos los CREATE e INSERT.
        
        clean_lines.append(line)

    clean_sql = '\n'.join(clean_lines)

    # 2. Reemplazar tipos de datos incompatibles
    # PostgreSQL 'bytea' -> SQLite 'BLOB'
    clean_sql = clean_sql.replace('bytea', 'BLOB')
    
    # PostgreSQL 'character varying(n)' -> SQLite 'TEXT'
    # Usamos regex para cambiar character varying(15), varchar(40), etc.
    clean_sql = re.sub(r'character varying\(\d+\)', 'TEXT', clean_sql)
    clean_sql = re.sub(r'varchar\(\d+\)', 'TEXT', clean_sql)
    
    # PostgreSQL 'smallint' / 'integer' -> SQLite 'INTEGER' (SQLite es flexible, pero mejor estandarizar)
    # En realidad SQLite acepta smallint, pero INTEGER es más estándar.
    
    # 3. Manejo de comillas dobles vs simples
    # PostgreSQL usa a menudo "nombre_tabla". SQLite prefiere 'nombre_tabla' o nada.
    # Reemplazamos comillas dobles alrededor de identificadores por nada o comillas simples si es necesario.
    # Una forma segura es quitar las comillas dobles de los nombres de tablas/columnas
    clean_sql = clean_sql.replace('"', '') 

    # 4. Más limpiezas específicas de dumps de PostgreSQL
    # - Quitar sentencias ALTER TABLE ... ADD CONSTRAINT (SQLite maneja constraints diferente)
    # - Quitar comentarios de tipo COMMENT ON ...;
    # - Eliminar la palabra ONLY en ALTER TABLE ONLY ...
    # - Reemplazar literales de bytea '\x' por cadena vacía
    # - Asegurar que las referencias FOREIGN KEY que no especifican columnas sean eliminadas
    clean_sql = re.sub(r'ALTER TABLE[\s\S]*?;\n', '', clean_sql, flags=re.IGNORECASE)
    clean_sql = re.sub(r'COMMENT ON[\s\S]*?;\n', '', clean_sql, flags=re.IGNORECASE)
    clean_sql = re.sub(r'\bONLY\b\s+', '', clean_sql, flags=re.IGNORECASE)
    clean_sql = clean_sql.replace("'\\x'", "''")
    # Eliminar líneas que añaden constraints o referencias sin especificar columnas
    clean_sql = re.sub(r"ADD CONSTRAINT[\s\S]*?;\n", '', clean_sql, flags=re.IGNORECASE)
    clean_sql = re.sub(r"REFERENCES\s+\w+\s*;", '', clean_sql, flags=re.IGNORECASE)

    print("Conectando a SQLite y creando base de datos...")
    
    try:
        conn = sqlite3.connect(output_file)
        cursor = conn.cursor()
        
        # Habilitar foreign keys (opcional, pero recomendado)
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # Ejecutar el script limpio
        # Nota: executescript puede tener problemas con transacciones grandes si hay errores.
        # Usamos executescript para permitir múltiples statements.
        cursor.executescript(clean_sql)
        
        conn.commit()
        print(f"¡Éxito! Base de datos creada en: {output_file}")
        
        # Verificación rápida
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tablas creadas: {[t[0] for t in tables]}")
        
        # Verificar cantidad de clientes
        cursor.execute("SELECT count(*) FROM customers;")
        count = cursor.fetchone()[0]
        print(f"Clientes importados: {count}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
            if conn:
                conn.close()

# Rutas de los archivos
# Asegúrate de que northwind.sql esté en la misma carpeta o pon la ruta completa
input_file = 'northwind.sql'
output_file = 'northwind.db'

if __name__ == "__main__":
    convertir_pg_a_sqlite(input_file, output_file)