from IPython.core.display import display, HTML
import translation 


class translate(object):

	id_start = 0

	def __init__(self, column_types, language_to='en'):

		self.num_of_columns = len(column_types) + 1
		column_types.insert(0, 'original text')
		self.column_types = column_types

		self.language_to = language_to

		self.funcs = {'original text':self.original_text_pls, 'translate':self.tranlate_pls,
		 'parts of speech':self.polyglot_pos, 'language':self.polyglot_languages}
		self.header = {'original text':'Original Text:', 'translate':'Translation:',
		 'parts of speech':'Parts of Speech:', 'language':'Language(s) Detected:'}

		self.fonttype = 'Courier New'
		self.additionalcss = ''


	# these are the functions that will go within the body calls

	# need to fill in these functions so that we get the right things
	def tranlate_pls(self, txt):
		return translation.bing(txt, dst = self.language_to)

	def original_text_pls(self, txt):
		return txt

	def parts_of_speech_pls(self, txt):
		import nltk
		tokenized = nltk.word_tokenize(txt)
		return nltk.pos_tag(tokenized)

	def polyglot_languages(self, txt):
		from polyglot.detect import Detector
		langs = Detector(txt, quiet=True).languages
		selected_items = [(x.name, x.confidence) for x in langs]
		# converting to readable from Detector objects
		stringy_list = ['Name: ' + str(x) + '    Confidence: ' +str(y) for x,y in selected_items]
		return '<br><br>'.join(stringy_list)

	def polyglot_pos(self, txt):
		from polyglot.text import Text
		return Text(txt).pos_tags


	# make a function for part of speech counts
	# and names in the text
	# maybe name counts

	# make it so that we can try different translating services
	# a google integration may be necessary :(



	# incrementing the ids so that the css of a new one doesn't change an old one
	def increment_ids(self):
		strt_id = translate.id_start
		translate.id_start += self.num_of_columns
		return range(strt_id, strt_id + self.num_of_columns)



	# creating the divs and the content that will go in them
	def create_body(self, id_numbers, txt):
		# setting up all of the divs that will be there
		base_column = '<div id="{}">{}<br>{}</div>'
		blank_divs = base_column * self.num_of_columns

		# calling the functions specified in our constructor on our body of text
		content = [self.funcs[col](txt) for col in self.column_types]

		headers = [self.header[col] for col in self.column_types]

		# zipping them together so we can make a string in the correct order, then flattening
		nested_order = list(zip(id_numbers, headers, content))
		unnested = [item for sublist in nested_order for item in sublist]

		return '<div id="wrapper">' + blank_divs.format(*(unnested)) + '</div>'



	def create_css(self, id_numbers):
		
		# picking alternating colors for columns
		clrs = ['#e6f3f7', 'lightgray']
		def alternate():
			while True:
				yield 0
				yield 1
		gen = alternate()

		clr_list = [clrs[next(gen)] for i in range(self.num_of_columns)]

		# width evenly divided by number of columns
		width = "width:{}%;".format(str(100 / self.num_of_columns))

		# setting up for all different css that will be there
		base_css = "#{} {{background-color: {};" + width + "float:left;padding: .5vw;border-right: solid black 1.5px;}}"
		blank_csss = base_css * self.num_of_columns

		# zipping them together so we can make a string in the correct order, then flattening
		nested_order = list(zip(id_numbers, clr_list))
		unnested = [item for sublist in nested_order for item in sublist]

		final_css = blank_csss.format(*(unnested))

		wrapper = "{} #wrapper {{width:100%;clear:both;display: flex;font-family:{};}}".format(self.additionalcss, self.fonttype)

		return wrapper + final_css



	def create(self, initial_text):

		id_list = self.increment_ids()
		string_ids = ['d'+str(x) for x in id_list]

		display(HTML('<style>{}</style> <body>{}</body>'.format(self.create_css(string_ids), self.create_body(string_ids, initial_text))))

		# Add a return statement so that the values are accessible

