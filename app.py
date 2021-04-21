import numpy as np
from flask import Flask, request, jsonify, render_template
from model import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    customer_id = [int(x) for x in request.form.values()]
    prediction = rec_items(customer_id, product_train, user_vecs, item_vecs, customers_arr, products_arr, item_lookup, num_items=3)
    plist = prediction['Product_Name'].to_list()
    output1 = plist[0]
    output2 = plist[1]
    output3 = plist[2]

    purchases = get_items_purchased(customer_id, product_train, customers_arr, products_arr, item_lookup)
    purchaselist = purchases['data_subscriptions'].to_list()
    purchasehistory1 = purchaselist[0]
    purchasehistory2 = purchaselist[1]
    purchasehistory3 = purchaselist[2]


    return render_template('index.html',
                           prediction_text1='1.  {} '.format(output1),
                           prediction_text2='2.  {} '.format(output2),
                           prediction_text3='3.  {} '.format(output3),
                           purchase_text1='1.  {} '.format(purchasehistory1),
                           purchase_text2='2.  {} '.format(purchasehistory2),
                           purchase_text3='3.  {} '.format(purchasehistory3),
                           )



if __name__ == "__main__":
    app.run(debug=True)