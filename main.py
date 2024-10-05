from flask import Flask, render_template, request
import image_editor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
@app.route('/image', methods=['POST'])
def upload_image():
    try:
        try:
            image = request.files['image']
        except:
            return "missing image"
        
        text = request.form.get('text')
        xCoordinate = request.form.get('xCoordinates')
        yCoordinate = request.form.get('yCoordinates')
        color = request.form.get('color')
        color = hex_to_rgb(color)
        fontSize = request.form.get('fontSize')
    except Exception as e:
        return "missing some parameters"

    save_name = image_editor.write_text_on_image(image, text, int(fontSize), (int(xCoordinate), int(yCoordinate)), color, "output.jpg")
    return render_template('result.html', result=save_name)


if __name__ == '__main__':
    app.run(debug=True)