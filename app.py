import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    app.logger.info("Homepage endpoint invoked")
    return jsonify(
        message="Welcome to My Page, Greetings by Hamza",
        platform="GitHub Actions",
        runtime="Docker + Flask",
    )


@app.get("/health")
def health():
    app.logger.info("Health check endpoint invoked")
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.logger.info("Starting Flask application")

    app.run(
        host="0.0.0.0",  # nosec B104 - required for Docker networking
        port=int(os.getenv("PORT", "5000")),
    )
