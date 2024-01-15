from time_counter import start, end, count
t1 = start()
for i in range(100):
	with open("data/index.json", "rb") as json_file:
		json_data = eval(json_file.read().decode())

	out_file = open("data/index.xml", "w", encoding='utf-8')

	def parser(JSON):
		KEY = list(JSON.keys())
		KEYS = len(KEY)

		for i in range(KEYS):
			POSITION = KEY[i]
			if (type(JSON[POSITION]) == list):
				out_file.write("<list name = \"" + str(POSITION) + "\" >\n")
				for i in range(len(JSON[POSITION])):
					out_file.write("\t<s>" + str(JSON[POSITION][i]) + "</s>\n")
				out_file.write("</list>\n")
			else:
				out_file.write("<" + POSITION + ">")

				if (type(JSON[POSITION]) == int or type(JSON[POSITION]) == float):
					out_file.write(str(JSON[POSITION]))
				elif (len(JSON[POSITION]) > 0):
					NEW_DATA = JSON[POSITION]
					if (type(NEW_DATA) == str):
						out_file.write(str(JSON[POSITION]))

					else:
						out_file.write("\n")
						parser(NEW_DATA)

				else:
					pass

				out_file.write("</" + POSITION + ">\n")

	out_file.write("<root>\n")

	parser(json_data)

	out_file.write("</root>\n")

	out_file.close()

t2 = end()

count(t1, t2)