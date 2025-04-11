from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Modelo para los datos
class SugarData(BaseModel):
    country: str
    year: int
    sugar_consumption: float

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect("database/sugar_data.db")  # Cambia la ruta si usas otra base de datos
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para obtener datos
@app.get("/data", response_model=List[SugarData])
def read_data():
    conn = get_db_connection()
    cursor = conn.execute("SELECT country, year, sugar_consumption FROM sugar_consumption")
    data = cursor.fetchall()
    conn.close()
    return [dict(row) for row in data]

# Endpoint para agregar datos
@app.post("/data")
def add_data(data: SugarData):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO sugar_consumption (country, year, sugar_consumption) VALUES (?, ?, ?)",
        (data.country, data.year, data.sugar_consumption),
    )
    conn.commit()
    conn.close()
    return {"message": "Data added successfully"}
