from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

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

DONATIONS_FILE = "static/db/donations.json"
VOLUNTEERS_FILE = "static/db/volunteers.json"

@app.route("/submit-donation", methods=["POST"])
def submit_donation():
    data = request.json

    if not data:
        return jsonify({"success": False, "message": "No data received"})

    data["timestamp"] = datetime.now().isoformat()

    os.makedirs("static/db", exist_ok=True)

    try:
        with open(DONATIONS_FILE, "r") as f:
            donations = json.load(f)
    except:
        donations = []

    donations.append(data)

    with open(DONATIONS_FILE, "w") as f:
        json.dump(donations, f, indent=4)

    print("New donation:", data)

    return jsonify({"success": True, "message": "Thank you! Your donation request has been recorded."})

@app.route("/submit-volunteer", methods=["POST"])
def submit_volunteer():
    data = request.json

    if not data:
        return jsonify({"success": False, "message": "No data received"})

    data["timestamp"] = datetime.now().isoformat()

    os.makedirs("static/db", exist_ok=True)

    try:
        with open(VOLUNTEERS_FILE, "r") as f:
            volunteers = json.load(f)
    except:
        volunteers = []

    volunteers.append(data)

    with open(VOLUNTEERS_FILE, "w") as f:
        json.dump(volunteers, f, indent=4)

    print("New volunteer:", data)

    return jsonify({"success": True, "message": "Your application has been submitted successfully!"})

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # Here you would typically save to database or send email
        print(f"Contact form submitted: {data}")
        return jsonify({'success': True, 'message': 'Thank you for your message!'})
    return render_template('contact.html')

NEWSLETTER_FILE = "static/db/newsletter.json"

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')

    if not email:
        return jsonify({'success': False, 'message': 'Please provide a valid email'})

    # Ensure directory exists
    os.makedirs(os.path.dirname(NEWSLETTER_FILE), exist_ok=True)

    # Load existing emails
    if os.path.exists(NEWSLETTER_FILE):
        try:
            with open(NEWSLETTER_FILE, 'r') as f:
                emails = json.load(f)
        except:
            emails = []
    else:
        emails = []

    # Prevent duplicates
    if email in emails:
        return jsonify({'success': False, 'message': 'This email is already subscribed!'})

    # Add new email
    emails.append(email)

    # Save back to file
    with open(NEWSLETTER_FILE, 'w') as f:
        json.dump(emails, f, indent=4)

    print(f"New subscription saved: {email}")

    return jsonify({'success': True, 'message': 'Thank you for subscribing!'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
