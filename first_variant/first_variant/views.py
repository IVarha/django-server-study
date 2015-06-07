from django.http import HttpResponse

from django.shortcuts import render_to_response

def home(request):
    xdata = range(100)
    ydata = [x ** 3 + 234 for x in range(100)]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "lineChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    chartcontainer2 = 'piechart_container2'

    data2 = {
        'charttype2': charttype,
        'chartdata2': {'x': range(100), 'y': [x ** (-3) + 234 for x in range(1, 101)]},
        'chartcontainer2': chartcontainer2,
        'extra2': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    data.update(data2)
    return render_to_response('simple_plot.html', data)