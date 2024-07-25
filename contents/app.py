from flask import Flask, request, jsonify

app = Flask(__name__)

# Giả lập cơ sở dữ liệu bằng một từ điển
vcards = {}

@app.route('/vcards', methods=['POST'])
def create_vcard():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    
    if id in vcards:
        return jsonify({'message': 'VCard already exists'}), 400
    
    vcards[id] = name
    return jsonify({'id': id, 'name': name}), 201

@app.route('/vcards/<id>', methods=['GET'])
def read_vcard(id):
    name = vcards.get(id)
    if not name:
        return jsonify({'message': 'VCard not found'}), 404
    
    return jsonify({'id': id, 'name': name})

@app.route('/vcards/<id>', methods=['PUT'])
def update_vcard(id):
    data = request.get_json()
    name = data.get('name')
    
    if id not in vcards:
        return jsonify({'message': 'VCard not found'}), 404
    
    vcards[id] = name
    return jsonify({'id': id, 'name': name})

@app.route('/vcards/<id>', methods=['DELETE'])
def delete_vcard(id):
    if id not in vcards:
        return jsonify({'message': 'VCard not found'}), 404
    
    del vcards[id]
    return jsonify({'message': 'VCard deleted'})

if __name__ == '__main__':
    app.run(debug=True)
