normalize = (q) -> q.toLowerCase().replace(/[ ]+/g, ' ').trim()

results_tmpl = '
<h1>{{person_name}} has {{count}} records</h1>
<table border="1">
  <tr>
    <td>Person Name</td>
    <td>Team Name</td>
    <td>Description</td>
    <td>Duration</td>
    <td>Date</td>
    <td>Score</td>
  </tr>
  {{#results}}
  <div class="result">
  <tr>
  <td>{{person_name}}</td>
  <td>{{team}}</td>
  <td>{{description}}</td>
  <td>{{duration}}</td>
  <td>{{date}}</td>
  <td>{{score}}</td>
  </tr>
  </div>
  {{/results}}
</table>
'

load_result = (q) ->
  console.log 'load_result is called, q is ' + q
  if !q
    url = '/records/all'
    console.log 'all case'
  else
    url = '/records/' + encodeURIComponent(q)
    console.log 'individual case'
  $.getJSON url, (json) ->
    rendered = Mustache.render(results_tmpl, json)
    $('#results').html(rendered)

$ ->
  console.log 'document load ready'
  load_result ''
  $('.search-button button').click ->
    console.log 'start'
    q = normalize $('#search-bar').val()
    load_result q