#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app.core.oci_vault import audit_security_compliance

def main():
    print("OCI Vault & Security Diagnostic Scan Test")
    findings = audit_security_compliance()
    print("Findings:", findings)

if __name__ == "__main__":
    main()
