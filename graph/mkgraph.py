#!/usr/bin/env python

import csv
import graphviz

graph = graphviz.Digraph()

with open("/Users/eric/shoebank.csv") as csvfile:
    r = csv.DictReader(csvfile, delimiter=',')
    styles = set()
    style_graph = graphviz.Digraph()
    widths = set()
    width_graph = graphviz.Digraph()
    sizes = set()
    size_graph = graphviz.Digraph()
    size_widths = set()
    size_width_graph = graphviz.Digraph()
    size_width_styles = set()
    size_width_style_graph = graphviz.Digraph()

    for row in r:
        size_width = "%s:%s" % (row['size'], row['width'])
        size_width_style = "%s:%s:%s" % (row['size'], row['width'], row['style'])

        if not row['style'] in styles:
            style_graph.node(row['style'])
        if not row['width'] in widths:
            width_graph.node(row['width'])
        if not row['size'] in sizes:
            size_graph.node(row['size'])
        if not size_width in size_widths:
            size_width_graph.node(size_width)
            graph.edge(row['size'], size_width)
            graph.edge(row['width'], size_width)
        if not size_width_style in size_width_styles:
            size_width_style_graph.node(size_width_style)
            graph.edge(size_width, size_width_style)
            graph.edge(row['style'], size_width_style)

        styles.add(row['style'])
        widths.add(row['width'])
        sizes.add(row['size'])
        size_widths.add(size_width)
        size_width_styles.add(size_width_style)

graph.subgraph(size_graph)
graph.subgraph(width_graph)
graph.subgraph(size_width_graph)
graph.subgraph(size_width_style_graph)

print "Rendering graph"
#graph.render('output.dot')

size_width_style_graph.render('sizes_styles.dot')

for style in sorted(styles):
    with open("%s.html" % style, 'w') as style_file:
        style_file.write(style)

for width in sorted(widths):
    with open("%s.html" % width, 'w') as width_file:
        width_file.write(width)
