from flask import Flask, render_template, request, redirect, url_for, session
import stripe

# Initialize Flask App
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up Stripe keys (replace with your actual keys)
stripe.api_key = "sk_test_your_secret_key"
publishable_key = "pk_test_your_publishable_key"

# Dummy product data
products = [
    {"id": 1, "name": "Product 1", "price": 10.0},
    {"id": 2, "name": "Product 2", "price": 20.0},
    {"id": 3, "name": "Product 3", "price": 30.0}
]

# Home page route
@app.route('/')
def index():
    return render_template('index.html', products=products, key=publishable_key)

# Checkout route
@app.route('/checkout', methods=['POST'])
def checkout():
    # Get the product ID and price from the form
    product_id = int(request.form.get('product_id'))
    product = next(p for p in products if p['id'] == product_id)
    
    try:
        # Create a payment intent to be sent to Stripe
        intent = stripe.PaymentIntent.create(
            amount=int(product['price'] * 100),  # Amount in cents
            currency='usd',
            metadata={'product_name': product['name']}
        )
        return redirect(url_for('payment', intent_secret=intent.client_secret, product=product))
    except Exception as e:
        return str(e)

# Payment page route
@app.route('/payment')
def payment():
    intent_secret = request.args.get('intent_secret')
    product = request.args.get('product')
    return render_template('payment.html', secret=intent_secret, product=product)

# Handle successful payment
@app.route('/success')
def success():
    return render_template('success.html')

# Handle payment failure
@app.route('/failure')
def failure():
    return render_template('failure.html')

if __name__ == '__main__':
    app.run(debug=True)
