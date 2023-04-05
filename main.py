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
    bmi_options = ['<25','25-29','30-34','≥35']
    if ethnicity == "Yes":
        bmi_options = ['<23','≥23', '23-30','30-34','≥35']
    bmi = st.radio(label = "What is the person's BMI?", options = bmi_options)
with col2:
    weight_increase = st.radio("Has the person had a weight increase of greater than 5kg over the past 3 months?", ["Yes", "No"])
with col3:
    waist_options = ['<80','≥80']
    if sex == 'Male':
        if ethnicity == "Yes":
            waist_options = ['<90','≥90'] 
        else:
            waist_options = ['<94','≥94']
    
    waist_circ = st.radio(label = "What is the person's waist circumference in cm?", options=waist_options)
col1, col2 = st.columns(2)
with col1:
    waist_increase = st.radio("Has the person had an increase in waist circumference of over 5cm in the past 3 months?", ["Yes", "No"])

# Blood pressure questions
st.header("Blood Pressure")
col1, col2 = st.columns(2)
with col1:
    sys_bp_options = ['<140 mmHg','≥140 mmHg']
    systolic_bp = st.radio(label = "What is the person's systolic blood pressure?", options = sys_bp_options)
with col2:
    dia_bp_options = ['<90 mmHg','≥90 mmHg']
    diastolic_bp = st.radio(label = "What is the person's diastolic blood pressure?", options = dia_bp_options)

# Glucose questions
st.header("Glucose")
col1, col2, col3, col4 = st.columns(4)
with col1:
    hba1c_options = ['<6.0% (<42 mmol/mol)','6.0%-6.4% (42-47 mmol/mol)','≥6.4% (48 mmol/mol)']
    hba1c = st.radio(label = "What is the person's HbA1c?", options = hba1c_options)
with col2:
    fpg_options = ['<5.6 mmol/L','5.6-6.9 mmol/L','≥7.0 mmol/L']
    fpg = st.radio(label = "What is the person's FPG?", options = fpg_options)
with col3:
    ausdrisk_options = ['<12','≥12']
    ausdrisk = st.radio(label = "What is the person's [AUSDRISK](%s)?" % 'https://www.health.gov.au/resources/apps-and-tools/the-australian-type-2-diabetes-risk-assessment-tool-ausdrisk', options = ausdrisk_options)
with col4:
    rpg_options = ['<11 mmol/L','>11 mmol/L']
    rpg = st.radio(label = "What is the person's RPG?", options = rpg_options)

# Blood lipids questions
st.header("Blood Lipids")
col1, col2, col3 = st.columns(3)
with col1:
    tc_options = ['<4 mmol/L','≥4 mmol/L']
    tc = st.radio(label = "What is the person's TC?", options = tc_options)
with col2:
    ldl_options = ['<2 mmol/L','≥2 mmol/L']
    ldl = st.radio(label = "What is the person's LDL?", options = ldl_options)
with col3:
    hdl_options = ['<1 mmol/L','≥1 mmol/L']
    hdl = st.radio(label = "What is the person's HDL?", options = hdl_options)
col1, col2, col3 = st.columns(3)
with col1:
    non_hdl_options = ['<2.5 mmol/L','≥2.5 mmol/L']
    non_hdl = st.radio(label = "What is the person's non-HDL?", options = non_hdl_options)
with col2:
    trig_options = ['<1.7 mmol/L','≥1.7 mmol/L']
    trig = st.radio(label = "What is the person's TRIG?", options = trig_options)
with col3:
    placeholder = st.empty()

# Sleep questions
st.header("Sleep")
col1, col2, col3 = st.columns(3)
with col1:
    neck_circ_options = ['<40 cm','≥40 cm']
    neck_circ = st.radio(label="What is the person's neck circumference in cm?", options = neck_circ_options)
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
        st.write("BMI: ", bmi)
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
        st.write("HbA1c: ", hba1c)
        st.write("FPG: ", fpg)
        st.write("AUSDRISK: ", ausdrisk)
    with col2:
        st.write("**Blood Lipids:**")
        st.write("TC: ", tc)
        st.write("LDL: ", ldl)
        st.write("HDL: ", hdl)
        st.write("RPG: ", rpg)
        st.write("non-HDL: ", non_hdl)
        st.write("TRIG: ", trig)
    with col3:
        st.write("**Sleep:**")
        st.write("Neck Circumference: ", neck_circ)
        st.write("Daytime Tiredness: ", daytime_tiredness)
        st.write("Snoring: ", snoring)

    st.write(" ")
    st.write("# **Recommendations**")

    st.write("Intensify and individualise structured nutritional counselling and lifestyle interventions. Refer for investigation, diagnosis and treatment by appropriate clinician if necessary.")
    st.write("Medication review (consider antipsychotic switching; review medications and rationalise any polypharmacy).")

    if smoking == "Yes":
        st.markdown(body = """
        ### **Smoking:**
        #### *Interventions:*
        <li><p>Individualised smoking cessation program</p></li>
        <li><p>Use Mindgardens Tobacco Treatment Framework</p></li>
        <li><p>quitnow.gov.au</p></li>
        <li><p>icanquit.com.au</p></li>
        #### *Targets:*
        <li><p>Smoking prevention or cessation</p></li>
        """, unsafe_allow_html = True)

    if diet == "Yes":
        st.markdown("""
        **Diet:**
            - *Interventions:*
                - Decrease in discretionary foods
                - Increase in vegetables and legumes/beans
                - Consider referral to a Dietitian
                - eatforhealth.gov.au
            - *Targets:*
                - Improve quality of diet
                - Contain energy intake (to stabilise weight)
        """)
    if activity == "No":
        st.markdown("""
         **Activity:**
            - *Interventions:*
                - Decrease sedentariness
                - Increase physical activity
                - Refer to the Physical Activity Guidelines
                - Consider referral to an Exercise Physiologist
            - *Targets:*
                - Physical activity (at least 30 mins on most, preferably all days)
            """)

    if (bmi in ['25-29','30-34','≥35'] or (bmi in ['≥23', '23-30','30-34','≥35']) and ethnicity=='Yes') or (weight_increase == "Yes") or (sex == "Male" and waist_circ >= 94) or (sex == "Female" and waist_circ >= 80) or (ethnicity == "Yes" and sex == "Male" and waist_circ >= 90) or waist_increase == "Yes":
        st.markdown("""
        **Weight and BMI:**
            - *Interventions:*
                - Consider metformin and/or GLP receptor agonist""")
        if bmi in ["30-34","≥35"]:
            st.markdown("""     - Consider intensive intervention if BMI is greater than or equal to 30""")
        st.markdown(""" - *Targets:*
                - BMI 20-24.9 kg/m2 (<23 kg/m2)*
                - Waist circumference: <94 cm male (<90 cm)* and <80 cm female
        """)

    if systolic_bp == '≥140 mmHg' or diastolic_bp == '≥90 mmHg':
        st.markdown("""
        **Blood Pressure:**
            - *Interventions:*
                - Consider antihypertensive medication
                - Limit salt intake in diet
            - *Targets:*
                - <140 mmHg systolic and/or <90 mmHg diastolic
                - (<130/80 if CVD or diabetes)
    """)

    if (hba1c == ['6.0%-6.4% (42-47 mmol/mol)','≥6.4% (48 mmol/mol)']) or (fpg in ['5.6-6.9 mmol/L','≥7.0 mmol/L']) or ausdrisk == '≥12':
        if hba1c == "≥6.4% (48 mmol/mol)" or fpg == "≥7.0 mmol/L" or rpg == "≥11.1 mmol/L":
            st.markdown(f"""
            **Glucose:**
                - *Interventions:*
                    - {patient_name} meets the criteria for diabetes
                    - Consider metformin
                    - Consider referral to an endocrinologist
                - *Targets:*
                    - HbA1c individualised to the consumer's circumstances
                    - Generally <7% As per [RACGP Handbook](https://www.racgp.org.au/clinical-resources/clinical-guidelines/key-racgp-guidelines/view-all-racgp-guidelines/diabetes/introduction)
            """)
        else:
            st.markdown(f"""
            **Glucose:**
                - *Interventions:*
                    - Consider metformin
                    - Consider referral to an endocrinologist if necessary
                - *Targets:*
                    - It is vital to prevent or delay onset of diabetes by targeting:
                        - HbA1c <6.0% (<42 mmol/mol)
                        - FPG <5.6 mmol/L
            """)

    if tc == "≥4 mmol/L" or ldl == "≥2 mmol/L" or hdl == "≥1 mmol/L" or non_hdl == "≥2.5 mmol/L" or trig == "≥1.7 mmol/L":
        st.markdown("""
        **Blood Lipids:**
            - Consider lipid lowering therapy
        """)

    if bmi == '≥35' or neck_circ == "≥40 cm" or daytime_tiredness == "Yes" or snoring == "Yes":
        st.markdown("""
        **Sleep:**
            - *Interventions:*
                - Consider referral for a sleep study
                - If mild-moderate sleep apnoea is diagnosed, target weight loss
                - If severe sleep apnoea is diagnosed, consider CPAP
            - *Targets:*
                - Improved alertness
                - Reduced or resolved OSA
        """)

