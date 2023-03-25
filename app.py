import json
import pandas as pd


from flask import Flask, render_template, request
import joblib


app= Flask(__name__, template_folder="template")

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    job = request.form['job']
   
    balance = int(request.form['balance'])
    education = request.form['education']
    duration = int(request.form["duration"])
    default = request.form['default']
    housing = request.form['housing']
    loan = request.form['loan']
    contact = request.form['contact']
    month = request.form['month']
    day= request.form['day']
    marital = request.form['marital']
    campaign = int(request.form['campaign'])
    pdays = int(request.form['pdays'])
    previous = int(request.form['previous'])
    poutcome= request.form['poutcome']
    """
    new_data = pd.DataFrame({
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'balance': [balance],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'day': [day],
        'month': [month],
        'duration':[duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'poutcome': [poutcome] })"""
    

    # convert categorical varibles to one hot encoding
    job_admin=job_blue_collar= job_entrepreneur=job_housemaid= job_management= job_retired= job_self_employed=job_services= job_student=job_technician=job_unemployed=job_unknown = 0

    if job == "admin":
        job_admin =1
    elif job == "blue-collar":
        job_blue_collar=1
    elif job== 'entrepreneur' :
         job_entrepreneur= 1
    elif job == 'housemaid':
        job_housemaid=1
    elif job == 'management':
        job_management=1
    elif job == "retired":
        job_retired =1
    elif job == "self-employed":
        job_self_employed=1
    elif job== 'services':
        job_services=1
    elif job == 'student':
        job_student =1
    elif job== 'technician':
        job_technician =1
    elif job == 'unemployed':
        job_unemployed=1
    elif job == 'unknown':
        job_unknown =1

    marital_divorced=marital_single=marital_married=0

    if marital =="single":
        marital_single=1
    elif marital== "married":
        marital_married =1
    elif marital == "divorced" :
        marital_divorced=1

    education_primary=education_secondary=education_tertiary= education_unknown=0

    if education== "primary":
        education_primary=1
    elif education == "secondary":
        education_secondary=1
    elif education == "tertiary":
        education_tertiary=1
    elif education == "unknown":
        education_unknown=1

    default_no=default_yes=0
    if default == 'no':
        default_no=1
    elif default == 'yes':
        default_yes =1

    loan_no=loan_yes=0
    if loan == 'no':
        loan_no=1
    elif default == 'yes':
        loan_yes =1

    housing_no=housing_yes=0
    if housing == 'no':
        housing_no=1
    elif housing == 'yes':
        housing_yes =1

    contact_cellular=contact_telephone=contact_unknown=0
    if contact == 'cellular':
        contact_cellular=1
    elif contact == 'telephone' :
        contact_telephone =1
    elif contact == " unknown":
        contact_unknown =1
    

    month_apr=month_aug=month_dec=month_feb=month_jan=month_jul=month_jun=month_mar=month_may=month_nov=month_oct=month_sep=0
    if month == 'jan':
        month_jan =1
    elif month == 'feb':
        month_feb =1
    elif month == 'mar':
        month_mar =1
    elif month == 'apr':
        month_apr =1
    elif month == 'may':
        month_may = 1
    elif month == 'jun':
        month_jun =1
    elif month == "jul":
        month_jul =1
    elif month == "aug":
        month_aug= 1
    elif month == "sep":
        month_sep= 1
    elif month == "oct":
        month_sep=1
    elif month == "nov":
        month_nov =1
    elif month == "dec":
        month_dec= 1
    
    poutcome_failure=poutcome_other=poutcome_success=poutcome_unknown=0

    if poutcome == "failure":
        poutcome_failure=1
    elif poutcome == 'success':
        poutcome_success=1
    elif poutcome == 'other':
        poutcome_other=1
    elif poutcome == 'unknown':
        poutcome_unknown=1
    
    new_data=[[age, balance, day, duration, campaign ,pdays, previous,
        job_admin, job_blue_collar, job_entrepreneur,
       job_housemaid, job_management, job_retired, job_self_employed,
       job_services, job_student, job_technician, job_unemployed,
       job_unknown, marital_divorced, marital_married, marital_single,
       education_primary, education_secondary, education_tertiary,
       education_unknown, default_no, default_yes, housing_no,
       housing_yes, loan_no, loan_yes, contact_cellular,
       contact_telephone, contact_unknown, month_apr, month_aug,
       month_dec, month_feb, month_jan, month_jul, month_jun,
       month_mar, month_may, month_nov, month_oct, month_sep,
       poutcome_failure, poutcome_other, poutcome_success,
       poutcome_unknown]]

    """new_data = pd.get_dummies(new_data, columns=['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome'])
    
    
    """
    



    # load the trained model from joblib
    model = joblib.load('model.joblib')




    prediction = model.predict(new_data)

    # Display the prediction to the user

    # Display the prediction to the user
    if prediction == 0:
        result = 'not subscribed to the term deposit'
    else:
        result = 'subscribed to the term deposit'

    return render_template('result.html', prediction_text='The customer is {}'.format(result))

    
    



    




if __name__=="__main__":
    app.run(debug=True)

