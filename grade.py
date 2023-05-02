import pandas as pd,json,numpy as np

# df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-03-15-03-05-56.csv')
# df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-03-15-04-47-12.csv')

df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-05-01-11-00-30.csv')
df_honors = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-05-01-10-58-49.csv')

# print(df)
df=df.fillna(0)
print(df)

max_points_raw={
'Homework set #1 [Total Pts: 65 Score] |3229258':				65,
'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229259':	4,

'Homework set #2 [Total Pts: 57 Score] |3229260':				57,
'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229261':	6,

'Homework set #3 [Total Pts: 30 Score] |3229262':				30,
'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229263':	4,

'Homework set #4 [Total Pts: 79 Score] |3229264':				79,
'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229265':14,

'Homework set #5 [Total Pts: 45 Score] |3229266':				45,
'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229267':	4,

'Homework set #6 [Total Pts: 77 Score] |3231530':				77,
'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231531':	8,

"Homework set #7 [Total Pts: 50 Score] |3238191":                50,
"Homework set #7 [EXTRA CREDIT] [Total Pts: 11 Score] |3238192": 11,

"Homework set #8 [Total Pts: 26 Score] |3241590":                26,
"Homework set #8 [EXTRA CREDIT] [Total Pts: 11 Score] |3241591": 11,

"Homework set #9 [Total Pts: 79 Score] |3250662":                79,
"Homework set #9 [EXTRA CREDIT] [Total Pts: 1 Score] |3250663":  1,

"Homework set #10 [Total Pts: 120 Score] |3250664":              120,
"Homework set #10 [EXTRA CREDIT] [Total Pts: 6 Score] |3250665": 6,

"Homework set #11 [EXTRA CREDIT] [Total Pts: 81 Score] |3263798":81,


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202844':			100,
'One D Motion Experiment [Total Pts: 100 Score] |3207326':		100,
"Newton's Laws Experiment [Total Pts: 100 Score] |3210663":		100,
'Friction Lab [Total Pts: 100 Score] |3217406':					100,
'Work and Energy Lab [Total Pts: 100 Score] |3220960':			100,
'Spring Simulation [Total Pts: 370 Score] |3222989':			370,
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228374':			100,
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232803':		100,
"Gravity Simulation [Total Pts: 290 Score] |3235284":           290,
"Archimedes' Principle Lab [Total Pts: 100 Score] |3240360":    100,
"SHM Lab [Total Pts: 100 Score] |3244588":                      100,
"Standing Wave Lab [Total Pts: 100 Score] |3256661":            100,
"Ideal Gas Law Lab [Total Pts: 100 Score] |3264798":            100,
"Calorimetry Lab (EC) [Total Pts: 100 Score] |3269505":         100,


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211456':			5,
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218068':			4,
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221458':			3,
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224878':			4,
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229364':			4,
'Quiz 6 [Total Pts: 4 Score] |3232860':							4,
"Quiz 7 -- answer sheet [Total Pts: 4 Score] |3237288":         4,
"Quiz 8 [Total Pts: 3 Score] |3239647":                         3,
"Quiz 9 [Total Pts: 40 Score] |3245723":                        40,
"Quiz 10 [Total Pts: 4 Score] |3260548":                        4,
"Quiz 11 -- answer sheet [Total Pts: 4 Score] |3265441":        4,

'Unit Exam I [Total Pts: 0 Text] |3225572':						100,
"Unit Exam 2 [Total Pts: 0 Text] |3248067":                     100,
"FCI VERII Percentage Score [Total Pts: 0 Text] |3239696":      100,



}

columns_to_rename={
'Homework set #1 [Total Pts: 65 Score] |3229258':				"HW1B",
'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229259':	"HW1E",

'Homework set #2 [Total Pts: 57 Score] |3229260':				"HW2B",
'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229261':	"HW2E",

'Homework set #3 [Total Pts: 30 Score] |3229262':				"HW3B",
'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229263':	"HW3E",

'Homework set #4 [Total Pts: 79 Score] |3229264':				"HW4B",
'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229265':"HW4E",

'Homework set #5 [Total Pts: 45 Score] |3229266':				"HW5B",
'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229267':	"HW5E",

'Homework set #6 [Total Pts: 77 Score] |3231530':				"HW6B",
'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231531':	"HW6E",

"Homework set #7 [Total Pts: 50 Score] |3238191":                'HW7B',
"Homework set #7 [EXTRA CREDIT] [Total Pts: 11 Score] |3238192": 'HW7E',

"Homework set #8 [Total Pts: 26 Score] |3241590":                'HW8B',
"Homework set #8 [EXTRA CREDIT] [Total Pts: 11 Score] |3241591": 'HW8E',

"Homework set #9 [Total Pts: 79 Score] |3250662":                'HW9B',
"Homework set #9 [EXTRA CREDIT] [Total Pts: 1 Score] |3250663":  'HW9E',

"Homework set #10 [Total Pts: 120 Score] |3250664":              'HW10B',
"Homework set #10 [EXTRA CREDIT] [Total Pts: 6 Score] |3250665": 'HW10E',

"Homework set #11 [EXTRA CREDIT] [Total Pts: 81 Score] |3263798": 'HW11',


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202844':			"LAB_ERROR",
'One D Motion Experiment [Total Pts: 100 Score] |3207326':		"LAB_1D",
"Newton's Laws Experiment [Total Pts: 100 Score] |3210663":		"LAB_NEWTON",
'Friction Lab [Total Pts: 100 Score] |3217406':					"LAB_FRICTION",
'Work and Energy Lab [Total Pts: 100 Score] |3220960':			"LAB_ENERGY",
'Spring Simulation [Total Pts: 370 Score] |3222989':			"LAB_SPRING",
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228374':			"LAB_MOMENTUM",
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232803':		"LAB_ROTATIONAL",
"Gravity Simulation [Total Pts: 290 Score] |3235284":           'LAB_GRAVITY',
"Archimedes' Principle Lab [Total Pts: 100 Score] |3240360":    'LAB_ARCHIMEDE',
"SHM Lab [Total Pts: 100 Score] |3244588":                      'LAB_SHM',
"Standing Wave Lab [Total Pts: 100 Score] |3256661":            'LAB_WAVE',
"Ideal Gas Law Lab [Total Pts: 100 Score] |3264798":            'LAB_GAS',
"Calorimetry Lab (EC) [Total Pts: 100 Score] |3269505":         'LAB_CALORIMETRY',


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211456':			"QUIZ1",
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218068':			"QUIZ2",
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221458':			"QUIZ3",
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224878':			"QUIZ4",
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229364':			"QUIZ5",
'Quiz 6 [Total Pts: 4 Score] |3232860':							"QUIZ6",
"Quiz 7 -- answer sheet [Total Pts: 4 Score] |3237288":         'QUIZ7',
"Quiz 8 [Total Pts: 3 Score] |3239647":                         'QUIZ8',
"Quiz 9 [Total Pts: 40 Score] |3245723":                        'QUIZ9',
"Quiz 10 [Total Pts: 4 Score] |3260548":                        'QUIZ10',
"Quiz 11 -- answer sheet [Total Pts: 4 Score] |3265441":        'QUIZ11',

'Unit Exam I [Total Pts: 0 Text] |3225572':						"EXAM1",
"Unit Exam 2 [Total Pts: 0 Text] |3248067":                     'EXAM2',
"FCI VERII Percentage Score [Total Pts: 0 Text] |3239696":      'FCI',

}

max_points={}
for i in max_points_raw.keys():
    max_points[columns_to_rename[i]]=max_points_raw[i]



columns_to_rename_honors={
'Homework set #1 (honors) [Total Pts: 66 Score] |3229300':              "HW1B",
'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229301':         "HW1E",

'Homework set #2 (honors) [Total Pts: 60 Score] |3229303':              "HW2B",
'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229302':         "HW2E",

'Homework set #3 (honors) [Total Pts: 31 Score] |3229304':              "HW3B",
'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229305':         "HW3E",

'Homework set #4 (honors) [Total Pts: 80 Score] |3229306':              "HW4B",
'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229307':        "HW4E",

'Homework set #5 (honors) [Total Pts: 45 Score] |3229308':              "HW5B",
'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229309':         "HW5E",

'Homework set #6 (honors) [Total Pts: 82 Score] |3231533':              "HW6B",
'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231532':         "HW6E",

"Homework set #7 (honors) [Total Pts: 53 Score] |3238194":              "HW7B",
"Homework set #7 [EXTRA CREDIT] [Total Pts: 11 Score] |3238193":        "HW7E",

"Homework set #8 (honors) [Total Pts: 27 Score] |3241593":              "HW8B",
"Homework set #8 [EXTRA CREDIT] [Total Pts: 11 Score] |3241594":        "HW8E",

"Homework set #9 (honors) [Total Pts: 81 Score] |3250669":              "HW9B",
"Homework set #9 [EXTRA CREDIT] [Total Pts: 1 Score] |3250670":         "HW9E",

"Homework set #10 (honors) [Total Pts: 123 Score] |3250671":            "HW10B",
"Homework set #10 [EXTRA CREDIT] [Total Pts: 6 Score] |3250672":        "HW10E",

"Homework set #11 [EXTRA CREDIT] [Total Pts: 81 Score] |3263797":       "HW11",


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202882':                   "LAB_ERROR",
'LAB2: ONE DIM M [Total Pts: 100 Score] |3207346':                      "LAB_1D",
"Newton's Laws Experiment [Total Pts: 100 Score] |3210665":             "LAB_NEWTON",
'Friction Lab [Total Pts: 100 Score] |3217488':                         "LAB_FRICTION",
'Work and Energy Lab [Total Pts: 100 Score] |3220961':                  "LAB_ENERGY",
'Spring Simulation [Total Pts: 370 Score] |3223686':                    "LAB_SPRING",
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228378':                 "LAB_MOMENTUM",
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232804':              "LAB_ROTATIONAL",
"Gravity Simulation [Total Pts: 290 Score] |3235287":                   "LAB_GRAVITY",
"Archimedes' Principle Lab [Total Pts: 100 Score] |3240361":            "LAB_ARCHIMEDE",
"SHM Lab [Total Pts: 100 Score] |3244592":                              "LAB_SHM",
"Standing Wave Lab [Total Pts: 100 Score] |3256664":                    "LAB_WAVE",
"Ideal Gas Law Lab [Total Pts: 100 Score] |3264804":                    "LAB_GAS",
"Calorimetry Lab (EC) [Total Pts: 100 Score] |3269594":                 "LAB_CALORIMETRY",


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211459':                 "QUIZ1",
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218069':                 "QUIZ2",
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221459':                 "QUIZ3",
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224881':                 "QUIZ4",
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229374':                 "QUIZ5",
'Quiz 6 [Total Pts: 4 Score] |3232864':                                 "QUIZ6",
"Quiz 7 -- answer sheet [Total Pts: 4 Score] |3237289":                 "QUIZ7",
"Quiz 8 [Total Pts: 3 Score] |3239652":                                 "QUIZ8",
"Quiz 9 [Total Pts: 40 Score] |3245719":                                "QUIZ9",
"Quiz 10 [Total Pts: 4 Score] |3260551":                                "QUIZ10",
"Quiz 11 -- answer sheet [Total Pts: 4 Score] |3265449":                "QUIZ11",

'Unit Exam I [Total Pts: 0 Text] |3225571':                             "EXAM1",
"Unit Exam 2 [Total Pts: 0 Text] |3248068":                             "EXAM2",
"FCI VERII Percentage Score [Total Pts: 0 Text] |3239697":              "FCI",
"Honors Project -- Report [Total Pts: 100 Score] |3263847":             "HONORS",
}

max_points_honors_raw={
'Homework set #1 (honors) [Total Pts: 66 Score] |3229300':              66,
'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229301':         4,

'Homework set #2 (honors) [Total Pts: 60 Score] |3229303':              60,
'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229302':         6,

'Homework set #3 (honors) [Total Pts: 31 Score] |3229304':              31,
'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229305':         4,

'Homework set #4 (honors) [Total Pts: 80 Score] |3229306':              80,
'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229307':        14,

'Homework set #5 (honors) [Total Pts: 45 Score] |3229308':              45,
'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229309':         4,

'Homework set #6 (honors) [Total Pts: 82 Score] |3231533':              82,
'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231532':         8,

"Homework set #7 (honors) [Total Pts: 53 Score] |3238194":              53,
"Homework set #7 [EXTRA CREDIT] [Total Pts: 11 Score] |3238193":        11,

"Homework set #8 (honors) [Total Pts: 27 Score] |3241593":              27,
"Homework set #8 [EXTRA CREDIT] [Total Pts: 11 Score] |3241594":        11,

"Homework set #9 (honors) [Total Pts: 81 Score] |3250669":              81,
"Homework set #9 [EXTRA CREDIT] [Total Pts: 1 Score] |3250670":         1,

"Homework set #10 (honors) [Total Pts: 123 Score] |3250671":            123,
"Homework set #10 [EXTRA CREDIT] [Total Pts: 6 Score] |3250672":        6,

"Homework set #11 [EXTRA CREDIT] [Total Pts: 81 Score] |3263797":       81,


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202882':                   100,
'LAB2: ONE DIM M [Total Pts: 100 Score] |3207346':                      100,
"Newton's Laws Experiment [Total Pts: 100 Score] |3210665":             100,
'Friction Lab [Total Pts: 100 Score] |3217488':                         100,
'Work and Energy Lab [Total Pts: 100 Score] |3220961':                  100,
'Spring Simulation [Total Pts: 370 Score] |3223686':                    370,
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228378':                 100,
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232804':              100,
"Gravity Simulation [Total Pts: 290 Score] |3235287":                   290,
"Archimedes' Principle Lab [Total Pts: 100 Score] |3240361":            100,
"SHM Lab [Total Pts: 100 Score] |3244592":                              100,
"Standing Wave Lab [Total Pts: 100 Score] |3256664":                    100,
"Ideal Gas Law Lab [Total Pts: 100 Score] |3264804":                    100,
"Calorimetry Lab (EC) [Total Pts: 100 Score] |3269594":                 100,


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211459':                 5,
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218069':                 4,
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221459':                 3,
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224881':                 4,
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229374':                 4,
'Quiz 6 [Total Pts: 4 Score] |3232864':                                 4,
"Quiz 7 -- answer sheet [Total Pts: 4 Score] |3237289":                 4,
"Quiz 8 [Total Pts: 3 Score] |3239652":                                 3,
"Quiz 9 [Total Pts: 40 Score] |3245719":                                40,
"Quiz 10 [Total Pts: 4 Score] |3260551":                                4,
"Quiz 11 -- answer sheet [Total Pts: 4 Score] |3265449":                4,

'Unit Exam I [Total Pts: 0 Text] |3225571':                             100,
"Unit Exam 2 [Total Pts: 0 Text] |3248068":                             100,
"FCI VERII Percentage Score [Total Pts: 0 Text] |3239697":              100,
"Honors Project -- Report [Total Pts: 100 Score] |3263847":             100,

}

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

assesment_weights={
    'LAB_AVG':0.2,
    'QUIZ_AVG':0.15,
    'EXAM_AVG':0.50,
    'HW_AVG':0.15,   
}

total_norm=sum([assesment_weights[i] for i in assesment_weights.keys()])#0.2+0.15+0.15+0.15
print(total_norm)


# Labs and/or simulations: 20%

# Homework problems: 15%

# Quizzes: 15%

# Exam 1: 15%

# Exam 2: 15%

# Final Exam: 20%

# "LAB_ERROR",
# "LAB_1D",
# "LAB_NEWTON",
# "LAB_FRICTION",
# "LAB_ENERGY",
# "LAB_SPRING",
# "LAB_MOMENTUM",
# "LAB_ROTATIONAL",

# for i in assessments.keys():
#     df[i] = np.sort(df[assessments[i]], axis=1)[:, 2:].append(df[assessments_extracredit[i]]).sum(1)/(len(assessments[i])-2)
# print (df)  

exam_weights=
{"EXAM1":0.3,
"EXAM2":0.3,
"FINAL":0.4}

for i in assessments.keys():
    if i=='EXAM_AVG':
        df[i]=sum([df[j]*exam_weights[j] for j in assessments[i]])
    else:
        df[i]=sum([df[j] for j in assessments[i]])/len(assessments[i])

df['total']=sum([
        df[i]*assesment_weights[i]
        for i in assesment_weights.keys()
        ])/total_norm*100

# df["Final_Fee"] = df["Fee"] - df["Discount"]

# for col in df.columns:
#     if col.
df2=df.loc[df['Last Name'] == "Murray"]
print(df2[['Last Name', 'First Name',"LAB_AVG","QUIZ_AVG","HW_AVG","EXAM_AVG",'total']])

# f_waivers = open('grading-data/waivers.json')
# waivers = json.load(f_waivers)
# f_waivers.close()
  
# Iterating through the json
# list
# for i in waivers['student']:
#     print(i)
  

