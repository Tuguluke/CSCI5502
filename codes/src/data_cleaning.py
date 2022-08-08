# data cleaning
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

h1b = pd.read_pickle("../data/hb1_2m_without_csharp.pkl")
h1b_test['state'] = h1b_test["LOCATION"].str[-2:]
column_name = h1b_test.columns.values.tolist()
column_name.remove("Dice_job_title")

states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

h1b_clean = h1b_test[h1b_test['state'].isin(states)]
h1b_clean["BASE SALARY"] = h1b_clean["BASE SALARY"].str.replace(
    ',', '').astype(int)

# box plot
list(h1b_clean.groupby('state')['BASE SALARY'].agg(count='size', mean_sent='mean').reset_index(
).sort_values(by=['count'], ascending=True).head(10).state)
ax = h1b_clean[h1b_clean['state'].isin(['WY', 'MT', 'AK', 'VT', 'ND', 'SD', 'WV', 'HI', 'ME', 'NM'])].boxplot(
    rot=45, fontsize=15,
    by='state', column=["BASE SALARY"])
title_boxplot = 'Box plot for bottom 10 state\'s salary'
plt.title(title_boxplot)
plt.suptitle('')  # that's what you're after
ax.set_xlabel("State")
ax = plt.show()


# define index column
h1b_timeseries = h1b_clean[h1b_clean['Dice_job_title'].isin(['Dynamics Functional Analyst',
                                                             'Director Infrastructure',
                                                            'F# Developer',
                                                             'Vulnerability Management Analyst',
                                                             'Vertica DBA',
                                                             'Avaya Engineer',
                                                             'VR Engineer',
                                                             'Desktop Support Analyst',
                                                             'Disaster Recovery Specialist',
                                                             'Epic Consultant'])].groupby(['Dice_job_title', 'start_year'])['Dice_job_title'].agg(count='size').reset_index()

h1b_timeseries.set_index('start_year', inplace=True)

# group data by product and display sales as line chart
ax = h1b_timeseries.groupby('Dice_job_title')[
    'count'].plot(legend=True, figsize=(10, 5))
title_timeplot = 'Time series plot for bottom 10 job\'s polularity'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()


h1b_timeseries = h1b_clean[h1b_clean['state'].isin(['WY', 'MT', 'AK', 'VT', 'ND', 'SD', 'WV', 'HI', 'ME', 'NM'])].groupby([
    'state', 'start_year'])['state'].agg(count='size').reset_index()

h1b_timeseries.set_index('start_year', inplace=True)

# group data by product and display sales as line chart
ax = h1b_timeseries.groupby('state')['count'].plot(
    legend=True, figsize=(10, 5))
title_timeplot = 'Time series plot for bottom 10 state\'s polularity'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()

ax = h1b_clean[h1b_clean['state'].isin(['CA', 'TX', 'NY',
                                        'NJ', 'IL', 'MA', 'GA', 'MI', 'FL', 'PA'])].boxplot(
    rot=45, fontsize=15,
    by='state', column=["BASE SALARY"])
title_boxplot = 'Box plot for top 10 state\'s salary'
plt.title(title_boxplot)
plt.suptitle('')  # that's what you're after
ax.set_xlabel("State")
ax = plt.show()

# Time series plot
h1b_timeseries = h1b_clean[h1b_clean['Dice_job_title'].isin(['Systems Analyst', 'Research Associate', 'Lead Engineer',
                                                             'Project Manager', 'Developer', 'Business Analyst',
                                                             'Network Engineer', 'Java Developer', 'Computer Systems Analyst',
                                                            'Application Developer'])].groupby(['Dice_job_title', 'start_year'])['Dice_job_title'].agg(count='size').reset_index()

h1b_timeseries.set_index('start_year', inplace=True)

# group data by product and display sales as line chart
ax = h1b_timeseries.groupby('Dice_job_title')[
    'count'].plot(legend=True, figsize=(10, 5))
title_timeplot = 'Time series plot for top 10 job\'s polularity'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()

h1b_clean.groupby(['Dice_job_title', 'start_year'])['Dice_job_title'].agg(
    count='size').reset_index().sort_values(by=['count'], ascending=False)


# H1b abusers
h1b_timeseries = h1b_clean[h1b_clean['EMPLOYER'].isin(['TATA CONSULTANCY SERVICES LIMITED',
                                                       'WIPRO LIMITED', 'IBM INDIA PRIVATE LIMITED',
                                                      'TECH MAHINDRA (AMERICAS)INC',
                                                       'L&T TECHNOLOGY SERVICES LIMITED',
                                                       'IBM CORPORATION', 'TECH MAHINDRA (AMERICAS) INC',
                                                       'MICROSOFT CORPORATION', 'GOOGLE LLC',
                                                       'LARSEN & TOUBRO INFOTECH LIMITED'])].groupby(['EMPLOYER', 'start_year'])['EMPLOYER'].agg(count='size').reset_index()

h1b_timeseries.set_index('start_year', inplace=True)

# group data by product and display sales as line chart
ax = h1b_timeseries.groupby('EMPLOYER')['count'].plot(
    legend=True, figsize=(10, 5))
title_timeplot = 'Time series plot for top 10 Employer\'s polularity'
plt.title(title_timeplot)
plt.suptitle('')  # that's what you're after
# ax.set_xlabel("Year");
ax = plt.show()
