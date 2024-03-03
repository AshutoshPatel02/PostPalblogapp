from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

blogs = []


@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)


@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.json
    blogs.append(data)
    return jsonify({"message": "Blog created successfully."})


@app.route('/blogs/<int:index>', methods=['PUT'])
def update_blog(index):
    data = request.json
    blogs[index] = data
    return jsonify({"message": "Blog updated successfully."})


@app.route('/blogs/<int:index>', methods=['DELETE'])
def delete_blog(index):
    del blogs[index]
    return jsonify({"message": "Blog deleted successfully."})


if __name__ == '__main__':
    app.run(debug=True)
