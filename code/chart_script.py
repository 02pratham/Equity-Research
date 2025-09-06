import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('ril_financial_performance.csv')

# Create the chart with bars and line on single axis
fig = go.Figure()

# Add revenue bars
fig.add_trace(go.Bar(
    x=df['Year'],
    y=df['Revenue_Billions_INR'],
    name='Revenue',
    marker_color='#1FB8CD',
    opacity=0.8,
    hovertemplate='<b>Revenue</b><br>Year: %{x}<br>Amount: %{y:.1f}b INR<extra></extra>'
))

# Add net income line
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Net_Income_Billions_INR'],
    mode='lines+markers',
    name='Net Income',
    line=dict(color='#DB4545', width=4),
    marker=dict(size=10, color='#DB4545'),
    hovertemplate='<b>Net Income</b><br>Year: %{x}<br>Amount: %{y:.1f}b INR<extra></extra>'
))

# Update layout
fig.update_layout(
    title='RIL Financial Performance 2021-2025',
    xaxis_title='Year',
    yaxis_title='Amount (b INR)',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)

# Update traces
fig.update_traces(cliponaxis=False)

# Update axes
fig.update_yaxes(tickformat='.1f')
fig.update_xaxes(dtick=1)

# Save the chart
fig.write_image('ril_financial_chart.png')

print("Chart saved successfully!")