from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def process_payment():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Bad Request",
                "message": "No se envió JSON"
            }), 400

        amount = data.get('amount')
        method = data.get('method')

        if not amount or not method:
            return jsonify({
                "error": "Bad Request",
                "message": "Faltan campos requeridos"
            }), 400

        return jsonify({
            "status": "success",
            "message": "Pago procesado correctamente",
            "data": {
                "amount": amount,
                "method": method
            }
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)