#!/usr/bin/env python3
"""
Diagnostic Script: Test OCI Generative AI SDK Chat Inference
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app.core.oci_genai import generate_llm_response
from app.config import settings

def main():
    print("=" * 60)
    print("OCI Generative AI Service Diagnostic Test")
    print("=" * 60)
    print(f"GenAI Endpoint: {settings.OCI_GENAI_ENDPOINT}")
    print(f"GenAI Model ID: {settings.OCI_GENAI_MODEL_ID}")
    print(f"Demo Mode: {settings.is_demo_mode}")
    print("-" * 60)

    prompt = "Explain enterprise security controls in OCI Generative AI Service."
    ans, model, latency = generate_llm_response(prompt)

    print(f"Model: {model}")
    print(f"Latency: {latency} ms")
    print("Response Output:")
    print(ans)
    print("=" * 60)

if __name__ == "__main__":
    main()
