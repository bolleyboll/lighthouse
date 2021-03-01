from light import app


@app.route('/')
def home():
    return "Welcome to the App"


@app.route('/lon')
def light_on():
    return "Lights On! :)"


@app.route('/loff')
def light_off():
    return "Lights Off! :("
