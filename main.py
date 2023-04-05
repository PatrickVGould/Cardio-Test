import streamlit as st

# Add logo to page
st.image("mg_logo.png", width=200)


# Set up page title and subtitle
st.title("Positive Cardiometabolic Health Resource 💓")
st.subheader("An early intervention framework for people on psychotropic medication")

# Demographic questions
st.header("Demographics")
patient_name = st.text_input(label = "What is the person's name?", help = "This will be used to personalise the report at the end and will not be stored or shared with anyone else.")
col1, col2, col3 = st.columns(3)
with col1:
    sex = st.radio("What is the person's sex?", ["Male", "Female", "Other"])
with col2:
    age = st.number_input(label="What is the person's age?", step=1, min_value=0, max_value=120, help = "This is to determine which risk calculations and recommendations should be made as they vary between age groups.")
with col3:
    ethnicity = st.radio("Is the person of any of the following ethnicities? South Asian, Chinese, Japanese, Ethnic South and Central Americans", ["Yes", "No"])

# Lifestyle questions
st.header("Lifestyle")
col1, col2, col3 = st.columns(3)
with col1:
    smoking = st.radio("Is the person a current smoker (including tobacco, THC, vaping, shisha)?", ["Yes", "No"])
with col2:
    diet = st.radio(label="Does the person have a poor diet?", options = ["Yes", "No"], help="Poor diet includes high intake of processed foods, red meat, sugar-sweetened beverages, and low intake of vegetables, fruit, wholegrains, legumes/beans, and fish. See https://dietitiansaustralia.org.au/sites/default/files/2022-02/DA_NationalNutritionStrategy_Brief.pdf for more information.")
with col3:
    activity = st.radio("Does the person have more than 30 minutes physical activity on most days?", ["Yes", "No"])

# Obesity questions
st.header("Obesity")
col1, col2, col3 = st.columns(3)
with col1:
    BMI = st.number_input(label = "What is the person's BMI?", step=1, min_value=0, max_value=120)
with col2:
    weight_increase = st.radio("Has the person had a weight increase of greater than 5kg over the past 3 months?", ["Yes", "No"])
with col3:
    waist_circ = st.number_input(label = "What is the person's waist circumference in cm?", step=1, min_value=0, max_value=120)
col1, col2 = st.columns(2)
with col1:
    waist_increase = st.radio("Has the person had an increase in waist circumference of over 5cm in the past 3 months?", ["Yes", "No"])

# Blood pressure questions
st.header("Blood Pressure")
col1, col2 = st.columns(2)
with col1:
    systolic_bp = st.number_input("What is the person's systolic blood pressure?")
with col2:
    diastolic_bp = st.number_input("What is the person's diastolic blood pressure?")

# Glucose questions
st.header("Glucose")
col1, col2, col3 = st.columns(3)
with col1:
    HbA1c = st.number_input("What is the person's HbA1c?")
with col2:
    FPG = st.number_input("What is the person's FPG?")
with col3:
    AUSDRISK = st.number_input("What is the person's AUSDRISK?")

# Blood lipids questions
st.header("Blood Lipids")
col1, col2, col3 = st.columns(3)
with col1:
    TC = st.number_input("What is the person's TC?")
with col2:
    LDL = st.number_input("What is the person's LDL?")
with col3:
    HDL = st.number_input("What is the person's HDL?")
col1, col2, col3 = st.columns(3)
with col1:
    RPG = st.number_input("What is the person's RPG?")
with col2:
    non_HDL = st.number_input("What is the person's non-HDL?")
with col3:
    TRIG = st.number_input("What is the person's TRIG?")

# Sleep questions
st.header("Sleep")
col1, col2, col3 = st.columns(3)
with col1:
    neck_circ = st.number_input("What is the person's neck circumference in cm?")
with col2:
    daytime_tiredness = st.radio("Does the person have daytime tiredness?", ["Yes", "No"])
with col3:
    snoring = st.radio("Does the person have loud snoring or stop breathing during sleep?", ["Yes", "No"])

# Submit button
submit = st.button("Submit")

# Recommendations
if submit:
    st.write("**Cardiometabolic Recommendations Report**")
    st.write("Patient Name: ", patient_name)
    st.write("Age: ", age)
    st.write("Sex: ", sex)

    st.write("**Current Values:**")
    # Table of the current values that were entered by the user that are not blank
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Lifestyle:**")
        st.write("Smoking: ", smoking)
        st.write("Diet: ", diet)
        st.write("Activity: ", activity)
        st.write("Weight Increase: ", weight_increase)
        st.write("Waist Increase: ", waist_increase)   
    with col2:
        st.write("**Obesity:**")
        st.write("BMI: ", BMI)
        st.write("Waist Circumference: ", waist_circ)
        st.write("Waist Increase: ", waist_increase)
        st.write("Weight Increase: ", weight_increase)
    with col3:
        st.write("**Blood Pressure:**")
        st.write("Systolic BP: ", systolic_bp)
        st.write("Diastolic BP: ", diastolic_bp)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Glucose:**")
        st.write("HbA1c: ", HbA1c)
        st.write("FPG: ", FPG)
        st.write("AUSDRISK: ", AUSDRISK)
    with col2:
        st.write("**Blood Lipids:**")
        st.write("TC: ", TC)
        st.write("LDL: ", LDL)
        st.write("HDL: ", HDL)
        st.write("RPG: ", RPG)
        st.write("non-HDL: ", non_HDL)
        st.write("TRIG: ", TRIG)
    with col3:
        st.write("**Sleep:**")
        st.write("Neck Circumference: ", neck_circ)
        st.write("Daytime Tiredness: ", daytime_tiredness)
        st.write("Snoring: ", snoring)

    st.write(" ")
    st.write("**Recommendations**")

    st.write("Intensify and individualise structured nutritional counselling and lifestyle interventions. Refer for investigation, diagnosis and treatment by appropriate clinician if necessary.")
    st.write("Medication review (consider antipsychotic switching; review medications and rationalise any polypharmacy).")

    if smoking == "Yes":
        st.write("**Smoking:**")
        st.write("  *Interventions:*")
        st.write("      - Individualised smoking cessation program")
        st.write("      - Use Mindgardens Tobacco Treatment Framework")
        st.write("      - quitnow.gov.au")
        st.write("      - icanquit.com.au")
        st.write(" ")
        st.write("  *Targets:*")
        st.write("      Smoking prevention or cessation")

    if diet == "Yes":
        st.write("Diet:")
        st.write("- Decrease in discretionary foods")
        st.write("- Increase in vegetables and legumes/beans")
        st.write("- Consider referral to a Dietitian")
        st.write("- eatforhealth.gov.au")
        st.write(" ")

    st.write("Activity:")
    st.write("- Decrease sedentariness")
    st.write("- Increase physical activity")
    st.write("- Refer to the Physical Activity Guidelines")
    st.write("- Consider referral to an Exercise Physiologist")
    st.write(" ")

    if BMI >= 25 or weight_increase == "Yes" or (sex == "Male" and waist_circ >= 94) or (sex == "Female" and waist_circ >= 80) or (ethnicity == "Yes" and sex == "Male" and waist_circ >= 90) or waist_increase == "Yes":
        st.write("Weight and BMI:")
        st.write("- Consider metformin and/or GLP receptor agonist ")
        st.write("- Consider intensive intervention if BMI is greater than or equal to 30")
        st.write(" ")

    if systolic_bp >= 140 or diastolic_bp >= 90:
        st.write("Blood Pressure:")
        st.write("- Consider antihypertensive medication")
        st.write("- Limit salt intake in diet")
        st.write(" ")

    if HbA1c >= 6 or FPG >= 5.6 or AUSDRISK >= 12:
        st.write("Glucose:")
        st.write("- Monitor and manage blood glucose levels closely")
        st.write("- Consider referral to an endocrinologist if necessary")
        st.write(" ")

    if HbA1c >= 6.4 or FPG >= 7.0 or RPG >= 11.1:
        st.write("Glucose:")
        st.write("- Consider metformin")
        st.write("- Consider referral to an endocrinologist if necessary")
        st.write(" ")

    if TC >= 4 or LDL >= 2 or HDL <= 1 or non_HDL >= 2.5 or TRIG >= 1.7:
        st.write("Blood Lipids:")
        st.write("- Consider lipid lowering therapy")
        st.write(" ")

    if BMI >= 35 or neck_circ >= 40 or daytime_tiredness == "Yes" or snoring == "Yes":
        st.write("Sleep:")
        st.write("- Consider referral for a sleep study")
        st.write("- If mild-moderate sleep apnoea is diagnosed, target weight loss")
        st.write("- If severe sleep apnoea is diagnosed, consider CPAP")
        st.write(" ")

