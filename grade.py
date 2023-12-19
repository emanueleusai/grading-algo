import pandas as pd,numpy as np,importlib


df = pd.read_csv('grading-data/gc_43634.202340_fullgc_2023-12-18-03-11-40.csv')
# df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-05-06-12-32-50.csv')


# print(df)
df=df.fillna(0)
# df_honors=df_honors.fillna(0)

from assessments import *

max_points={}
for i in columns_info.keys():
    max_points[columns_info[i][0]]=columns_info[i][1]

columns_to_rename={}
for i in columns_info.keys():
    columns_to_rename[i]=columns_info[i][0]

# max_points_honors={}
# for i in max_points_honors_raw.keys():
#     max_points_honors[columns_to_rename_honors[i]]=max_points_honors_raw[i]


# hw_extra_credit_weights={
# 	"HW1E": 0.1,
# 	"HW2E": 0.1,
# 	"HW3E": 0.15,
# 	"HW4E": 0.1,
# 	"HW5E": 0.1,
# 	"HW6E": 0.1,

#     "HW7E": 0.1,
#     "HW8E": 0.1,
#     "HW9E": 0.1,
#     "HW10E": 0.1,
# }

hw_extra_credit_weights={
    "HW1E": 0.15,
    "HW2E": 0.15,
    "HW3E": 0.15,
    "HW4E": 0.15,
    "HW5E": 0.15,
    "HW6E": 0.15,

    "HW7E": 0.15,
    "HW8E": 0.15,
    "HW9E": 0.15,
    "HW10E": 0.15,
}

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
    'LAB_AVG':0.30,
    'QUIZ_AVG':0.10,
    'EXAM_AVG':0.45,
    'HW_AVG':0.15,   
}

df=df.rename(columns=columns_to_rename)
# df_honors=df_honors.rename(columns=columns_to_rename_honors)


columns=[columns_to_rename[i] for i in columns_to_rename.keys()]

print(df.columns)

for col in columns:
    # print(col)
    # print(df[col])
    df[col]=df[col]/max_points[col]
    # df_honors[col]=df_honors[col]/max_points_honors[col]

# df_honors['HONORS']=df_honors['HONORS']/max_points_honors['HONORS']

for i in range(1,len(hw_extra_credit_weights)+1):
    n=str(i)
    df["HW"+n]=df["HW"+n+"B"]+df["HW"+n+"E"]*hw_extra_credit_weights["HW"+n+"E"]
    # df_honors["HW"+n]=df_honors["HW"+n+"B"]+df_honors["HW"+n+"E"]*hw_extra_credit_weights["HW"+n+"E"]

# take_home_only=['QUIZ4','QUIZ8','QUIZ10','QUIZ11']
take_home_only=[4,8,10,11]

for i in range(1,len(assessments["QUIZ_AVG"])+1):
    n=str(i)
    if i not in take_home_only:
        df["QUIZ"+n+"RAW"]=df[["QUIZ"+n+"AS", "QUIZ"+n+"TH"]].max(axis=1)

quiz_intervals=np.array([-0.1,0.9,1.9,2.9,3.9,1000])
quiz_percent=np.array([0,0.5,0.75,1,1.10])
quiz_percent6=np.array([0.5,1,1.25,1.5,1.60])

for i in range(1,len(assessments["QUIZ_AVG"])+2):
    n=str(i)
    if i!=6:
        df["QUIZ"+n]=quiz_percent[np.searchsorted(quiz_intervals, df["QUIZ"+n+"RAW"])-1]
    else:
        df["QUIZ"+n]=quiz_percent6[np.searchsorted(quiz_intervals, df["QUIZ"+n+"RAW"])-1]



waivers = importlib.import_module("grading-data.waivers")


for student in waivers.waivers:
    for waiver in waivers.waivers[student]:
        df.loc[df['Username']==student,waiver]=10000
        # print(student,waiver,df.loc[df['Username']==student,waiver])

# for student in waivers.waivers_honors:
#     for waiver in waivers.waivers_honors[student]:
#         df_honors.loc[df_honors['Username']==student,waiver]=10000
        # print(student,waiver,df_honors.loc[df_honors['Username']==student,waiver])

total_norm=sum([assessment_weights[i] for i in assessment_weights.keys()])#0.2+0.15+0.15+0.15
print(total_norm)


# exam_weights={
# "EXAM1":0.3,
# "EXAM2":0.3,
# "FINAL":0.4}

# exam_weights_skip1={
# "EXAM1":0.0,
# "EXAM2":0.45,
# "FINAL":0.55}

# exam_weights_skip2={
# "EXAM1":0.3,
# "EXAM2":0.0,
# "FINAL":0.7}

ec_weights={
    "FCI":0.1,
    # "HONORS": 0.07
}

for i in assessments.keys():
    if i=='EXAM_AVG':
        tmp=np.sort(df[assessments[i]], axis=1)[:, 1:]
        tmp_low=np.sort(df[assessments[i]], axis=1)[:, 0:1]
        # print('tmp',tmp,'tmp_low',tmp_low)
        tmp=np.append(tmp,tmp_low/3,axis=1)
        # print("tmp2",tmp)
        df[i] = tmp.sum(1)/2


        # df[i]=sum([df[j]*exam_weights[j] for j in assessments[i]])
        # df.loc[df['EXAM1']>1000,i]=sum([df.loc[df['EXAM1']>1000][j]*exam_weights_skip1[j] for j in assessments[i]])
        # df.loc[df['EXAM2']>1000,i]=sum([df.loc[df['EXAM2']>1000][j]*exam_weights_skip2[j] for j in assessments[i]])


        # df_honors[i]=sum([df_honors[j]*exam_weights[j] for j in assessments[i]])
        # df_honors.loc[df_honors['EXAM1']>1000,i]=sum([df_honors.loc[df_honors['EXAM1']>1000][j]*exam_weights_skip1[j] for j in assessments[i]])
        # df_honors.loc[df_honors['EXAM2']>1000,i]=sum([df_honors.loc[df_honors['EXAM2']>1000][j]*exam_weights_skip2[j] for j in assessments[i]])
    else:
        # df[i]=sum([df[j] for j in assessments[i]])/len(assessments[i])
        df[i+"_num"]=df[assessments[i]].lt(1000).sum(axis=1)-2
        tmp=np.sort(df[assessments[i]], axis=1)[:, 2:]
        tmp=np.append(tmp,df[assessments_extracredit[i]],axis=1)
        df[i] = ((tmp<1000)*tmp).sum(1)/df[i+"_num"]


        # df_honors[i+"_num"]=df_honors[assessments[i]].lt(1000).sum(axis=1)-2
        # tmp_honors=np.sort(df_honors[assessments[i]], axis=1)[:, 2:]
        # tmp_honors=np.append(tmp_honors,df_honors[assessments_extracredit[i]],axis=1)
        # df_honors[i] = ((tmp_honors<1000)*tmp_honors).sum(1)/df_honors[i+"_num"]

        # tmp_honors=np.sort(df_honors[assessments[i]], axis=1)[:, 2:]
        # tmp_honors=np.append(tmp_honors,df_honors[assessments_extracredit[i]],axis=1)
        # df_honors[i] = tmp_honors.sum(1)/(len(assessments[i])-2)

df['total']=sum([
        df[i]*assessment_weights[i]
        for i in assessment_weights.keys()
        ]+[df["FCI"]*ec_weights['FCI']])*100#/total_norm*100

# df_honors['total']=sum([
#         df_honors[i]*assessment_weights[i]
#         for i in assessment_weights.keys()
#         ]+[df_honors["FCI"]*ec_weights['FCI'],df_honors["HONORS"]*ec_weights['HONORS']])*100#/total_norm*100




letters_intervals=np.array([0.,59.,63-0.005,67-0.005,70-0.005,73-0.005,77-0.005,80-0.005,83-0.005,87-0.005,90-0.005,93-0.005,97-0.005,1000])
letters_intervals=letters_intervals-5
print(letters_intervals)
letters=np.array(['F','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','A+'])
df['letter']=letters[np.searchsorted(letters_intervals, df['total'])-1]
# df_honors['letter']=letters[np.searchsorted(letters_intervals, df_honors['total'])-1]
print('105')
for i in letters:
    print(i,round(df[df['letter']==i].shape[0]/df.shape[0]*10000)/100,df[df['letter']==i].shape[0])
# print('125')
# for i in letters:
#     print(i,round(df_honors[df_honors['letter']==i].shape[0]/df_honors.shape[0]*10000)/100)

# df2=df.loc[df['Last Name'] == ""]
# df2=df.loc[df['First Name'] == ""]
# print(df2[['Last Name', 'First Name',"LAB_AVG","QUIZ_AVG","HW_AVG","EXAM_AVG",'FCI','total','letter']])

print('lab avg ',df['LAB_AVG'].mean())
print('lab quantile ',df['LAB_AVG'].quantile(0.33))
print('quiz avg ',df['QUIZ_AVG'].mean())
print('quiz quantile ',df['QUIZ_AVG'].quantile(0.25))
print('exam 1 ',df.loc[df['EXAM1']<1000,'EXAM1'].mean())
print('exam 1 q ',df.loc[df['EXAM1']<1000,'EXAM1'].quantile(0.33))
print('exam 2 ',df.loc[df['EXAM2']<1000,'EXAM2'].mean())
print('exam 2 q ',df.loc[df['EXAM2']<1000,'EXAM2'].quantile(0.33))
print('final ',df['FINAL'].mean())
print('final q ',df['FINAL'].quantile(0.33))

df.to_csv("grading-data/output.csv")
# df_honors.to_csv("grading-data/output_honors.csv")

df[['Username',"LAB_AVG","QUIZ_AVG","HW_AVG","EXAM_AVG",'total','letter']].to_csv("grading-data/output_bb.csv",float_format='%.2f')
# df_honors[['Username',"LAB_AVG","QUIZ_AVG","HW_AVG","EXAM_AVG",'total','letter']].to_csv("grading-data/output_honors_bb.csv")
  

