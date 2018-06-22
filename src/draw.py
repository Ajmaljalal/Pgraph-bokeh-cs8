import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider
from bokeh.models import ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8
from bokeh.models.markers import Circle, Diamond, Hex

from graph import *

graph_data = Graph()
#graph_data.debug_create_test_data()
graph_data.randomize(5, 5, 10, 10)
#graph_data.bfs(graph_data.vertexes[0])
graph_data.connected_components()

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
            source=source, render_mode='canvas', text_align='center', text_baseline='middle')


color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(x_range=(0,500), y_range=(0,500),
              toolbar_location='right', plot_width=900, plot_height=500)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Hex(size=40, line_color="#3288bd", line_width=3, fill_color='color')

start_points = []
end_points = []
for start_index, v in enumerate(graph_data.vertexes):
    for e in v.edges:
        start_points.append(start_index)
        end_points.append(graph_data.vertexes.index(e.destination))

graph.edge_renderer.data_source.data = dict(
    start=start_points, #node_indices[0:-1]
    end=end_points )

### start of layout code

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.renderers.append(labels)

output_file('graph.html')
show(plot)