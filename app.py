from flask import Flask, request

app = Flask(__name__)

@app.route('/styleTransfer', methods=['POST'])
def style_transfer():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400
    image = request.files['image']
    # Process the image...
    return {"message": "Image processed successfully"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
