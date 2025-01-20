import logging
from flask import Blueprint, jsonify
from app.routes.product_routes import product_bp

# Initialize the main blueprint
main = Blueprint('main', __name__)

# Configure logging
def configure_logging():
    """
    Configures logging for the application.
    Logs can be customized using environment variables for flexibility.
    """
    logging.basicConfig(
        level=logging.INFO,  # Change to DEBUG or ERROR as needed
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    return logger

logger = configure_logging()

# Register blueprints
main.register_blueprint(product_bp)

# Example of adding logging in a route
@main.route('/example', methods=['GET'])
def example_route():
    """
    Example route to demonstrate logging.
    Logs a message each time this route is accessed.
    
    Returns:
        Response: A simple text response.
    """
    logger.info("Example route accessed")
    return jsonify({"message": "This is an example route."}), 200

# Global error handler (optional enhancement)
@main.errorhandler(Exception)
def handle_global_errors(error):
    """
    Handles uncaught exceptions and logs them.
    
    Args:
        error (Exception): The exception that occurred.

    Returns:
        Response: JSON response with error details.
    """
    logger.error(f"Unhandled Exception: {error}", exc_info=True)
    return jsonify({"error": "An internal error occurred."}), 500
