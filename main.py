import streamlit as st

# Set up page title and subtitle
st.title("Positive Cardiometabolic Health Resource")
st.subheader("An early intervention framework for people on psychotropic medication")

# Demographic questions
sex = st.radio("What is the person's sex?", ["Male", "Female", "Other"])
age = st.number_input("What is the person's age?")
ethnicity = st.radio("Is the person of any of the following ethnicities? South Asian, Chinese, Japanese, Ethnic South and Central Americans", ["Yes", "No"])

# Lifestyle questions
st.header("Lifestyle")
smoking = st.radio("Is the person a current smoker (including tobacco, THC, vaping, shisha)?", ["Yes", "No"])
diet = st.radio("Does the person have a poor diet?", ["Yes", "No"])
activity = st.radio("Does the person have more than 30 minutes physical activity on most days?", ["Yes", "No"])

# Obesity questions
st.header("Obesity")
BMI = st.number_input("What is the person's BMI?")
weight_increase = st.radio("Has the person had a weight increase of greater than 5kg over the past 3 months?", ["Yes", "No"])
waist_circ = st.number_input("What is the person's waist circumference in cm?")
waist_increase = st.radio("Has the person had an increase in waist circumference of over 5cm in the past 3 months?", ["Yes", "No"])

# Blood pressure questions
st.header("Blood Pressure")
systolic_bp = st.number_input("What is the person's systolic blood pressure?")
diastolic_bp = st.number_input("What is the person's diastolic blood pressure?")

# Glucose questions
st.header("Glucose")
HbA1c = st.number_input("What is the person's HbA1c?")
FPG = st.number_input("What is the person's FPG?")
AUSDRISK = st.number_input("What is the person's AUSDRISK?")

# Blood lipids questions
st.header("Blood Lipids")
TC = st.number_input("What is the person's TC?")
LDL = st.number_input("What is the person's LDL?")
HDL = st.number_input("What is the person's HDL?")
RPG = st.number_input("What is the person's RPG?")
non_HDL = st.number_input("What is the person's non-HDL?")
TRIG = st.number_input("What is the person's TRIG?")

# Sleep questions
st.header("Sleep")
neck_circ = st.number_input("What is the person's neck circumference in cm?")
daytime_tiredness = st.radio("Does the person have daytime tiredness?", ["Yes", "No"])
snoring = st.radio("Does the person have loud snoring or stop breathing during sleep?", ["Yes", "No"])

# Recommendations
st.header("Recommendations")
if smoking == "Yes":
    st.subheader("Smoking")
    st.write("Individualised smoking cessation program")
    st.write("Use Mindgardens Tobacco Treatment Framework")
    st.write("quitnow.gov.au")
    st.write("icanquit.com.au")

if diet == "Yes":
    st.subheader("Diet")
    st.write("Discretionary foods")
    st.write("Vegetables and legumes/beans")
    st.write("Consider referral to a Dietitian")
    st.write("eatforhealth.gov.au")

if activity == "No":
    st.subheader("Activity")
    st.write("Sedentariness")
    st.write("Physical activity")
    st.write("Physical Activity Guidelines")
    st.write("Consider referral to an Exercise Physiologist")

if BMI >= 25 or weight_increase == "Yes" or (sex == "Male" and waist_circ >= 94) or (sex == "Female" and waist_circ >= 80) or (ethnicity == "Yes" and sex == "Male" and waist_circ >= 90) or waist_increase == "Yes":
    st.subheader("Weight, BMI")
    st.write("Consider metformin and/or GLP receptor agonist")

if BMI >= 30:
    st.subheader("Weight, BMI")
    st.write("Consider intensive intervention")

if systolic_bp >= 140 or diastolic_bp >= 90:
    st.subheader("Blood Pressure")
    st.write("Consider antihypertensive medication")
    st.write("Limit salt intake in diet")

if HbA1c >= 6 or FPG >= 5.6 or AUSDRISK >= 12:
    st.subheader("Glucose")
if HbA1c >= 6.4 or FPG >= 7.0 or RPG >= 11.1:
    st.write("Consider endocrine referral")
    st.write("Consider metformin")

if TC >= 4 or LDL >= 2 or HDL <= 1 or non_HDL >= 2.5 or TRIG >= 1.7:
    st.subheader("Blood Lipids")
    st.write("Consider lipid lowering therapy")

if BMI >= 35 or neck_circ >= 40 or daytime_tiredness == "Yes" or snoring == "Yes":
    st.subheader("Sleep")
    st.write("Consider referral for a sleep study. If they have mild-moderate sleep apnoea, target weight loss. If they have severe sleep apnoea, consider CPAP therapy.")

# Submit button
submit = st.button("Submit")
