import pandas as pd,json

# df = pd.read_csv('grading-data/gc_10683.202310_fullgc_2023-03-15-03-05-56.csv')
df = pd.read_csv('grading-data/gc_11035.202310_fullgc_2023-03-15-04-47-12.csv')

print(df.columns)

max_points={
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


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202844':			100,
'One D Motion Experiment [Total Pts: 100 Score] |3207326':		100,
"Newton's Laws Experiment [Total Pts: 100 Score] |3210663":		100,
'Friction Lab [Total Pts: 100 Score] |3217406':					100,
'Work and Energy Lab [Total Pts: 100 Score] |3220960':			100,
'Spring Simulation [Total Pts: 370 Score] |3222989':			370,
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228374':			100,
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232803':		100,


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211456':			5,
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218068':			4,
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221458':			3,
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224878':			4,
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229364':			4,
'Quiz 6 [Total Pts: 4 Score] |3232860':							4,


'Unit Exam I [Total Pts: 0 Text] |3225572':						100,
}

columns_to_rename={
'Homework set #1 [Total Pts: 65 Score] |3229258':				"HW1",
'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229259':	"HW1E",

'Homework set #2 [Total Pts: 57 Score] |3229260':				"HW2",
'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229261':	"HW2E",

'Homework set #3 [Total Pts: 30 Score] |3229262':				"HW3",
'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229263':	"HW3E",

'Homework set #4 [Total Pts: 79 Score] |3229264':				"HW4",
'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229265':"HW4E",

'Homework set #5 [Total Pts: 45 Score] |3229266':				"HW5",
'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229267':	"HW5E",

'Homework set #6 [Total Pts: 77 Score] |3231530':				"HW6",
'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231531':	"HW6E",


'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202844':			"LAB_ERROR",
'One D Motion Experiment [Total Pts: 100 Score] |3207326':		"LAB_1D",
"Newton's Laws Experiment [Total Pts: 100 Score] |3210663":		"LAB_NEWTON",
'Friction Lab [Total Pts: 100 Score] |3217406':					"LAB_FRICTION",
'Work and Energy Lab [Total Pts: 100 Score] |3220960':			"LAB_ENERGY",
'Spring Simulation [Total Pts: 370 Score] |3222989':			"LAB_SPRING",
'Linear Momeuntum Lab [Total Pts: 100 Score] |3228374':			"LAB_MOMENTUM",
'Rotational Dynamics Lab [Total Pts: 100 Score] |3232803':		"LAB_ROTATIONAL",


'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211456':			"QUIZ1",
'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218068':			"QUIZ2",
'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221458':			"QUIZ3",
'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224878':			"QUIZ4",
'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229364':			"QUIZ5",
'Quiz 6 [Total Pts: 4 Score] |3232860':							"QUIZ6",

'Unit Exam I [Total Pts: 0 Text] |3225572':						"EXAM1",
}


columns_to_rename_honors={
}

max_points_honors={
}


Index(['Last Name', 'First Name', 'Username', 'Student ID', 'Last Access',
       'Availability',
       'Homework set #1 (honors) [Total Pts: 66 Score] |3229300',
       'Homework set #4 (honors) [Total Pts: 80 Score] |3229306',
       'Homework set #3 (honors) [Total Pts: 31 Score] |3229304',
       'Homework set #2 (honors) [Total Pts: 60 Score] |3229303',
       'Homework set #2 [EXTRA CREDIT] [Total Pts: 6 Score] |3229302',
       'Homework set #5 (honors) [Total Pts: 45 Score] |3229308',
       'Homework set #3 [EXTRA CREDIT] [Total Pts: 4 Score] |3229305',
       'Homework set #5 [EXTRA CREDIT] [Total Pts: 4 Score] |3229309',
       'Homework set #4 [EXTRA CREDIT] [Total Pts: 14 Score] |3229307',
       'Homework set #1 [EXTRA CREDIT] [Total Pts: 4 Score] |3229301',
       'Homework set #6 (honors) [Total Pts: 82 Score] |3231533',
       'Homework set #6 [EXTRA CREDIT] [Total Pts: 8 Score] |3231532',
       'Weighted Total [Total Pts: up to 0 Percentage] |3032235',
       'Total [Total Pts: up to 1,499 Score] |3032234',
       'Honors project -- Letter [Total Pts: 1 Complete/Incomplete] |3197432',
       'ERROR ANALYSIS LAB [Total Pts: 100 Score] |3202882',
       'LAB2: ONE DIM M [Total Pts: 100 Score] |3207346',
       "Newton's Laws Experiment [Total Pts: 100 Score] |3210665",
       'Quiz 1 -- answer sheet [Total Pts: 5 Score] |3211459',
       'Friction Lab [Total Pts: 100 Score] |3217488',
       'Quiz 2 -- answer sheet [Total Pts: 4 Score] |3218069',
       'Work and Energy Lab [Total Pts: 100 Score] |3220961',
       'Quiz 3 -- answer sheet [Total Pts: 3 Score] |3221459',
       'Spring Simulation [Total Pts: 370 Score] |3223686',
       'Quiz 4 -- answer sheet [Total Pts: 4 Score] |3224881',
       'Unit Exam I [Total Pts: 0 Text] |3225571',
       'Linear Momeuntum Lab [Total Pts: 100 Score] |3228378',
       'Quiz 5 -- answer sheet [Total Pts: 4 Score] |3229374',
       'Rotational Dynamics Lab [Total Pts: 100 Score] |3232804',
       'Quiz 6 [Total Pts: 4 Score] |3232864'],
      dtype='object')




hw_extra_credit_weights={
	"HW1E": 0.1,
	"HW2E": 0.1,
	"HW3E": 0.15,
	"HW4E": 0.1,
	"HW5E": 0.1,
	"HW6E": 0.1,
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

for col in data.columns:
    if col.



f_waivers = open('waivers.json')
waivers = json.load(f_waivers)
f_waivers.close()
  
# Iterating through the json
# list
for i in waivers['student']:
    print(i)
  

