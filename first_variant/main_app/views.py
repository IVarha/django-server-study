from django.conf.global_settings import INSTALLED_APPS
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import Template, loader, Context
from mako.lookup import TemplateLookup

# Create your views here.


def basic(request):
    print(str(INSTALLED_APPS))
    # mylookup = TemplateLookup(directories=['/docs'], output_encoding='utf-8', encoding_errors='replace')
    # mytemplate = mylookup.get_template("/home/igorv/server/DJ/first_variant/main_app/templates/main.mako")
    t = loader.get_template("main.mako")

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

    # view = 'basic'
    # html = "<html><body>this is %s view</body></html>" % view

    # print(templ.render())
    # print(mytemplate.render())
    return render_to_response("index.html", data)
    # return render_to_response("main.mako", {"foo": ['vollid', 'fsdfsd', 'fsdfsdf', 'fsdfsdf']})
pass