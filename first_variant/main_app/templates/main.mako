{% load i18n %}
{% load static %}
{% load staticfiles %}
<!DOCTYPE html>
<html>

  <head>
    <meta charset='utf-8' />
    <meta http-equiv="X-UA-Compatible" content="chrome=1" />
    <meta name="description" content="Hadoopecosystemtable.github.io : This page is a summary to keep the track of Hadoop related project, and relevant projects around Big Data scene focused on the open source, free software enviroment." />

    <link rel="stylesheet" type="text/css" media="screen" href="{% static "css/stylesheet.css" %}">

    <title>The Hadoop Ecosystem Table</title>
  </head>

  <body>

    <!-- HEADER -->
    <div id="header_wrap" class="outer">
        <header class="inner">

          <h1 id="project_title">Real Time Analysis Web UI</h1>
          <h2 id="project_tagline">This page is an example of usage analyze consumer interest and propose what product is better for realization</h2>

        </header>
    </div>

    <!-- MAIN CONTENT -->
    <div id="main_content_wrap" class="outer">

<section id="main_content" class="inner">
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>

</section>

<section id="main_content1" class="inner">
<select>
    {% for name in foo %}
        <option value="volvo">{{name}}</option>
    {% endfor %}
</select>

</section>


    </div>
    <!-- FOOTER  -->
    <div id="footer_wrap" class="outer">
      <footer class="inner">
       </footer>
    </div>

  </body>
</html>