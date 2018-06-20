import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.models import ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)
node_indices = list(range(N))
print(node_indices)
print(N)

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

values = []
for vertex in graph_data.vertexes:
    values.append(vertex.value)

source = ColumnDataSource(data=dict(height=y,
                                    weight=x,
                                    names=values))


labels = LabelSet(x='weight', y='height', text='names', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')


citation = Label(x=70, y=70, x_units='screen', y_units='screen',
                 render_mode='css',
                 border_line_color='white', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0,500), y_range=(0,500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=20, width=20, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0, 1, 2, 3],
    end=[1, 2, 3, 4])

### start of layout code

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.renderers.append(labels)
plot.renderers.append(citation)

output_file('graph.html')
show(plot)