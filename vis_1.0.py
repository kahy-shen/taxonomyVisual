# -*- coding: utf-8 -*-
# @Time    : 9/17/20 11:03 PM
# @Author  : Kay
# @Email   : kahy.shen@gmail.com
# @File    : visualization.py
# @Desc    :

import csv
import networkx as nx
import math
import argparse
import os
import json
def readcsv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        rows = [rows[i] for i in range(len(rows)) if i != 0]
        # nodes = list(set([line[1] for line in rows]))
        edges = [(line[-2], line[1]) for line in rows]
        # print(edges)
        csvfile.close()
    G = nx.Graph()
    # G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G


def diGraph(G):
    G_ = nx.DiGraph()
    G_.add_node("ROOT")
    # G_.add_edges_from([("ROOT", n) for n in G.neighbors("ROOT")])

    for n in G.nodes():
        for n_ in G.neighbors(n):
            if n_ in G.nodes():
                if len(nx.shortest_path(G, "ROOT", n)) > len(nx.shortest_path(G, "ROOT", n_)):
                    G_.add_edge(n_, n)
                else:
                    G_.add_edge(n, n_)
    return G_

def renew_digraph(G_, path):
    G__ = nx.DiGraph()
    nodesList = list(G_.nodes())
    nodes_id = {n: nodesList.index(n) for n in G_.nodes()}
    nodes_id["ROOT"] = -1
    for n in G_.nodes():
        # print(n, nodes_id[n])
        G__.add_node(nodes_id[n], name=n)
    # print(G_.nodes["ROOT"])
    for e in G_.edges():
        # print(e[0], e[1])
        G__.add_edge(nodes_id[e[0]], nodes_id[e[1]])
    output = nx.tree_data(G__, nodes_id["ROOT"])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, ensure_ascii=False, indent="\t"))



def visualization(input_name, output_dir, filename):
    print(output_dir, filename)
    G = readcsv(input_name)
    G_ = diGraph(G)
    renew_digraph(G_, "{}{}_d3.json".format(output_dir, filename.split(".")[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default="/Users/keshen/Documents/ISI/zero_shot_taxonomy/"
                                                     "FREP_Yahoo_Product_Taxonomies/data/output_concepts.csv")
    parser.add_argument('--output', type=str, default="/Users/keshen/Documents/ISI/zero_shot_taxonomy/"
                                                      "FREP_Yahoo_Product_Taxonomies/data/")
    args = parser.parse_args()
    input_dir = args.input
    output_dir = args.output

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    if os.path.isdir(args.input):
        files = os.listdir(args.input)
        for file in files:
            # print(file)
            if file.split(".")[-1] == 'csv':
                # print(file)
                filename = "{}/{}".format(args.input, file)
                visualization(filename, output_dir, file)

    elif os.path.isfile(args.input):
        visualization(input_dir, output_dir, input_dir.split('/')[-1])
        # print(args.input, args.input.split('/')[-1])

    else:
        print("illegal input")