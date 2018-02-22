# Expresiones regulares y wildcards en Python

"\\n"
r"\n

r"\w[-\w\.]*@\w[-\w]*(\.\w[-\w]*)+"
r"<TAG\b[^>]*<(.*?)</TAG>"
r"[-+]?((\d*\.?\d+)|(\d\.))([eE][-+]?\d+)?"

# modulo re
import re
re.function(rawPattern, ...)
compiledPattern.function(...)

split(pattern, string, maxsplit=0, flags=0)
re.split(r"\W", "Hola, wendy, me prestas un sol")
re.split(r"\W+", "Hello, world!")

match(pattern, string, flags=0)
mo = re.match(r"\d+", "067 Empieza con un numero")
mo.group()

re.match(r"\d+", "No empieza con un numero ")

search(pattern, string, flags=0) 
re.search(r"[a-z]+", "0010010 tiene al menos un 010 letras 0010010")

findall(pattern, string, flags=0)
re.findall(r"[a-z]+", "0010010 tiene al menos 010 letras 0010010", re.I)

sub(pattern, repl, string, flags=0)
re.sub(r"[a-z ]+", "[...]", "0010010 tiene al menos 010 letras 0010010")

# modulo glob
import glob
glob.glob("*.txt")
