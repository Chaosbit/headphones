_javascript = '''
	;

	'''

_header = '''
	<html>
	<head>
		<title>Headphones</title>
		<link rel="stylesheet" type="text/css" href="data/css/style.css" />
		<link rel="icon" type="image/x-icon" href="data/images/favicon.ico" /> 
		<link rel="apple-touch-icon" href="data/images/headphoneslogo.png" />
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js" type="text/javascript"></script>
		<script type="text/javascript">
			%s
		</script>
	</head>
	<body>
	<div class="container">''' % _javascript
	
			
_logobar = '''
		<div class="logo">
			<a href="/"><img src="data/images/headphoneslogo.png" border="0">headphones</a>
		</div>
		<br />
	'''

_nav = '''<div class="nav">
					<a href="/searchPage">SEARCH</a>
					<a href="/">LIBRARY</a>
					<a href="/upcoming">UPCOMING</a>
					<a href="/manage">MANAGE</a>    
					<a href="/history">HISTORY</a>
					<a href="/config">SETTINGS</a>
					<a href="/shutdown"><font color="red">SHUTDOWN</font></a>
			</div>'''
	
_footer = '''
	</div><div class="footer"></div>
	</body>
	</html>'''