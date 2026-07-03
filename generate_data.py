import pandas as pd
import numpy as np

np.random.seed(42)
n_records = 2500

applicant_ids = [f"LAPP_{i:04d}" for i in range(1, n_records + 1)]
ages = np.random.randint(21, 65, size=n_records)
genders = np.random.choice(['Male', 'Female'], size=n_records, p=[0.55, 0.45])
education = np.random.choice(['Graduate', 'Undergraduate', 'Postgraduate', 'High School'], size=n_records, p=[0.45, 0.30, 0.15, 0.10])
marital_status = np.random.choice(['Married', 'Single', 'Divorced'], size=n_records, p=[0.50, 0.40, 0.10])
employment_type = np.random.choice(['Salaried', 'Self-Employed', 'Business Owner', 'Unemployed'], size=n_records, p=[0.60, 0.20, 0.15, 0.05])

base_income = {'High School': 25000, 'Undergraduate': 45000, 'Graduate': 65000, 'Postgraduate': 85000}
annual_incomes = []
for edu, emp in zip(education, employment_type):
    bi = base_income[edu]
    multiplier = np.random.uniform(0.7, 1.8)
    if emp == 'Unemployed': multiplier = np.random.uniform(0.1, 0.4)
    elif emp == 'Business Owner': multiplier = np.random.uniform(1.2, 2.5)
    annual_incomes.append(int(bi * multiplier))

annual_incomes = np.array(annual_incomes)
credit_scores = []
for inc, age in zip(annual_incomes, ages):
    base_cs = 550 + int((inc / 150000) * 100) + int((age / 65) * 50)
    cs = int(base_cs + np.random.normal(0, 70))
    credit_scores.append(max(300, min(850, cs)))
credit_scores = np.array(credit_scores)

loan_amounts = []
for inc, cs in zip(annual_incomes, credit_scores):
    mult = np.random.uniform(0.5, 4.0)
    amt = int(inc * mult)
    loan_amounts.append(max(5000, min(500000, amt)))
loan_amounts = np.array(loan_amounts)

loan_terms = np.random.choice([12, 24, 36, 60, 84], size=n_records, p=[0.1, 0.2, 0.4, 0.2, 0.1])
dependents = np.random.choice([0, 1, 2, 3], size=n_records, p=[0.4, 0.3, 0.2, 0.1])
property_area = np.random.choice(['Urban', 'Semi-Urban', 'Rural'], size=n_records, p=[0.35, 0.45, 0.20])

approval_statuses = []
for cs, inc, amt, term in zip(credit_scores, annual_incomes, loan_amounts, loan_terms):
    m_inc = inc / 12
    m_pay = (amt * 1.08) / term
    dti = m_pay / (m_inc + 1)
    score = 0
    if cs >= 700: score += 45
    elif cs >= 600: score += 25
    elif cs >= 500: score += 10
    if dti <= 0.3: score += 35
    elif dti <= 0.5: score += 20
    if cs < 500: score -= 20
    if dti > 0.8: score -= 30
    score += np.random.normal(0, 15)
    approval_statuses.append('Approved' if score > 35 else 'Rejected')

df = pd.DataFrame({
    'Applicant_ID': applicant_ids, 'Age': ages, 'Gender': genders, 'Education': education,
    'Marital_Status': marital_status, 'Employment_Type': employment_type, 'Annual_Income': annual_incomes,
    'Credit_Score': credit_scores, 'Loan_Amount_Requested': loan_amounts, 'Loan_Term_Months': loan_terms,
    'Dependents': dependents, 'Property_Area': property_area, 'Approval_Status': approval_statuses
})

df.to_csv("bank_loan_data.csv", index=False)
print("Data file 'bank_loan_data.csv' successfully created with 2500 records!")