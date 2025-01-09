from flask import Flask, jsonify
import requests

app = Flask(__name__)
def check_external_service():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return response.status_code == 200
    except:
        return False

@app.route('/health', methods=['GET'])
def health_check():
    api_status = check_external_service()

    return jsonify({
        'external_api': 'up' if api_status else 'down'
    })

if __name__ == "__main__":
    app.run(debug=True)