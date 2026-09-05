#!/usr/bin/env python3
"""
Oracle Database 23ai Table Initializer
Executes DDL schema statements to create VECTOR tables in Oracle Autonomous DB.
"""
import os
import sys

# Add backend directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("init_db")

def run_schema():
    sql_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../database/schema_23ai.sql"))
    if not os.path.exists(sql_file):
        logger.error(f"Schema file not found at {sql_file}")
        return

    logger.info(f"Reading DDL from {sql_file}...")
    with open(sql_file, "r") as f:
        sql_content = f.read()

    if settings.is_demo_mode:
        logger.info("APP_ENV=development (Demo Mode). Skipping physical database execution.")
        logger.info("Demo database tables are initialized automatically in-memory.")
        return

    try:
        import oracledb
        logger.info(f"Connecting to Oracle Autonomous Database 23ai DSN: {settings.ORACLE_DB_DSN}...")
        conn = oracledb.connect(
            user=settings.ORACLE_DB_USER,
            password=settings.ORACLE_DB_PASSWORD,
            dsn=settings.ORACLE_DB_DSN
        )
        cursor = conn.cursor()

        statements = [s.strip() for s in sql_content.split(";") if s.strip() and not s.strip().startswith("--")]
        for stmt in statements:
            if stmt.upper() == "COMMIT":
                continue
            logger.info(f"Executing: {stmt[:60]}...")
            try:
                cursor.execute(stmt)
            except Exception as se:
                logger.warning(f"Statement notice: {se}")

        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Oracle Autonomous Database 23ai schema initialization complete!")

    except Exception as e:
        logger.error(f"Database connection error: {e}")

if __name__ == "__main__":
    run_schema()
