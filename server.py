from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    data = request.form
    added_numbers = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])

    return render_template("checkout.html", data=data, added_numbers=added_numbers)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    