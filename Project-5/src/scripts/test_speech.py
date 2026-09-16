#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app.core.oci_speech import process_audio_transcription

def main():
    print("OCI Speech AI Diagnostic Test")
    t, c, j = process_audio_transcription("sample_audio.mp3", b"test_audio_bytes")
    print("Transcript:", t)
    print("Confidence:", c)
    print("Job OCID:", j)

if __name__ == "__main__":
    main()
