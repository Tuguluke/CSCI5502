# the script to get imort the tech job title and the scrape each Job_Title
# into a seperate json file
from h1b_scraper import H1B_Scraper
import pandas as pd
import json
from glob import glob
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

jobs = pd.read_csv('TechandGrayAreaJobTitles_relatedSkills.csv')
dice_job = list(jobs.Job_Title)


def where_json(file_name):
    return os.path.exists(file_name)


def remove_words(list1, remove_words):
    for word in list(list1):
        if word in remove_words:
            list1.remove(word)
    return list1


scraper = H1B_Scraper()
years = [year for year in range(2010, 2021)]
for job in jobs_names:
    if where_json('./data/table_' + str(job)+'.json'):
        pass
    else:
        try:
            tables = scraper.scrape(years, [job])
            tables.to_json('./data/table_' + str(job)+'.json')
        except:
            pass


# less_dice_job = remove_words(dice_job, ['C# Application Developer', 'C# Developer'])
##
##big_table = pd.DataFrame()
# for i in less_dice_job:
# try:
##        f = open ('./data/table_'+ i +'.json', "r")
# Reading from file
##        data = json.loads(f.read())
# except:
# continue
# pd.DataFrame(data).fillna("nan")
##    table = pd.DataFrame()
##    medim_df = pd.DataFrame()
##    temp_df = pd.DataFrame()
##    scraper = H1B_Scraper()
##    years = [year for year in range(2010, 2021)]
# for year in years:
# print(year)
# for job in [i]:
# print(jobs)
# df = pd.DataFrame(scraper.extract_specific_table(tables, year, job))
##           temp_df = pd.DataFrame(scraper.extract_specific_table(pd.DataFrame(data), year, job))
##           medim_df = medim_df.append(temp_df)
##        table = table.append(medim_df)
##        table['Dice_job_title'] = i
##    big_table = big_table.append(table)
##
# new = pd.merge(big_table, jobs, left_on=  ['Dice_job_title'],
##                   right_on= ['Job_Title'],
# how = 'left')
# new.to_pickle('hb1_2m_without_csharp.pkl')
