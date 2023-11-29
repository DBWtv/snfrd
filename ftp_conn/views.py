from django.shortcuts import render
from django.http import HttpResponse
from .connection import FTPConnection
from .models import FTPServer


def index(request):
    servers = FTPServer.objects.all()
    html = '''
        <html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
    '''
    html += '''
    <table>
        <tr>
            <th>Host</th>
            <th>Port</th>
        </tr>
    '''
    for server in servers:
        html += f'<tr><td>{server.host}</td><td>{server.port}</td></tr>'
    html += '</table>'
    response = html + '</body></html>'
    return HttpResponse(response)
