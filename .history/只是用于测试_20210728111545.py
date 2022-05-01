import plotly
import plotly.graph_objs as go

'''初始化jupyter notebook中的绘图模式'''
plotly.offline.init_notebook_mode()

'''绘制一个基本的折线图，控制其尺寸为1600x600'''
plotly.offline.iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}],
                    image_height=600,
                    image_width=1600)
