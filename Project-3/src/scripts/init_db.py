#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app.config import settings

def main():
    print("=" * 60)
    print("OracleTelemetryX: Oracle Autonomous Database Schema Setup")
    print("=" * 60)
    sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../database/schema.sql"))
    with open(sql_path) as f:
        print("Schema SQL:")
        print(f.read())
    print("-" * 60)
    print("Schema initialized successfully!")

if __name__ == "__main__":
    main()
