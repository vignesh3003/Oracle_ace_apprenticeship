#!/usr/bin/env python3
"""
Diagnostic Script: Test OCI Vision SDK Authentication & OCR Text Detection
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app.config import settings
from app.services.oci_vision import process_document_with_oci_vision

def main():
    print("=" * 60)
    print("OCI Vision AI Service Diagnostic Test")
    print("=" * 60)
    print(f"App Environment: {settings.APP_ENV}")
    print(f"Demo Mode: {settings.is_demo_mode}")
    print(f"OCI Config Path: {settings.OCI_CONFIG_FILE}")
    print(f"OCI Compartment ID: {settings.OCI_COMPARTMENT_ID}")
    print("-" * 60)

    sample_text = b"ORACLE CLOUD INFRASTRUCTURE VISION TEST DOCUMENT"
    text, conf, lines = process_document_with_oci_vision(sample_text, "test_doc.txt")

    print(f"Confidence Score: {conf}%")
    print(f"Extracted Lines Count: {len(lines)}")
    print("Extracted Text Preview:")
    print(text[:200])
    print("=" * 60)
    print("OCI Vision Test Execution Successful!")

if __name__ == "__main__":
    main()
