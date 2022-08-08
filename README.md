# CSCI5502
Graduate Class Data Mining Project

## Project title
Mining the US Technologists Data

## Team members
Abulitibu Tuguluke (Group 5)
## Description of the project

Several studies have reported the US will face an even bigger tech talent shortages in the near future, which will translate into revenue decreases.  In this report, we will study the US technologist data through varies  mining techniques, by first introducing the US department of labor data along with H1b record (due to its partially reflective and openness). We then introduce the technologist concept along with data scrapping technique we applied to obtain the dataset. After carefully processing the data with exploratory analysis, we will try to understand the technologist trends such as: Which job title is becoming more popular and which one is not. The only machine learning algorithm for this project will be semi-unsupervised clustering, through which we will try to answer the utmost question of which tech skill set is becoming more demanding, and which can help our ultimate aim of recommending the right skill sets for the future tech job-seekers.
Our study shows that on top of tech talent demand in US are on the rise, is cloud engineering and project management skills will be in huge demand, while SQL and system analysis are in decline. Java still grows strong as python has not yet replace its spot, and Software developers should not worry that data scientists will make their job obsolete, as least not yet.  The report will end with conclusion along  the future work that can be study along the way.

## Summary of the question(s) sought and the answers
We successfully  mined the top 10 job titles that are in demand, they are: System analyst, Developer, Business Analyst, Computer System analyst, System Administrator, Project manager, Java Developer, System engineer, Application Developer. Lead Engineer. As opposed to media's champion: Data scientist and ML engineer. Next, we will explore the skill trend. Figure \ref{trending} shows us a clear image of what are the top skill that dominate each year's skill. QA and Software developer ranked 1 and 2 with no decline in sight. System analyst, on the other hand, is  becoming less popular over the year, probably due to job automation, so is SQL. Cloud computing is on the rise, along with agile, it is a clear sign that cloud engineering and project management will be in huge demand in the future.

## Application of this knowledge
-  There are infinite fields that our knowledge gain from this project be applied to. First, is the bigger picture of technology demand in  the US. For any recruiting company, the huge demand of particular job titles are the first thing they should pay attention to, since it is considered the 21st century capital, and need to compete for.
-   Second is for job market on which skill-sets are in need so that job-seekers can have a better vision. Words like 'A.I.' and 'Machine learning' are too vague to be focused on, while skill-set from our cluster study shows that:
-  Third, there can be a better job category mapping within the knowledge gained, how and why certain jobs should be labeled as the same title with text clustering and Fuzzy matching.
Many applications can be achieved with the future work on the same topic, due to the time limit for this project, we will sketch out the big picture for the future study in the next section.

*  Link to the video demonstration
[contributing guidelines](https://reponame/blob/master/CONTRIBUTING.md)
* [link](https://reponame/blob/master/CONTRIBUTING.md) to the final project paper

* [link](https://public.tableau.com/app/profile/abulitibu.tuguluke/viz/H1BApplicationsv2/H1BJobs?publish=yes) to the interactive dashboard

## Folder strcture
```text
All the PDFs/
text_project/
└── Part 1--7/
    ├── .tex
    └── .pdf
    └── .README
codes/
└── scrapped_data/
│   └── .json
└── src/
    ├── .py
    └── notebooks/
    │   └── .ipynb
    └── .tex
```
