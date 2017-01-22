# -*- coding: utf-8 -*-
"""
Lending Club
"""

## load required packages
import pandas as pd 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt 
%matplotlib inline 
import seaborn as sns

## Load the dataset 
import os 
os.chdir(r'D:/Dataset/kaggle_Lending Club Loan Data')

loan = pd.read_csv('loan.csv')

print(loan.head())

# 74 columns?
# there may be some errors with reading the dataset 

# check which column has NA
print(loan.isnull().any())

## check the errors causing the wrong number of columns
print(loan.columns)
print(len(loan.columns))

# get the right column names
correct_col = 'index, id, member_id, loan_amnt, funded_amnt, funded_amnt_inv, term, int_rate, installment, grade, sub_grade, emp_title, emp_length, home_ownership, annual_inc, verification_status, issue_d, loan_status, pymnt_plan, url, desc, purpose, title, zip_code, addr_state, dti, delinq_2yrs, earliest_cr_line, inq_last_6mths, mths_since_last_delinq, mths_since_last_record, open_acc, pub_rec, revol_bal, revol_util, total_acc, initial_list_status, out_prncp, out_prncp_inv, total_pymnt, total_pymnt_inv, total_rec_prncp, total_rec_int, total_rec_late_fee, recoveries, collection_recovery_fee, last_pymnt_d, last_pymnt_amnt, next_pymnt_d, last_credit_pull_d, collections_12_mths_ex_med, mths_since_last_major_derog, policy_code, application_type, annual_inc_joint, dti_joint, verification_status_joint, acc_now_delinq, tot_coll_amt, tot_cur_bal, open_acc_6m, open_il_6m, open_il_12m, open_il_24m, mths_since_rcnt_il, total_bal_il, il_util, open_rv_12m, open_rv_24m, max_bal_bc, all_util, total_rev_hi_lim, inq_fi, total_cu_tl, inq_last_12m'
correct_col = correct_col.split(',')
correct_col = [x.strip() for x in correct_col]
print(correct_col)
print(len(correct_col))

# get the difference between them 
print(np.setdiff1d(np.array(correct_col), np.array(loan.columns))) # the array with more elements is put as the former parameter

# the index column is the difference
# this doesn't matter 


### filter the loans that have been expired
from datetime import datetime
import time
print(loan['issue_d'][:10])
print(loan['issue_d'][887360:])
print(loan['term'][:10])

# test
test = 'Dec-2011'
print(datetime.strptime(test, '%b-%Y'))
print(datetime.strptime(test, '%b-%Y').year)
print(datetime.strptime(test, '%b-%Y').replace(year = datetime.strptime(test, '%b-%Y').year+3))

loan['end_d'] = loan['issue_d'].apply(lambda x: datetime.strptime(x, '%b-%Y'))
print(loan['end_d'][:10])
start_time = time.time()
for i in range(len(loan)):
    print(i)
    if int(loan['term'][i].split()[0]) == 36:
        loan['end_d'][i] = loan['end_d'][i].replace(year = loan['end_d'][i].year+int(36/12))
    else:
        loan['end_d'][i] = loan['end_d'][i].replace(year = loan['end_d'][i].year+int(60/12))
end_time = time.time()
print('done')        
print(end_time - start_time)
print(loan['end_d'][:10])



loan['end_test'] = loan.apply(lambda row: row['end_d'].replace(year = row['end_d'].year+int(36/12)) if 
int(row['term'].split()[0]) == 36 else row['end_d'].replace(year = row['end_d'].year+int(60/12)), axis=1)