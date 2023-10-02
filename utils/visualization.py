# Copyright 2023 Miguel Matey Sanz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_execution(data_collection, execution):
    '''
    Generates an interactive plot with the accelerometer and gyroscope data of the specified execution.
    
    Args:
        data_collection(dict): dictionary containing the collected dataset. See: `data_loading.load_data`
        execution(str): execution data to plot. Format: 'sXX_YY_{sp|sw}'
        
    Returns:
        plotly.graph_objs.Figure: interactive plot
    '''
    
    if execution not in data_collection:
        raise Exception(f'Execution {execution} not present in dataset.')
        
    df = data_collection[execution]
    components_group = [['x_acc', 'y_acc', 'z_acc'], ['x_gyro', 'y_gyro', 'z_gyro']]
    y_axes_titles = ['Intensity (m/s<sup>2</sup>)', 'Angular velocity (º/s)']
    figures = []
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08)
    line_style = ['solid', 'dashdot', 'dot']
    line_colors = ['red', 'green', 'blue']
    
    change = df['label'].shift(1, fill_value=df["label"].head(1)) != df["label"]
    change_timestamps = df[change]['timestamp'].to_list()
    change_timestamps = df.head(1)['timestamp'].to_list() + change_timestamps + df.tail(1)['timestamp'].to_list()
    activities = ['SEATED', 'STANDING UP', 'WALKING', 'TURNING', 'WALKING', 'TURNING', 'SITTING DOWN', 'SEATED']
    
    for c, components in enumerate(components_group):
        
        for i, component in enumerate(components):
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'], y=df[component], 
                    line=go.scatter.Line(dash=line_style[i], color=line_colors[i]),
                    name=component.split('_')[0], legendgroup='legend', showlegend= c == 0),
                row = c + 1, col = 1
            )
            
        for i in range(len(change_timestamps) - 1):
            fig.add_vline(
                x=change_timestamps[i], line_width=3, line_dash="dash", line_color="black",
                row = c+1, col = 1
            )
            
            if c == 0:
                fig.add_vrect(
                    x0=change_timestamps[i], x1=change_timestamps[i+1],
                    fillcolor='white', opacity=0,
                    layer="below", line_width=0,
                    annotation_text=f'<b>{activities[i]}</b>', annotation_font_size=13, annotation_font_color='black',
                    annotation_position='bottom', annotation_xanchor='center', 
                    annotation_yshift=-25, annotation_bordercolor='black',
                    row = c+1, col = 1
                )
        
    for ax in fig['layout']:
        if ax[:5] == 'yaxis':
            fig['layout'][ax]['gridcolor'] = 'darkgrey'
            fig['layout'][ax]['gridwidth'] = 1
            fig['layout'][ax]['zeroline'] = True
            fig['layout'][ax]['zerolinecolor'] = 'black'
            fig['layout'][ax]['zerolinewidth'] = 2
        elif ax[:5] == 'xaxis':
            fig['layout'][ax]['gridcolor'] = 'darkgrey'
            fig['layout'][ax]['gridwidth'] = 1
         
    source_device = 'Smartphone' if execution.split('_')[-1] == 'sp' else 'Smartwatch'
    fig.update_layout(height=600, width=1200,
        title={
            'text': f'{source_device} accelerometer (top) and gyroscope (bottom) samples',
            'y': 0.90,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font_size': 22
        },
        plot_bgcolor = 'rgb(255,255,255)', showlegend=True)
    fig.update_xaxes(dtick=500, tickformat='%H:%M:%S.%2f')
    fig.update_xaxes(title_text='Timestamp', row=2, col=1)
    fig.update_yaxes(title_text='Intensity (m/s<sup>2</sup>)', row=1, col=1)
    fig.update_yaxes(title_text='Angular velocity (º/s)', row=2, col=1)
    fig.update_layout(margin=dict(l=20, r=20, t=100, b=20), font_family='Helvetica')
    return fig