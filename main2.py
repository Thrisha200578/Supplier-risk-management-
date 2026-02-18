# =============================================================================
# main.py — Flask Authentication Backend
# Project: Role-Based Login System
# Description: Authenticates users from login.html and redirects them to
#              their respective role-based dashboards.
# =============================================================================

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os


HTML_FOLDER = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# App Initialization
# ---------------------------------------------------------------------------
app = Flask(__name__, static_folder=".")
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend communication


@app.route("/")

def index():

    return send_from_directory(".", "login.html")

@app.route("/<path:filename>")

def serve_static(filename):

    return send_from_directory(".", filename)
# ---------------------------------------------------------------------------
# Hardcoded Demo Users
# Format: "email": { "password": ..., "role": ..., "redirect": ... }
# ---------------------------------------------------------------------------
USERS = {
    "admin@platform.com": {
        "password": "admin123",
        "role": "admin",
        "redirect": "/admin1.html"
    },
    "seller@test.com": {
        "password": "seller123",
        "role": "seller",
        "redirect": "/seller.html"
    },
    "manufacturer@test.com": {
        "password": "manu123",
        "role": "manufacturer",
        "redirect": "/manu1.html"
    }
}

# ---------------------------------------------------------------------------
# Helper: Input Validation
# ---------------------------------------------------------------------------
def validate_login_input(data):
    """
    Validates that the request body contains non-empty email and password fields.
    Returns (True, None) if valid, or (False, error_message) if invalid.
    """
    if not data:
        return False, "Request body is missing or not JSON."
    
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()

    if not email:
        return False, "Email is required."
    if not password:
        return False, "Password is required."
    if "@" not in email:
        return False, "Invalid email format."

    return True, None

# ---------------------------------------------------------------------------
# Route: Serve login.html (optional convenience — works if files are co-located)
# ---------------------------------------------------------------------------
@app.route("/")
def serve_login():
    """Serve the login.html frontend from the same directory."""
    return send_from_directory(".", "login.html")

# ---------------------------------------------------------------------------
# Route: POST /login — Core Authentication Endpoint
# ---------------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON credentials, validates them, and returns a role-based
    redirect URL on success, or an error message on failure.

    Expected Request Body:
        { "email": "user@example.com", "password": "secret" }

    Success Response:
        { "status": "success", "role": "admin", "redirect": "/admin-dashboard.html" }

    Failure Response:
        { "status": "error", "message": "Invalid email or password" }
    """

    # Step 1: Parse JSON body
    data = request.get_json(silent=True)

    # Step 2: Validate input fields
    is_valid, validation_error = validate_login_input(data)
    if not is_valid:
        return jsonify({
            "status": "error",
            "message": validation_error
        }), 400

    email = data["email"].strip().lower()
    password = data["password"].strip()

    # Step 3: Look up user by email
    user = USERS.get(email)

    # Step 4: Check if user exists and password matches
    if user and user["password"] == password:
        return jsonify({
            "status": "success",
            "role": user["role"],
            "redirect": user["redirect"]
        }), 200

    # Step 5: Return generic error (avoid leaking which field was wrong)
    return jsonify({
        "status": "error",
        "message": "Invalid email or password."
    }), 401

# ---------------------------------------------------------------------------
# Route: Catch-All for undefined routes
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "message": "Endpoint not found."}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"status": "error", "message": "Method not allowed."}), 405
# ---------------------------------------------------------------------------
# Route: Serve frontend files from the same directory
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True enables auto-reload during development.
    # Set debug=False and use a WSGI server (e.g. gunicorn) in production.
    app.run(debug=True, host="0.0.0.0", port=5000)