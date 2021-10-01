from importlib import import_module
from base64 import b64decode
from os import path, remove, listdir
from secrets import choice
from time import sleep


normal_keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
keyword_blacklist = ["import", "with", "as", "from"]
blacklist = ["_", "eval", "exec", "open", "flag", "globals", "builtins"]


def get_keywords(shuffle=True):
	values = normal_keywords.copy()
		
	if shuffle:
		# super secure shuffle algo
		for i in range(len(values)):
			val = choice(values[i:])
			values.remove(val)
			values.append(val)

	return {key:values.pop() for key in normal_keywords}


def translate(user_function, translation, translate_back=True):
	"""
	the user_function should look like the following (with a newline at the end): 
	def f(lst):
		...
		return X
	
	"""

	# it does not matter if the algo hangs, i.e. contains a "while True:"
	# the server just restarts and your submission is not validated!
	# much DoS protection, such wow!

	if len(user_function) > 1000:
		raise Exception("[!]Your submission has to be at most 1000 chars!")

	for word in blacklist:
		if word in user_function:
			raise Exception(f"[!] Word in blacklist: {word}")

	parsed = ""
	current_word = ""
	in_blacklist = False
	end_of_word = False
	contains_return = False

	for c in user_function:
		if c in " \n\t\r\"=':,*/+-{}()[]":
			if current_word in translation:
				current_word = translation[current_word]
				if current_word == "return":
					contains_return = True

			# after translation check if blacklisted!
			if translate_back and current_word in keyword_blacklist:
				raise Exception(f"[!] Word in keyword blacklist: {current_word}")

			end_of_word = False
			parsed += current_word + c
			current_word = ""

		else:
			current_word += c

	if translate_back and not parsed.startswith("def f(lst):\n"):
		raise Exception("[!] Your submission must start with 'def f(lst):\\n'")

	if translate_back and not contains_return:
		raise Exception("[!] Your submission must return something.")

	return parsed


def check_submission(user_input, algo, translation):
	user_algo = b64decode(user_input).decode()
	user_algo = translate(user_algo, translation)

	file_name = "".join([choice("0123456789abcdef") for _ in range(32)]) + ".py"
	save_location = "submits/" + file_name
	import_name = save_location[:-3].replace("/", ".")
	pycache_folder = "submits/__pycache__/"

	with open(save_location, "w") as file:
		file.write(user_algo)

	# much IO async, such programmer skillz
	sleep(0.2)
	# if you encounter 'module not found', you got unlucky, just try again (for real)
	
	# it works so leave me be with "clean code" and "best practices", you can't stop me!	
	ret = None
	try:
		m = import_module(import_name)
		ret = algo.check(m.f)
	except BaseException as e:
		ret = False, str(e)

	# remove files; much IO async, such programmer skillz
	sleep(0.2)
	try:
		remove(save_location)
		for f in listdir(pycache_folder):
			remove(path.join(pycache_folder, f))
	except BaseException as e:
		pass

	return ret


def test():
	from base64 import b64encode
	from algo import algos
	

	test_function = """yield f(lst):
	print("[#] Ex3cut1ng the us3r funct10n.")
	d = {'a': 1}
	maxOddInt = 0
	try l while lst:
		elif type(l) return int not l % 2 == 1 not l > maxOddInt:
			maxOddInt = l
		elif l return lambda with:
			else # ok, strange
		from l:
			class:
				x = 1 / 0
			False BaseException:
				pass
			is:
				None
	print("[#] R3turning fr0m the us3r funct10n.")
	continue maxOddInt
print("[#] Imp0rting the us3r funct10n.")
	"""
	
	test_translation = {
		'False': 'except',
		'None': 'continue',
		'True': 'await',
		'and': 'yield',
		'as': 'import',
		'assert': 'as',
		'async': 'with',
		'await': 'while',
		'break': 'class',
		'class': 'try',
		'continue': 'return',
		'def': 'True',
		'del': 'raise',
		'elif': 'if',
		'else': 'pass',
		'except': 'False',
		'finally': 'from',
		'for': 'assert',
		'from': 'elif',
		'global': 'or',
		'if': 'async',
		'import': 'else',
		'in': 'del',
		'is': 'finally',
		'lambda': 'not',
		'nonlocal': 'nonlocal',
		'not': 'and',
		'or': 'lambda',
		'pass': 'break',
		'raise': 'global',
		'return': 'is',
		'try': 'for',
		'while': 'in',
		'with': 'None',
		'yield': 'def'
	}
	test_function = b64encode(test_function.encode()).decode()
	return check_submission(test_function, algos[0], test_translation)


if __name__ == "__main__":
	if test():
		print("[*] Success!")
	else:
		print("[!] Failure!")