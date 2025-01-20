# tests/e2e/teardown.py
def stop_backend(process):
    """Stop the backend service."""
    process.terminate()
    process.wait()
