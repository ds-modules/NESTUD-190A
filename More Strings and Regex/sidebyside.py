from IPython.core.display import display, HTML

class sbs(object):
	"""sbs: custom side by side printing in Jupyter
	uses HTML objects to display strings
	all attributes use traditional CSS syntax
	feel free to add any additional things with
	the additionalcss variable"""

	def __init__(self):
		
		# make it so that each time you generate an object w/ split
		# there is a new id for the div tags bc otherwise it
		# changes all of the divs

		# can do that by adding a count to instance attributes
		# and a increment it when create css is called
		# AND include it in body (in split)

		self.rightbackground = '#98AFC7'
		self.leftbackground = 'lightgray'
		
		self.alignright = 'left'
		self.alignleft = 'left'

		self.headerright = 'Right:'
		self.headerleft = 'Left:' 

		self.fonttype = 'Courier New'

		self.additionalcss = ''

	def create_css(self):

		#make this a multi line string
		return "{} #wrapper {{width:100%;clear:both;display: flex;font-family:{};}} #left {{background-color: {};width:49%;float:left;padding: .5vw;border-right: solid black 1.5px;text-align:{};}} #right {{background-color: {} !important;width:49%;float:left;padding: .5vw;border-left: solid black 1.5px;text-align:{};}}".format(self.additionalcss, self.fonttype, self.leftbackground, self.alignleft, self.rightbackground, self.alignright)
		print(self.rightbackground)

	def split(self, left, right):
		body ='<div id="wrapper"><div id="left">{}<br>{}</div><div id="right">{}<br>{}</div></div>'.format(self.headerleft, left, self.headerright, right)
		display(HTML('<style>{}</style> <body>{}</body>'.format(self.create_css(), body)))
		