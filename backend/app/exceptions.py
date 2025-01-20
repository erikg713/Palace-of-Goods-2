# backend/app/exceptions.py

class AppError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class ProductNotFoundError(AppError):
    def __init__(self):
        super().__init__("Product not found", 404)
