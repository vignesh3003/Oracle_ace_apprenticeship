#!/usr/bin/env python3
"""
Diagnostic Script: Test OCI Notification Service (ONS) Alert Publishing
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app.engine.oci_ons import publish_ons_alert
from app.config import settings

def main():
    print("=" * 60)
    print("OCI Notification Service (ONS) Diagnostic Test")
    print("=" * 60)
    print(f"Topic OCID: {settings.OCI_ONS_TOPIC_OCID}")
    print(f"Demo Mode: {settings.is_demo_mode}")
    print("-" * 60)

    res = publish_ons_alert(
        subject="TEST ALERT: OCI ONS Notification Pipeline Verification",
        message_body="This is an automated diagnostic test message from OracleTelemetryX verifying active ONS subscription delivery."
    )
    print(f"ONS Notification Delivery Status: {res}")
    print("=" * 60)

if __name__ == "__main__":
    main()
