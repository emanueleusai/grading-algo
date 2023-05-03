import pandas as pd,json,numpy as np

# df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-03-15-03-05-56.csv')
# df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-03-15-04-47-12.csv')

# df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-05-01-11-00-30.csv')
# df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-05-01-10-58-49.csv')

df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-05-02-18-21-07.csv')
df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-05-02-18-20-44.csv')

# print(df)
df=df.fillna(0)
df_honors=df_honors.fillna(0)

from assessments import *

max_points={}
for i in max_points_raw.keys():
    max_points[columns_to_rename[i]]=max_points_raw[i]

max_points_honors={}
for i in max_points_honors_raw.keys():
    max_points_honors[columns_to_rename_honors[i]]=max_points_honors_raw[i]


hw_extra_credit_weights={
	"HW1E": 0.1,
	"HW2E": 0.1,
	"HW3E": 0.15,
	"HW4E": 0.1,
	"HW5E": 0.1,
	"HW6E": 0.1,

    "HW7E": 0.1,
    "HW8E": 0.1,
    "HW9E": 0.1,
    "HW10E": 0.1,
}

letters_thresholds={
	'A+':[97-0.005 , 1000],
	'A': [93-0.005 , 97-0.005],
	'A-':[90-0.005 , 93-0.005],
	'B+':[87-0.005 , 90-0.005],
	'B': [83-0.005 , 87-0.005],
	'B-':[80-0.005 , 83-0.005],
	'C+':[77-0.005 , 80-0.005],
	'C': [73-0.005 , 77-0.005],
	'C-':[70-0.005 , 73-0.005],
	'D+':[67-0.005 , 70-0.005],
	'D': [63-0.005 , 67-0.005],
	'D-':[59.0     , 63-0.005],
	'F': [0.     , 59.],
}


df=df.rename(columns=columns_to_rename)
df_honors=df_honors.rename(columns=columns_to_rename_honors)


columns=[columns_to_rename[i] for i in columns_to_rename.keys()]

print(df.columns)

for col in columns:
    df[col]=df[col]/max_points[col]
    # np.argmin(df.applymap(np.isreal).all(1))
    df_honors[col]=df_honors[col]/max_points_honors[col]

for i in range(1,len(hw_extra_credit_weights)+1):
    n=str(i)
    df["HW"+n]=df["HW"+n+"B"]+df["HW"+n+"E"]*hw_extra_credit_weights["HW"+n+"E"]
    df_honors["HW"+n]=df_honors["HW"+n+"B"]+df_honors["HW"+n+"E"]*hw_extra_credit_weights["HW"+n+"E"]



assessments={
    'LAB_AVG':[
    "LAB_ERROR",
    "LAB_1D",
    "LAB_NEWTON",
    "LAB_FRICTION",
    "LAB_ENERGY",
    "LAB_SPRING",
    "LAB_MOMENTUM",
    "LAB_ROTATIONAL",
    "LAB_GRAVITY",
    "LAB_ARCHIMEDE",
    "LAB_SHM",
    "LAB_WAVE",
    "LAB_GAS",
    # "LAB_CALORIMETRY", EXTRA CREDIT
    ],
    'QUIZ_AVG':["QUIZ1","QUIZ2","QUIZ3","QUIZ4","QUIZ5","QUIZ6","QUIZ7","QUIZ8","QUIZ9","QUIZ10"],
    'EXAM_AVG':["EXAM1","EXAM2","FINAL"],
    'HW_AVG':["HW1","HW2","HW3","HW4","HW5","HW6","HW7","HW8","HW9","HW10"],
}

assessments_extracredit={
    'LAB_AVG': ["LAB_CALORIMETRY"],
    'QUIZ_AVG':["QUIZ11"],
    'EXAM_AVG':[],
    'HW_AVG':["HW11"],
}

assessment_weights={
    'LAB_AVG':0.2,
    'QUIZ_AVG':0.15,
    'EXAM_AVG':0.50,
    'HW_AVG':0.15,   
}

total_norm=sum([assessment_weights[i] for i in assessment_weights.keys()])#0.2+0.15+0.15+0.15
print(total_norm)


exam_weights={
"EXAM1":0.3,
"EXAM2":0.3,
"FINAL":0.4}

ec_weights={
    "FCI":0.1,
    "HONORS": 0.07
}

for i in assessments.keys():
    if i=='EXAM_AVG':
        df[i]=sum([df[j]*exam_weights[j] for j in assessments[i]])
        df_honors[i]=sum([df_honors[j]*exam_weights[j] for j in assessments[i]])
    else:
        # df[i]=sum([df[j] for j in assessments[i]])/len(assessments[i])
        tmp=np.sort(df[assessments[i]], axis=1)[:, 2:]
        tmp=np.append(tmp,df[assessments_extracredit[i]],axis=1)
        df[i] = tmp.sum(1)/(len(assessments[i])-2)

        tmp_honors=np.sort(df_honors[assessments[i]], axis=1)[:, 2:]
        tmp_honors=np.append(tmp_honors,df_honors[assessments_extracredit[i]],axis=1)
        df_honors[i] = tmp_honors.sum(1)/(len(assessments[i])-2)

df['total']=sum([
        df[i]*assessment_weights[i]
        for i in assessment_weights.keys()
        ]+[df["FCI"]*ec_weights['FCI']])/total_norm*100

df_honors['total']=sum([
        df_honors[i]*assessment_weights[i]
        for i in assessment_weights.keys()
        ]+[df_honors["FCI"]*ec_weights['FCI'],df_honors["HONORS"]*ec_weights['HONORS']])/total_norm*100

df2=df.loc[df['Last Name'] == "Usai"]
print(df2[['Last Name', 'First Name',"LAB_AVG","QUIZ_AVG","HW_AVG","EXAM_AVG",'FCI','total']])

# f_waivers = open('grading-data/waivers.json')
# waivers = json.load(f_waivers)
# f_waivers.close()
  
# Iterating through the json
# list
# for i in waivers['student']:
#     print(i)
  

