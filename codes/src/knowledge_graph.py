# this is script to run knowledge graph analysis
import networkx as ntx
import matplotlib.pyplot as plot
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy
import requests
import spacy
from tqdm import tqdm
import concurrent.futures
pandas as pd
# import en_core_web_sm

nlp = spacy.load('en_core_web_sm')


# %matplotlib inline

tech_skill = pd.read_csv('TechandGrayAreaJobTitles_relatedSkills.csv')
tech_skill['skill_list'] = tech_skill.relatedSkills.str.split(';')
# dataset = tech_skill.skill_list.dropna().tolist()


def obtain_relation(sent):
    doc = nlp(sent)

    matcher = Matcher(nlp.vocab)

    pattern = [{'DEP': 'ROOT'},
               {'DEP': 'prep', 'OP': "?"},
               {'DEP': 'agent', 'OP': "?"},
               {'POS': 'ADJ', 'OP': "?"}]

    matcher.add("matching_1", None, pattern)

    matcher = matcher(doc)
    h = len(matcher) - 1
    span = doc[matcher[h][1]:matcher[h][2]]

    return (span.text)


data = tech_skill.dropna()     # for relations

# subject extraction
source = [j[0] for j in new_list]

# object extraction
target = [k[1] for k in new_list]

data_kgf = pd.DataFrame(
    {'source': source, 'target': target, 'edge': relations})
# Create DG from the dataframe
graph = ntx.from_pandas_edgelist(data_kgf, "source", "target",
                                 edge_attr=True, create_using=ntx.MultiDiGraph())

# plotting the network
plot.figure(figsize=(14, 14))
posn = ntx.spring_layout(graph)
ntx.draw(graph, with_labels=True, node_color='green',
         edge_cmap=plot.cm.Blues, pos=posn)
plot.show()

# plot the knowledge graph
graph = ntx.from_pandas_edgelist(data_kgf[data_kgf['edge'] == "support"], "source", "target",
                                 edge_attr=True, create_using=ntx.MultiDiGraph())

plot.figure(figsize=(14, 14))
pos = ntx.spring_layout(graph, k=0.5)  # k regulates the distance between nodes
ntx.draw(graph, with_labels=True, node_color='green',
         node_size=1400, edge_cmap=plot.cm.Blues, pos=posn)
plot.show()
