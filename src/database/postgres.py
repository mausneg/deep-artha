from sqlalchemy import create_engine, text
from typing import Any

from consts import DB_URL

class PostgresDatabase:
    def __init__(self):
        self._engine = create_engine(DB_URL)

    def get_table_names(self)-> list[str]:
        try:
            with  self._engine.connect() as conn:
                cursor_result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
                table_names = [result[0] for result in cursor_result.fetchall()]
                return table_names
            
        except Exception as e:
            print(e)

    def get_table_schema(self, table_name: str)-> str:
        try:
            with self._engine.connect() as conn:
                cursor_result = conn.execute(text(f"""
                    SELECT column_name, data_type, is_nullable, column_default 
                    FROM information_schema.columns 
                    WHERE table_name = '{table_name}' 
                    ORDER BY ordinal_position;
                """))
                columns = cursor_result.fetchall()
                
                schema_lines = [f"{col[0]} {col[1]} {'NOT NULL' if col[2] == 'NO' else 'NULL'}" for col in columns]
                schema = "CREATE TABLE " + table_name + " (\n  " + ",\n  ".join(schema_lines) + "\n);"
                
                cursor_result = conn.execute(text(f"SELECT * FROM {table_name} LIMIT 3"))
                column_names = cursor_result.keys()
                records = cursor_result.fetchall()
                
                sample_data = "\t".join(column_names)
                for record in records:
                    record = "\t".join([str(cell) for cell in list(record)])
                    sample_data = sample_data + "\n" + record 
                
                schema = f"### TABLE {table_name} DDL\n{schema}\n\n### SAMPLE DATA\n{sample_data}"
                
                return schema
        except Exception as e:
            print(f"Error: {e}")
            
    def execute(self, query: str)-> Any:
        try:
            with self._engine.connect() as conn:
                cursor_result = conn.execute(text(query))
                column_names = cursor_result.keys()
                records = cursor_result.fetchall()
                
                results = "\t".join(column_names)
                for record in records:
                    record = "\t".join([str(cell) for cell in list(record)])
                    results = results + "\n" + record
                return results
            
        except Exception as e:
            print(f"Error: {e}")
                   