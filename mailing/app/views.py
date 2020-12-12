from main import app, send

@app.route('/')
def index():
    return '<h4>Welcome to async mailing</h4>'
    
@app.route('/<user>')
def send_pdf(user):
    # global result = send.delay(user)
    send.delay(user)
    return 'Your mail will be sent.'
