#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:41:15 2021

@author: mollybair
"""
# Objectives: Show examples of list comprehensions, and how to deal with 
# different python object types

import pandas as pd


# Problem 1: Take a list of strings and convert them into plural words.
singular_strings = ['apple', 'banana', 'orange', 'berry']
plural_strings = []
for string in singular_strings:
    if string[-1:] == 'y':  # if the string ends in y, plural form will be different
        temp = string[0:len(string)-1] + 'ies'
    else:
        temp = string + 's'
    plural_strings.append(temp)
print(plural_strings)


# Problem 2: Subset a list of values based on whether those values are present in another list
# Say we were trying to predict a person's income, and wanted to use backward
# selection to choose a model. 
# Solve with a for loop and with a list comprehension.
all_predictors = ['region', 'age', 'race', 'sex', 'educ', 'job_type']
removed = ['region']
remaining = []
for p in all_predictors:
    if p not in removed:
        remaining.append(p)
print(remaining)
remaining_predictors = [p for p in all_predictors if p not in removed]
print(remaining_predictors)


# Problem 3: Reshape a pandas dataframe and format date column
df = pd.read_csv('COVID Case Data.csv', nrows=23)
print(df.head())
df_stubnames = ['TOTAL CASES', 'BLACK CASES', 'HISPANIC CASES', 'WHITE CASES',\
                'BLACK CI', 'HISPANIC CI', 'WHITE CI']
df_panel = pd.wide_to_long(df, stubnames=df_stubnames, i='STATE', j='DATE',\
                           sep=' ').reset_index()
df_panel['DATE'] = pd.to_datetime(df_panel['DATE'], format='%y%m%d')
print(df_panel.head())


# Rewrite all three problems as functions
def plural_strings(singular_strings):
    plurals = []
    for string in singular_strings:
        if string[-1:] == 'y':
            temp = string[0:len(string)-1] + 'ies'
        else:
            temp = string + 's'
        plurals.append(temp)
    return plurals

def compare_lists(full_list, removed_values):
    remaining = []
    for value in full_list:
        if value not in removed_values:
            remaining.append(value)
    return remaining

def reshape_and_format(df, stubnames, i, j, dt_format):
    df_panel = pd.wide_to_long(df, stubnames=stubnames, i=i, j=j,\
                               sep=' ').reset_index()
    df_panel[j] = pd.to_datetime(df_panel[j], format=dt_format)
    return df_panel

def main():
    single_fruits = ['apple', 'banana', 'orange', 'berry']
    plural_fruits = plural_strings(single_fruits)
    
    all_predictors = ['region', 'age', 'race', 'sex', 'educ', 'job_type']
    removed = ['region']
    remaining_predictors = compare_lists(all_predictors, removed)
    
    cases = pd.read_csv('COVID Case Data.csv', nrows=23)
    cases_stubnames = ['TOTAL CASES', 'BLACK CASES', 'HISPANIC CASES', 'WHITE CASES',\
                'BLACK CI', 'HISPANIC CI', 'WHITE CI']
    cases_panel = reshape_and_format(cases, cases_stubnames, 'STATE', 'DATE',\
                                     '%y%m%d')
    print(cases_panel.head())

    















