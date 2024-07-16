from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def calculate_loan_details (amount, annual_rate, years):
    monthly_rate = annual_rate/100/12
    installments = years * 12
    if monthly_rate == 0:
        #return amount / installments
        monthly_payment = amount / installments
    else:
        #return amount *monthly_rate / (1  (1 + monthly_rate)** -installments)
        monthly_payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -installments)
        
    total_payment = monthly_payment * installments
    total_interest = total_payment - amount
    
    return {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'total_payment': total_payment
    }

@app.route('/')
def index():
    return render_template ('index1.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    amount = float(data['amount'])
    annual_rate = float(data['annual_rate'])
    years = int(data['years'])
    loan_details = calculate_loan_details(amount,annual_rate,years)
    return jsonify(loan_details)

if __name__ == '__main__':
    app.run(debug=True)