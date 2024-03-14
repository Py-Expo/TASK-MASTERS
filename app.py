

from flask import Flask, render_template, request, jsonify
from tax_calculator import IndianTaxCalculator  

app = Flask(__name__)

tax_calculator = IndianTaxCalculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data['message']
        
        # Check if the user's message contains an income value
        if "income" in user_message.lower():
            # Extract the income value from the user's message
            income = float(user_message.split()[-1])
            
            # Calculate tax using IndianTaxCalculator
            tax_amount, remaining_amount = tax_calculator.calculate_tax(income)
            
            # Get recommendations based on tax and income
            recommendations = tax_calculator.get_recommendations(income, tax_amount)
            
            # Format the response
            response = f"Tax Amount: ₹{tax_amount:.2f}, Remaining Amount: ₹{remaining_amount:.2f}, {recommendations}"
        else:
            # Add some manual responses based on specific user messages
            if any(word in user_message.lower() for word in ["hello", "hey", "hi"]):
                response = "Hello! Enter your annual income withnthe keyword income"
            elif "thank you" in user_message.lower():
                response = "You're welcome!"
            else:
                response = "I'm sorry, I didn't understand that. Please provide your income for tax calculation."

        return jsonify({'response': response})

    except ValueError as e:
        return jsonify({'response': str(e)}), 400
    except Exception as e:
        return jsonify({'response': 'An unexpected error occurred. Please try again.'}), 500

if __name__ == "__main__":
    app.run(debug=True)
