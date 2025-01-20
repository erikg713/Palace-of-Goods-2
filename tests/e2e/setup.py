# tests/e2e/setup.py
import subprocess

def start_backend():
    """Start the backend service for E2E tests."""
    process = subprocess.Popen(["flask", "run"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process
