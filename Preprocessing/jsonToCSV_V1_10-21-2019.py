#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:20:59 2019

@author: mahnaz_SSNL
"""
import json
import pandas as pd


#### function to convert the first char to lower case ####
def f_toLower(s):
    s = s[:3].lower() + s[3:] if s[0:2] =='NS' else s[:2].lower() + s[2:] 
    return s

#### read from json stream files (change the values to 999 and NA and "" if it's blank ####
def f_fillData(varNames, temp_varNames,streamNames, data, temp_datas):
    for j in range(4, len(varNames)):
        if varNames[j] in temp_varNames:
            if data['pingStates'][streamNames[i]]['currentQuestionAnswers'][varNames[j]]['nextWithoutOption']==True:
                temp_datas = temp_datas + ["NA"]
            elif data['pingStates'][streamNames[i]]['currentQuestionAnswers'][varNames[j]]['preferNotToAnswer']==True:
                temp_datas = temp_datas + ["999"]
            else:   
                temp_datas = temp_datas + [data['pingStates'][streamNames[i]]['currentQuestionAnswers'][varNames[j]]['data']]
        else:
                temp_datas = temp_datas + [""]
    print (i,streamNames[i],len(temp_varNames))
    return temp_datas 

#### path ####
path_in ="/Users/mahnaz_SSNL/Desktop/desktoplab/research/dormStudies/Scripts/PythonCode/JsonToCSV/input"
path_out ="/Users/mahnaz_SSNL/Desktop/desktoplab/research/dormStudies/Scripts/PythonCode/JsonToCSV/output"

#### read from variable names and make a list of them ####
df_var_names = pd.read_csv(path_in+"/var_names.csv")
modal_varNames = [n for n in list(df_var_names['Modal']) if str(n) != 'nan']
goal_varNames = [n for n in list(df_var_names['Goal']) if str(n) != 'nan']
laughter_varNames = [n for n in list(df_var_names['Laughter']) if str(n) != 'nan']
clossness_varNames = [n for n in list(df_var_names['Closeness']) if str(n) != 'nan']
interaction_varNames =  [n for n in list(df_var_names['Interaction']) if str(n) != 'nan']
stressor_varNames = [n for n in list(df_var_names['Stressor']) if str(n) != 'nan']
loneliness_varNames = [n for n in list(df_var_names['Loneliness']) if str(n) != 'nan']
anxiety_varNames = [n for n in list(df_var_names['Anxiety']) if str(n) != 'nan']
stressor_Follow_Up_varNames = [n for n in list(df_var_names['Stressor_Follow_Up']) if str(n) != 'nan']
loneliness_Follow_Up_varNames = [n for n in list(df_var_names['Loneliness_Follow_Up']) if str(n) != 'nan']
anxiety_Follow_Up_varNames = [n for n in list(df_var_names['Anxiety_Follow_Up']) if str(n) != 'nan']
 
    
#### read from Json file ####
f = open(path_in+"/demo3.json")
data = json.load(f)
f.close()


#### predefined variables ####
modal_Data = []
goal_Data = []
laughter_Data = []
clossness_Data = []
interaction_Data = [] 
stressor_Data = []
loneliness_Data = []
anxiety_Data = []
stressor_Follow_Up_Data = []
loneliness_Follow_Up_Data = []
anxiety_Follow_Up_Data = []
streamNames = []


#### read and make dataframe  ####
for i in range(0,len(data['pingInfos'])):
    streamNames.append(data['pingInfos'][i]['id'])
    
#### read data from each stream and make the output ####
for i in range(0,len(data['pingInfos'])):
    temp_streamNames = ''.join([k for k in streamNames[i] if not k.isdigit()])
    temp_datas = [data['pingInfos'][i]['notificationTime'],data['pingInfos'][i]['startTime'],data['pingInfos'][i]['endTime'],data['patientId']]
    temp_varNames = list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())

#### create the output data for dataframe  ####  
    if temp_streamNames == "modal":  
        modal_Data.append(f_fillData(modal_varNames, temp_varNames,streamNames, data, temp_datas )) 

    elif temp_streamNames == "goal":
        goal_Data.append(f_fillData(goal_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "laughter":
        laughter_Data.append(f_fillData(laughter_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "closeness":
        clossness_Data.append(f_fillData(clossness_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "interaction":
        interaction_Data.append(f_fillData(interaction_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "stressor":
        stressor_Data.append(f_fillData(stressor_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "loneliness":
        loneliness_Data.append(f_fillData(loneliness_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "anxiety":
        anxiety_Data.append(f_fillData(anxiety_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "stressor_Follow_Up":
        stressor_Follow_Up_Data.append(f_fillData(stressor_Follow_Up_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "loneliness_Follow_Up":
        loneliness_Follow_Up_Data.append(f_fillData(loneliness_Follow_Up_varNames, temp_varNames,streamNames, data, temp_datas ))
    
    elif temp_streamNames == "anxiety_Follow_Up":
        anxiety_Follow_Up_Data.append(f_fillData(anxiety_Follow_Up_varNames, temp_varNames,streamNames, data, temp_datas ))

    
#### create dataframe and csv file  ####
df_temp_modal = pd.DataFrame.from_records(modal_Data, columns=[f_toLower(s) for s in modal_varNames]) 
f = df_temp_modal.to_csv(path_out+"/modal.csv")
df_temp_goal = pd.DataFrame.from_records(goal_Data, columns=[f_toLower(s) for s in goal_varNames]) 
f = df_temp_goal.to_csv(path_out+"/goal.csv")
df_temp_laughter = pd.DataFrame.from_records(laughter_Data, columns=[f_toLower(s) for s in laughter_varNames]) 
f = df_temp_laughter.to_csv(path_out+"/laughter.csv")
df_temp_clossness = pd.DataFrame.from_records(clossness_Data, columns=[f_toLower(s) for s in clossness_varNames]) 
f = df_temp_clossness.to_csv(path_out+"/closeness.csv")
df_temp_interaction = pd.DataFrame.from_records(interaction_Data, columns=[f_toLower(s) for s in interaction_varNames]) 
f = df_temp_interaction.to_csv(path_out+"/interaction.csv")
df_temp_stressor = pd.DataFrame.from_records(stressor_Data, columns=[f_toLower(s) for s in stressor_varNames]) 
f = df_temp_stressor.to_csv(path_out+"/stressor.csv")
df_temp_loneliness = pd.DataFrame.from_records(loneliness_Data, columns=[f_toLower(s) for s in loneliness_varNames]) 
f = df_temp_loneliness.to_csv(path_out+"/loneliness.csv")
df_temp_anxiety = pd.DataFrame.from_records(anxiety_Data, columns=[f_toLower(s) for s in anxiety_varNames])
f = df_temp_anxiety.to_csv(path_out+"/anxiety.csv")
df_temp_stressor_Follow_Up = pd.DataFrame.from_records(stressor_Follow_Up_Data, columns=[f_toLower(s) for s in stressor_Follow_Up_varNames]) 
f = df_temp_stressor_Follow_Up.to_csv(path_out+"/stressor_Follow_Up.csv")
df_temp_loneliness_Follow_Up = pd.DataFrame.from_records(loneliness_Follow_Up_Data, columns=[f_toLower(s) for s in loneliness_Follow_Up_varNames]) 
f = df_temp_loneliness_Follow_Up.to_csv(path_out+"/loneliness_Follow_Up.csv")
df_temp_anxiety_Follow_Up = pd.DataFrame.from_records(anxiety_Follow_Up_Data, columns=[f_toLower(s) for s in anxiety_Follow_Up_varNames]) 
f = df_temp_anxiety_Follow_Up.to_csv(path_out+"/anxiety_Follow_Up.csv")

