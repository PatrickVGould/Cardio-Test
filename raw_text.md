Page title: Positive Cardiometabolic Health Resource

Sub title: An early intervention framework for people on psychotropic medication

Flowchart headings:
- Lifestyle
	- Smoking
	- Diet
	- Activity
- Obesity
	- Weight, BMI
	- Waist
- Blood Pressure
- Glucose
- Blood Lipids
- Sleep

Screening Questions:
Demographic:
	variable name: sex
    Question: What is the persons sex?
	Answer: Male/Female/Other
	
    variable name: age
    Question: What is the persons age?
    Answer: Number input

	variable name: ethnicity
    Question: Is the person of any of the following ethnicities? South Asian, Chinese, Japanese, Ethnic South and Central Americans
	Answer: Yes/No

Lifestyle:
	Smoking questions:
		variable name: smoking
        Question: Is the person a current smoking (including tobacco, thc, vaping, shisha)? (Remember to ask at regular opportunities)
		Options: Yes/No

	Diet questions:
		variable name: diet
        Question: Does the person have a poor diet?
		Options: Yes/No

	Activity questions:
		variable name: activity
        Question: Does the person have more than 30 minutes physical activity on most days?
		Options: Yes/No

Obesity:
	Weight,BMI questions:
		variable name: BMI
        Question: What is the persons BMI?
		Answer: Number input
		
		variable name: weight_increase
        Question: Has the person had a weight increase of greater than 5kg over the past 3 months?
		Answer: Yes/No
		
	Waist questions:
		variable name: waist_circ
        Question: What is the persons waist circumpherence in cm?
		Answer: Number input
		
        variable name: waist_increase
        Question: Has the person had an increase in waist circumpherence of over 5cm in the past 3 months?
		Answer: Yes/No

Blood Pressure:
    variable name: systolic_bp
    Question: What is the persons systolic blood pressure?
    Answer: Number input

    variable name: diastolic_bp
    Question: What is the persons diastolic blood pressure?
    Answer: Number input

Glucose:
    variable name: HbA1c
    Question: What is the persons HbA1c?
    Answer: Number input

    variable name: FPG
    Question: What is the persons FPG?
    Answer: Number input

    variable name: AUSDRISK
    Question: What is the persons AUSDRISK?
    Answer: Number input

Blood Lipids:
    variable name: TC
    Question: What is the persons TC?
    Answer: Number input

    variable name: LDL
    Question: What is the persons LDL?
    Answer: Number input

    variable name: HDL
    Question: What is the persons HDL?
    Answer: Number input

    variable name: non_HDL
    Question: What is the persons non-HDL?
    Answer: Number input

    variable name: TRIG
    Question: What is the persons TRIG?
    Answer: Number input

Sleep:
    variable name: neck_circ
    Question: What is the persons neck circumference in cm?
    Answer: Number input

    variable name: daytime_tiredness
    Question: Does the person have daytime tiredness?
    Answer: Yes/No

    variable name: snoring
    Question: Does the person have loud snoring or stops breathing during sleep?
    Answer: Yes/No

Recommendations:
Lifestyle:
    Smoking:
        if smoking = Yes
            Recommend: Individualised smoking cessation program
            Recommend: Use Mindgardens Tobacco Treatment Framework
            Recommend: quitnow.gov.au
            Recommend: icanquit.com.au
    Diet:
        if diet = Yes
            Recommend: Discretionary foods
            Recommend: Vegetables and legumes/beans
            Recommend: Consider referral to a Dietitian
            Recommend: eatforhealth.gov.au
    Activity:
        if activity = No
            Recommend: Sedentariness
            Recommend: Physical activity
            Recommend: Physical Activity Guidelines
            Recommend: Consider referral to an Exercise Physiologist
Obesity:
    Weight, BMI:
        if BMI >= 25 OR weight_increase = Yes OR (sex=male AND waist_circ >= 94) OR (sex=female AND waist_circ >=80) OR (ethnicity = Yes AND sex=male AND waist_circ>=90) OR waist_increase = Yes
            Recommend: Consider metformin and/or GLP receptor agonist
        if BMI >= 30
            Recommend: Consider intensive intervention
Blood Pressure:
    if systolic_bp >= 140 OR diastolic_bp >= 90
        Recommend: Consider antihypertensive medication
        Recommend: Limit salt intake in diet
Glucose:
    if HbA1c >= 6 OR FPG >= 5.6 OR AUSDRISK >= 12
        if HbA1c >= 6.4 or FPG >= 7.0 or RPG >= 11.1
            Recommend: Consider endocrine referral
        Recommend: Consider metformin
Blood Lipids:
    if TC >= 4 OR LDL >= 2 OR HDL <= 1 OR non_HDL >= 2.5 OR TRIG >= 1.7
        Recommend: Consider lipid lowering therapy
Sleep:
    if BMI >= 35 OR neck_circ >= 40 OR daytime_tiredness = Yes OR snoring = Yes
        Recommend: Consider referral for a sleep study. If they have mild-moderate sleep apnoea, target weight loss. If they have severe sleep apnoea, consider CPAP therapy.

[]: # Path: SynthScope\main\Cardiometabolic Test\raw_text.md


BMI >25 kg/m2
(>23 kg/m2)*
and/or
Weight . >5 kg
over 3 months

>94 cm male
(>90 cm)* 
or
>80 cm female
and/or
Waist . >5 cm
over 3 months

>140 mmHg systolic
and/or 
>90 mmHg diastolic

HbA1c =6.0% (>42 mmol/mol)
FPG =5.6 mmol/L
AUSDRISK =12

TC >4 mmol/L
LDL =2.0 mmol/L
HDL <1.0 mmol/L
non-HDL >2.5 mmol/L
TRIG =1.7 mmol/L

BMI >35 kg/m2
Neck circumference >40 cm
Daytime tiredness
Loud snoring/stopping breathing during sleep

Poor diet

Physical activity <30 mins
on most days

Current smoker
(e.g. tobacco, 
THC, vaping, 
shisha) 
Ask at regular opportunities

RED ZONE


Intensify and individualise structured nutritional counselling and lifestyle interventions. Refer for investigation, diagnosis and treatment by appropriate clinician if necessary.

Individualised smoking cessation program 
Use Mindgardens Tobacco Treatment Framework
quitnow.gov.au
icanquit.com.au

INTERVENTION

Medication review (consider antipsychotic switching; review medications and rationalise any polypharmacy).

. Discretionary foods
. Vegetables and legumes/beans
Consider referral 
to a Dietitian
eatforhealth.gov.au 


. Sedentariness

. Physical activity

Physical Activity Guidelines

Consider referral to an Exercise Physiologist 

Consider lipid lowering therapy

Refer for 
sleep study
 Mild-Moderate OSA: Weight loss
Severe OSA: CPAP

Consider metformin 
and/or
GLP receptor agonist
If BMI =30 kg/m2
consider intensive intervention (see rear page)

Limit salt intake in diet

Consider 
antihypertensive therapy

At High Risk of Diabetes:
HbA1c: 6.0-6.4%
(42 - 47 mmol/mol)
FPG 5.6-6.9 mmol/L
Consider metformin

Diabetes:
HbA1c >6.4%
(>48 mmol/mol)
FPG =7.0 mmol/L
RPG >11.1 mmol/L
Consider endocrine referral 


Smoking prevention or cessation

Improve quality 
of diet
Contain energy intake 
(to stabilise weight)

Physical activity (at least 30 mins on most, preferably 
all days)

Improved alertness
Reduced or resolved OSA

TC <4 mmol/L
LDL <2.0 mmol/L 
(<1.8 if CVD or diabetes)
HDL =1.0 mmol/L
non-HDL <2.5 mmol/L
TRIG <1.7 mmol/L

<140 mmHg systolic and/or 
<90 mmHg diastolic 

(<130/80 if CVD or diabetes)

Prevent or delay onset of diabetes:

HbA1c <6.0%
(<42 mmol/mol)

FPG <5.6 mmol/L

BMI 20-24.9 kg/m2 (<23 kg/m2)*
Waist circumference:
<94 cm male (<90 cm)* and 
<80 cm female

Diabetes:

HbA1c individualised to the consumer's circumstances

Generally <7% 
RACGP Handbook

TARGET


*For South Asian, Chinese, Japanese, Ethnic South and Central Americans. | BMI = Body Mass Index | CVD = Cardiovascular disease | FPG = Fasting Plasma Glucose | GLP = Glucagon-like Peptide | HbA1c = Glycated Haemoglobin | 
HDL = High Density Lipoprotein | LDL = Low Density Lipoprotein | OSA = Obstructive Sleep Apnoea | RPG = Random Plasma Glucose | TC = Total Cholesterol | TRIG = Triglycerides

mindgardens.org.au/KBIMResources

Positive Cardiometabolic Health Resource

An early intervention framework for people on psychotropic medication





DON’T JUST SCREEN 
INTERVENE
for all people in the ‘red zone’

Decision making surrounding screening and agreed interventions should be made with the consumer and include consultation with carers, families, and key stakeholders (e.g. general practitioner, mental health clinicians, and community providers).


Review of antipsychotic and 
mood stabiliser medications
•	 Choose lower metabolic liability medication first line where possible
•	 Review diagnosis and ensure ongoing need for all      	 psychotropic medications
•	 Consider switching to a more weight neutral  		 medication where possible
•	 Avoid antipsychotic polypharmacy
•	 Avoid off-label use of antipsychotic medications
•	 Changing antipsychotic medication requires careful 	 clinical judgement to weigh any benefits against the 
 risk of relapse of psychosis
Review should be a priority if there is:
	- Rapid weight gain (e.g. 5 kg < 3 months) 			   following antipsychotic initiation or change
	- Rapid development (< 3 months) of abnormal 		   lipids, BP, or glucose
If consumer has not successfully reached targets after
3 months, then consider specific pharmacological
interventions


Specific pharmacological interventions 
Consider metformin trial for:  
•  Impaired fasting glucose 
•  Obesity or rapid weight gain 
•  Polycystic ovary syndrome
Note that off-label use requires documented informed consent 
Metformin therapy: 
Start at 250 mg before dinner for two weeks, then increase to 250 mg bd. Dose can be increased by 500 mg per week to a maximum of 3 grams daily (taken in split doses with meals). If side-effects of nausea or abdominal cramping shift to after meal (or the XR preparation)
Lipid lowering therapy: 
Co-management with GP recommended. Consider lipid lowering therapy (use PBS guidelines). If severe hyperlipidaemia or other risk factors, consider specialist referral
Antihypertensive therapy: 
Refer to general practitioner or specialist
Vitamin D:
•  <50 nmol/L: Cholecalciferol treatment 3000–5000 IU daily for 6–12 weeks to replenish stores followed by a maintenance dose of 1000–2000 IU daily
•  Target: >80 nmol/L


Intensive Interventions
Intensive interventions to support weight loss may be considered with a BMI of >30 kg/m2 or if unsuccessful in reducing weight or has regained weight using lifestyle approaches. Intensive interventions may include:
•  Metformin and/or GLP receptor agonist 
•  Very low energy diets for 8-16 weeks under medical supervision, replacing one or more meals per day with food or formulas that provide a specified number of kilojoules (e.g. 1675-3350 kJ/day)
•  Referral to obesity clinic
•  Consider referral for assessment for bariatric surgery



History and examination following initiation or change of psychotropic medications
History: Seek history of smoking, poor diet (e.g. high calorie, high fat/sugar), physical activity and sedentariness (e.g. screen time), sleep, and polycystic ovary syndrome. Ask about family history (diabetes, obesity, early CVD), gestational diabetes. Note ethnicity.
Investigations: Fasting estimates of plasma glucose (FPG), HbA1c, and lipids (total cholesterol, LDL, HDL, non-HDL, triglycerides). If fasting samples are impractical then non-fasting samples are satisfactory for most measurements except for triglycerides.
Frequency: At a minimum, those starting or changing antipsychotics should be monitored as below. 
After 12 months, continue to monitor at 6-month intervals, with increased frequency if abnormalities emerge, which should then prompt appropriate action and/or continuing review at least every 3 months.

Monitoring Intervals
 
Baseline
 Weekly*

 3 months
 6 months
 9 months
 12 months
 Continue 6 monthly
 
Personal/Family History
 .
 .
 .
 
Lifestyle Review
 .
 .
 .
 .
 .
 .
 .
 
Weight
 .
 .
 .
 .
 .
 .
 .
 
Waist
 .
 .
 .
 .
 .
 .
 
Blood pressure
 .
 .
 .
 .
 .
 
FPG, RPG, HbA1c
 .
 .
 .
 .
 .
 
Lipid profile
 .
 .
 .
 .
 .
 
Vitamin D
 .
 .
 .
 .
 



Other Considerations:
Other baseline investigations are not included here and need to be performed as clinically required (e.g. TFTs, UECs, FBC, ECHO). Additional monitoring requirements apply for those on mood stabilisers and clozapine (e.g. medication plasma levels). Prolactin measurement is only recommended if symptomatic. Consider ECG/cardiology review if concern regarding QT prolongation or cardiovascular risk factors present. 
Screen for polycystic ovary syndrome in all women: No menstrual cycle for 3 months, acne, hirsutism. Check prolactin, consider metformin and endocrine referral. Treatment may restore fertility, ensure contraception is discussed. Some medications used to treat metabolic disorder are contraindicated in pregnancy (e.g. some antihypertensives and lipid lowering drugs). 
Other issues such as sexual health, blood borne virus screening, oral health, vaccination status, and substance use have not been included in this resource though are important to discuss with all consumers. 


2022 Update. Adapted from Curtis J, Newall H, Samaras K. ©HETI 2011



