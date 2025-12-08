from flask import Flask, render_template, request, jsonify
import os 
from config import config 


app = Flask(__name__)

# Load configuration
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Create upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/getinvolved')
def get_involved():
    return render_template('getinvolved.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # Here i would typically save to database or send email
        print(f"Contact form submitted: {data}")
        return jsonify({'success': True, 'message': 'Thank you for your message!'})
    return render_template('contact.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        # Here i would typically save to database
        print(f"New subscription: {email}")
        return jsonify({'success': True, 'message': 'Thank you for subscribing!'})
    return jsonify({'success': False, 'message': 'Please provide a valid email'})

if __name__ == '__main__':
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=app.config['DEBUG']
    )