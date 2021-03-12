# encoding utf-8

from pyecharts.charts import Page,Tab
from pyeUtil import bar_datazoom_slider,line_markpoint,pie_rosetype,grid_mutil_yaxis, \
    liquid_data_precision,table_base,timeline_bar_reversal

from data import getExcelToData1

'''
可用于自定义数据导出图表
'''
def tab(filename="info"):
    '''
    分页组件
    '''
    tab = Tab()
    tab.add(liquid_data_precision("111"), "前日留存")
    tab.add(bar_datazoom_slider("222"), "分端留存")
    tab.add(table_base("222"), "明细")
    tab.add(line_markpoint("222"), "人群留存")
    tab.add(pie_rosetype("222"), "城市")
    tab.add(grid_mutil_yaxis("222"), "新增留存")
    tab.render_notebook()
    tab.render('{}.html'.format(filename))


def page(filename="info"):
    '''
    页面
    '''
    # test data

    y_data = [
            {'name':'安卓','values':[0.34,0.76,0.88,0.99,0.242,0.42,0.22]},
            {'name':'ios','values':[0.50,0.90,0.72,0.34,0.76,0.88,0.99]}
        ]
    x_data = ['周一','周二','周三','周四','周五','周六','周日']

    page = Page()
    page.add(
        # timeline_bar_reversal(title='渠道留存'),
        liquid_data_precision("111"),
        bar_datazoom_slider("222",y_data=y_data,x_data=x_data, datazoom_opts=None,toolbox_opts=None),
        table_base("333"),
        line_markpoint("555"),
        pie_rosetype("444"),
        grid_mutil_yaxis("777"),
    )
    page.render('{}.html'.format(filename))


if __name__ == "__main__":
    page()
    # tab()