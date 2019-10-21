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
    
#### read from Json file ####
f = open("/Users/mahnaz_SSNL/Desktop/demo.json")
data = json.load(f)
f.close()


#### predefined variables ####
labels = ['pingTime',	'startTime'	,'endTime',	'participantID']
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



#### read stream namse  ####
for i in range(0,len(data['pingInfos'])):
    streamNames.append(data['pingInfos'][i]['id'])
    
#### read data from each stream and make the output ####
for i in range(0,len(data['pingInfos'])):
    temp_streamNames = ''.join([k for k in streamNames[i] if not k.isdigit()])
    temp_datas = [data['pingInfos'][i]['notificationTime'],data['pingInfos'][i]['startTime'],data['pingInfos'][i]['endTime'],data['patientId']]
    temp_varNames = list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())

#### change the values to 999 and NA ####
    for j in range(0, len(temp_varNames)):
        if data['pingStates'][streamNames[i]]['currentQuestionAnswers'][temp_varNames[j]]['nextWithoutOption']==True:
            temp_datas = temp_datas + ["NA"]
        elif data['pingStates'][streamNames[i]]['currentQuestionAnswers'][temp_varNames[j]]['preferNotToAnswer']==True:
            temp_datas = temp_datas + ["999"]
        else:   
            temp_datas = temp_datas + [data['pingStates'][streamNames[i]]['currentQuestionAnswers'][temp_varNames[j]]['data']]
    
#### create the output data for dataframe  ####  
    if temp_streamNames == "modal":
        if len(modal_Data)==0:
            modal_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        modal_Data.append(temp_datas) 
    elif temp_streamNames == "goal":
        if len(goal_Data)==0:
            goal_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        goal_Data.append(temp_datas)
    elif temp_streamNames == "laughter":
        if len(laughter_Data)==0:
            laughter_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        laughter_Data.append(temp_datas)
    elif temp_streamNames == "clossness":
        if len(clossness_Data)==0:
            clossness_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        clossness_Data.append(temp_datas)
    elif temp_streamNames == "interaction":
        if len(goal_Data)==0:
            interaction_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        interaction_Data.append(temp_datas)
    elif temp_streamNames == "stressor":
        if len(stressor_Data)==0:
            stressor_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        stressor_Data.append(temp_datas)
    elif temp_streamNames == "loneliness":
        if len(loneliness_Data)==0:
            loneliness_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        loneliness_Data.append(temp_datas)
    elif temp_streamNames == "anxiety":
        if len(anxiety_Data)==0:
            anxiety_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        anxiety_Data.append(temp_datas)
    elif temp_streamNames == "stressor_Follow_Up":
        if len(stressor_Follow_Up_Data)==0:
            stressor_Follow_Up_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        stressor_Follow_Up_Data.append(temp_datas)
    elif temp_streamNames == "loneliness_Follow_Up":
        if len(loneliness_Follow_Up_Data)==0:
            loneliness_Follow_Up_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        loneliness_Follow_Up_Data.append(temp_datas)
    elif temp_streamNames == "anxiety_Follow_Up":
        if len(anxiety_Follow_Up_Data)==0:
            anxiety_Follow_Up_varNames = labels + [f_toLower(s) for s in list(data['pingStates'][streamNames[i]]['currentQuestionAnswers'].keys())]
        anxiety_Follow_Up_Data.append(temp_datas)

    
#### create dataframe and csv file  ####
df_temp_modal = pd.DataFrame.from_records(modal_Data, columns=modal_varNames) 
f = df_temp_modal.to_csv("/Users/mahnaz_SSNL/Desktop/test_modal.csv")
df_temp_goal = pd.DataFrame.from_records(goal_Data, columns=goal_varNames) 
f = df_temp_goal.to_csv("/Users/mahnaz_SSNL/Desktop/test_goal.csv")
df_temp_laughter = pd.DataFrame.from_records(laughter_Data, columns=laughter_varNames) 
f = df_temp_laughter.to_csv("/Users/mahnaz_SSNL/Desktop/test_laughter.csv")
df_temp_clossness = pd.DataFrame.from_records(clossness_Data, columns=clossness_varNames) 
f = df_temp_clossness.to_csv("/Users/mahnaz_SSNL/Desktop/test_clossness.csv")
df_temp_interaction = pd.DataFrame.from_records(interaction_Data, columns=interaction_varNames) 
f = df_temp_interaction.to_csv("/Users/mahnaz_SSNL/Desktop/test_interaction.csv")
df_temp_stressor = pd.DataFrame.from_records(stressor_Data, columns=stressor_varNames) 
f = df_temp_stressor.to_csv("/Users/mahnaz_SSNL/Desktop/test_stressor.csv")
df_temp_loneliness = pd.DataFrame.from_records(loneliness_Data, columns=loneliness_varNames) 
f = df_temp_loneliness.to_csv("/Users/mahnaz_SSNL/Desktop/test_loneliness.csv")
df_temp_anxiety = pd.DataFrame.from_records(anxiety_Data, columns=anxiety_varNames)
f = df_temp_anxiety.to_csv("/Users/mahnaz_SSNL/Desktop/test_anxiety.csv")
df_temp_stressor_Follow_Up = pd.DataFrame.from_records(stressor_Follow_Up_Data, columns=stressor_Follow_Up_varNames) 
f = df_temp_stressor_Follow_Up.to_csv("/Users/mahnaz_SSNL/Desktop/test_stressor_Follow_Up.csv")
df_temp_loneliness_Follow_Up = pd.DataFrame.from_records(loneliness_Follow_Up_Data, columns=loneliness_Follow_Up_varNames) 
f = df_temp_loneliness_Follow_Up.to_csv("/Users/mahnaz_SSNL/Desktop/test_loneliness_Follow_Up.csv")
df_temp_anxiety_Follow_Up = pd.DataFrame.from_records(anxiety_Follow_Up_Data, columns=anxiety_Follow_Up_varNames) 
f = df_temp_anxiety_Follow_Up.to_csv("/Users/mahnaz_SSNL/Desktop/test_anxiety_Follow_Up.csv")

