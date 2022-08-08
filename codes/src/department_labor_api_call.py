# this is the script to get the BLS data for analysis
from io import BytesIO
import zipfile

import ipywidgets
import pandas as pd
import requests

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def load_data(year):
    url = 'https://www.bls.gov/oes/special.requests/oesm{}nat.zip'.format(
        year % 100)
    resp = requests.get(url)
    zf = zipfile.ZipFile(BytesIO(resp.content))
    for fi in zf.filelist:
        if fi.filename.rstrip('x').endswith('_dl.xls'):
            f = zf.read(fi)
            df = pd.read_excel(f)
            df.columns = df.columns.str.lower()
            df['year'] = year
            return df
    raise RuntimeError('Could not find correct Excel file within Zip archive.')


def load_years(years):
    frames = []
    for year in years:
        df = load_data(year)
        frames.append(df)
    return frames


df_all = pd.concat(load_years(range(2010, 2021)))
df_computer = df_all[df_all.occ_code.str.startswith('15')]

computer_titles = ['Computer and Mathematical Occupations',
                   'Computer and Information Research Scientists',
                   'Computer Systems Analysts', 'Computer Programmers',
                   'Software Developers, Applications',
                   'Software Developers, Systems Software', 'Database Administrators',
                   'Network and Computer Systems Administrators*',
                   'Computer Support Specialists',
                   'Information Security Analysts, Web Developers, and Computer Network Architects',
                   'Computer Occupations, All Other*', 'Actuaries', 'Mathematicians',
                   'Operations Research Analysts', 'Statisticians',
                   'Mathematical Technicians',
                   'Mathematical Science Occupations, All Other',
                   'Computer Occupations', 'Computer and Information Analysts',
                   'Information Security Analysts',
                   'Software Developers and Programmers', 'Web Developers',
                   'Database and Systems Administrators and Network Architects',
                   'Network and Computer Systems Administrators',
                   'Computer Network Architects', 'Computer User Support Specialists',
                   'Computer Network Support Specialists',
                   'Miscellaneous Computer Occupations',
                   'Computer Occupations, All Other',
                   'Mathematical Science Occupations',
                   'Miscellaneous Mathematical Science Occupations',
                   'Database and Network Administrators and Architects',
                   'Database Administrators and Architects',
                   'Software and Web Developers, Programmers, and Testers',
                   'Software Developers and Software Quality Assurance Analysts and Testers',
                   'Web Developers and Digital Interface Designers',
                   'Data Scientists and Mathematical Science Occupations, All Other']

df_computer['total employee'] = pd.to_numeric(
    df_computer['tot_emp'], errors='coerce')

df_computer['mean salary'] = pd.to_numeric(
    df_computer['a_mean'], errors='coerce')


# group data by product and display total employee as line chart

df_computer.set_index('year', inplace=True)
ax = df_computer.groupby('occ_title')['total employee'].plot(figsize=(10, 10))
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), prop={'size': 10})

title_timeplot = 'Deparment of Labour tech job total employee'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()

# salary plot
ax = df_farming.groupby('occ_title')['mean salary'].plot(figsize=(10, 10))
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), prop={'size': 15})

title_timeplot = 'Deparment of Labour farming job salary'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()


# import requests
# import json
# import prettytable
# headers = {'Content-type': 'application/json'}
# data = json.dumps({"seriesid": ['WMU00000001020000001730272400'],"startyear":"2020", "endyear":"2020"})
# p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
# json_data = json.loads(p.text)
# for series in json_data['Results']['series']:
#     x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
#     seriesId = series['seriesID']
#     for item in series['data']:
#         year = item['year']
#         period = item['period']
#         value = item['value']
#         footnotes=""
#         for footnote in item['footnotes']:
#             if footnote:
#                 footnotes = footnotes + footnote['text'] + ','
#         if 'M01' <= period <= 'M12':
#             x.add_row([seriesId,year,period,value,footnotes[0:-1]])
#     output = open(seriesId + '.txt','w')
#     output.write (x.get_string())
#     output.close()
