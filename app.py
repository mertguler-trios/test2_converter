from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    # conv_choice declared for further use in result page
    global conv_choice
    
    if request.method == "POST":
        conv_choice = request.form["convertor-choice"]
        if conv_choice == '1':
            return redirect("/weights")
        elif conv_choice == '2':
            return redirect("/distance")
        elif conv_choice == '3':
            return redirect("/temperature")
    else:
        return render_template('index.html')


@app.route('/weights', methods=['POST','GET'])
def weight():
    return render_template('weight-conversion.html')


@app.route('/distance', methods=['POST','GET'])
def distance():
    return render_template('distance-conversion.html')


@app.route('/temperature', methods=['POST','GET'])
def temperature():
    return render_template('temperature-conversion.html')


@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == "POST":

        if conv_choice == '1':
            # Weight calculation
            weight_pounds = request.form["weight-input"]
            weight_pounds = float(weight_pounds)
            weight_kg = weight_pounds * 0.45359237
            return render_template('result.html',weight_kg=weight_kg,weight_pounds=weight_pounds,conv_choice=conv_choice)

        elif conv_choice == '2':
            # Distance calculation
            distance_miles = request.form["distance-input"]
            distance_miles = float(distance_miles)
            distance_km = distance_miles * 1.609344
            return render_template('result.html',distance_km=distance_km,distance_miles=distance_miles,conv_choice=conv_choice)
    
        elif conv_choice == '3':
            # Temperature calculation
            temperature_fahrenheit = request.form["temperature-input"]
            temperature_fahrenheit = float(temperature_fahrenheit)
            temperature_celsius = (temperature_fahrenheit - 32) * 0.5556
            return render_template('result.html',temperature_celsius=temperature_celsius,temperature_fahrenheit=temperature_fahrenheit,conv_choice=conv_choice)
    else:
        pass
        
    
    

if __name__ == "__main__":
    app.run(debug=True)
