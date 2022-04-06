import cgi

form = cgi.FieldStorage()

name = form["name"].value
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<head>
<meta charset="UTF-8">
<title>/main.html</title>
</head>
<body>
<h2>반가워요</h2>
이름 : {0}, 전화 : {1}, 성별 : {2}
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(name, phone, gen))