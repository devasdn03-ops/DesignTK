# app.py
import os
from nicegui import ui
import plotly.express as px

# Read port from environment (Render sets PORT). Default to 8080 for local runs.
PORT = int(os.environ.get('PORT', 8080))
HOST = '0.0.0.0'

df = px.data.iris()

def update_plot(value):
    try:
        max_val = float(value)
    except Exception:
        max_val = float(slider.value)
    filtered = df[df['sepal_length'] <= max_val]
    fig = px.scatter(
        filtered,
        x='sepal_width',
        y='sepal_length',
        color='species',
        labels={'sepal_width':'Sepal Width','sepal_length':'Sepal Length'},
        height=540
    )
    fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))
    plot.set_figure(fig)
    plot.update()

ui.label('Iris scatter — filter by max sepal length').classes('text-lg font-medium')

with ui.row().classes('items-center gap-4'):
    slider = ui.slider(
        min=float(df['sepal_length'].min()),
        max=float(df['sepal_length'].max()),
        value=float(df['sepal_length'].max()),
        step=0.1,
        on_change=lambda e: update_plot(e.value)
    ).classes('w-1/3')
    ui.label('Max sepal length').classes('ml-2')

fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', height=540)
fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))
plot = ui.plotly(fig).classes('w-full h-[540px]')

# Call ui.run() directly - NO nme guard needed here
ui.run(
    host=HOST, 
    port=PORT, 
    title='NiceGUI Demo',
    reload=False,
    show=False
)
```

#Update profile
```
web: python app.py
