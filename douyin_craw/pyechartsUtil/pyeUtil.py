# encoding utf-8

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker


from data import getExcelToData1


def timeline_bar_reversal(title="Timeline-Bar-Reversal", is_auto_play=True):
    '''
    动效数据增长图
    '''
    data = getExcelToData1()


    tl = Timeline()
    tl.add_schema(is_auto_play=is_auto_play,
                    play_interval=100,
                    is_loop_play=True,
                    is_inverse= False,
                    # axis_type='time',
                    is_timeline_show=True, # 是否展示播放按钮
                    )

    # for i in range(1950, 2020):
    #     bar = Bar()
    #     bar.add_xaxis(Faker.choose())
    #     bar.add_yaxis("商家A", Faker.values(), label_opts=opts.LabelOpts(position="right"))
    #     bar.add_yaxis("商家B", Faker.values(), label_opts=opts.LabelOpts(position="right"))
    #     bar.reversal_axis()
    #     bar.set_global_opts(title_opts=opts.TitleOpts("{}: {} ".format(title,i)))
    #     tl.add(bar, "{}年".format(i))
    for i in range(1, len(data['date'])):
        bar = Bar()
        bar.add_xaxis(data['kanaal'])
        bar.add_yaxis('新增', data['values'][i-1], label_opts=opts.LabelOpts(position="right"))
        bar.reversal_axis()
        bar.set_global_opts(title_opts=opts.TitleOpts("{}: {} ".format(title,i)))
        tl.add(bar, "{}".format(i))

    return tl



def bar_datazoom_slider(title='Bar-DataZoom（slider-水平）',width="1200px",x_data=['前天','昨天','今天'], \
        y_data = [{'name':'商家A','values':[1,6,7]}],
        toolbox_opts=opts.ToolboxOpts(),
        datazoom_opts=[opts.DataZoomOpts()]
        ) -> Bar:
    '''
    柱状图
    y_data 几根柱子，默认1根
    y_data = [{'name':'商家A','values':[1,6,7]}]

    toolbox_opts 是否展示右上方的小工具，默认展示，不展示传 None
    datazoom_opts 是否展示图表下方可拖动的进度条，默认展示，不展示传 None
    '''
    b = Bar(init_opts=opts.InitOpts(width=width))

    if len(y_data) == 1:
        b.add_yaxis(y_data[0]['name'], y_data[0]['values'])
    if len(y_data) == 2:
        b.add_yaxis(y_data[0]['name'], y_data[0]['values'])
        b.add_yaxis(y_data[1]['name'], y_data[1]['values'])
        
    b.add_xaxis(x_data)
    b.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        datazoom_opts=datazoom_opts,
        toolbox_opts=toolbox_opts,
    )
    return b


def line_markpoint(title = "Line-MarkPoint") -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c


def pie_rosetype(title="Pie-玫瑰图示例") -> Pie:
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c


def grid_mutil_yaxis(title="Grid-多 Y 轴示例") -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title=title),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def liquid_data_precision(title="Liquid-数据精度",text='值',value=[0.7234]) -> Liquid:
    '''
    水球图
    '''
    c = (
        Liquid()
        .add(
            text,
            value,
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c


def table_base(title="Table") -> Table:
    table = Table()

    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title=title)
    )
    return table
