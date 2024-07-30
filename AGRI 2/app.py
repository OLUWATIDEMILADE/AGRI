from flask import Flask, redirect, render_template, request
import stripe

app = Flask(__name__, template_folder='template', static_folder='static')

stripe.api_key = 'sk_test_51PiErIIwtgt7YZ8O5gwZNNfk1Jz4qY4fuj9QEVxUEQ6vWLDAmtttYYgb6Y9qRk0SSBWKAoT2XkSVi7KgHnn2WHk500tePpoHUl'



YOUR_DOMAIN = 'http://127.0.0.1:5000'




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/cart')
def cart():
    return render_template('cart.html')



@app.route('/payment', methods=['POST'])
def payment():
    items = request.form.getlist('items')
    quantities = request.form.getlist('quantities')


    line_items = []
    for item, quantity in zip(items, quantities):
        line_items.append({
            'price': item,
            'quantity': int(quantity)
        })

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url= YOUR_DOMAIN + '/success.html',
            cancel_url=  YOUR_DOMAIN + '/cancel.html'
        )
        
    except Exception as e:
        return str(e)
    

    return redirect(checkout_session.url, code=303)





if __name__ == '__main__':
    app.run(debug=True)