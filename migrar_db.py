"""
Script de migración para agregar columnas es_profesor y genero
"""
import sqlite3
import os

db_path = 'instance/berakah.db'

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Agregar columna es_profesor
        cursor.execute("ALTER TABLE usuario ADD COLUMN es_profesor BOOLEAN DEFAULT 0")
        print("✅ Columna 'es_profesor' agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print("ℹ️ Columna 'es_profesor' ya existe")
        else:
            print(f"❌ Error: {e}")
    
    try:
        # Agregar columna genero
        cursor.execute("ALTER TABLE usuario ADD COLUMN genero VARCHAR(10)")
        print("✅ Columna 'genero' agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e):
            print("ℹ️ Columna 'genero' ya existe")
        else:
            print(f"❌ Error: {e}")
    
    conn.commit()
    conn.close()
    print("\n✅ Migración completada exitosamente")
else:
    print("❌ No se encontró la base de datos en instance/berakah.db")
