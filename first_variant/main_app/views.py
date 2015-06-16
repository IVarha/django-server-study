from django.conf.global_settings import INSTALLED_APPS
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import Template, loader, Context
from nvd3 import lineChart
from mako.lookup import TemplateLookup
from sklearn import linear_model
from scipy.integrate import trapz
# Create your views here.


def basic(request):
    print(str(INSTALLED_APPS))
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
    # print(mytemplate.render())
    return render_to_response("index.html", data)
    # return render_to_response("main.mako", {"foo": ['vollid', 'fsdfsd', 'fsdfsdf', 'fsdfsdf']})
pass


def testgraphic(request):
    if request.POST:
        type = 'lineChart'
        chart = lineChart(name=type,  x_is_date=False)

        #
        xdata = range(100)
        ydata = [x ** 3 + 234 for x in range(100)]
        chart.add_serie(y=ydata,x=xdata,name='sas')
        # chartdata = {'x': xdata, 'y': ydata}
        # charttype = "lineChart"
        # chartcontainer = 'piechart_container'
        # data = {
        #     'charttype': charttype,
        #     'chartdata': chartdata,
        #     'chartcontainer': chartcontainer,
        #     'extra': {
        #         'x_is_date': False,
        #         'x_axis_format': '',
        #         'tag_script_js': True,
        #         'jquery_on_ready': False,
        #     }
        # }
        return HttpResponse(chart.htmlcontent)



def regression_main(data,xstart,xend):
  temp = [regression(x) for x in data]
  tmp2 = []
  for i in range(0,len(temp)):
    x = integrate(temp[i].prefict,xstart,xend,0.1)
    tmp2.append((x,i))
  mt = tmp2[0]
  for x in tmp2:
    if mt[0] < x[0] :
      mt = x
  return temp[mt[1]]
  pass

def regression(data):
  regr = linear_model.LinearRegression()
  regr.fit(data[0],data[1])
  return regr
  pass

def integrate(func,start,end,dx):
  n = int((end - start)/dx)
  tx = []
  for i in range(0,n):
    tx.append(start + i*dx)
  return trapz(func,x=tx)


