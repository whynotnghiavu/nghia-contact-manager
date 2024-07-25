from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Cấu hình Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Đường dẫn đến tệp swagger.json

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Swagger API"}
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/api/hello', methods=['GET'])
def hello():
    """
    Đoạn mô tả cho endpoint này.
    ---
    responses:
      200:
        description: Trả về một thông điệp chào.
    """
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
