# Codigo de Python de ejemplos

# Funciones de cadenas

"		Hello, world! \t\t\n".strip()
"Hola,  amigos!".split()
"Hela, amigos!".split(" ")
"www.networksciencelab.com".split(".")

", ".join(["python", "es ", "un", "lenguaje", "divertido"])
"-".join("1.617.305.1985".split("."))
" ".join("Esta cadena\n\r tiene  muchos \t\tespacios".split())
"www.networksciencelab.com".find(".com")
"www.networksciencelab.com".count(".")

# Estructuras de python

bLista = [str(i) for i in range(10000000)]
"abc" in bLista
bConjunto = set(bLista)
"abc" in bConjunto

seq = ["alpha", "bravo", "charlie", "delta"]
dict(enumerate(seq))
kseq = "abcd" 
vseq = ["alpha", "bravo", "charlie", "delta"]
dict(zip(kseq, vseq))

# Algo de programacion funcional en Python 

[x for x in miLista]
[x for x in miLista if x >= 0]
[x**2 for x in miLista]
[1/x for x in miLista if x != 0]
[l.strip() for l in infile if l.strip()]
[linea for linea in [l.strip() for l in infile] if linea]

(x**2 for x in miLista)

# Modulo collections

from collections import Counter
frase = "ella es la mas bella entre todas"
cntr = Counter(frase.split())
cntr.most_common()
cntrDict['a']


# Leer y escribir archivos en Python

f.read() 
f.read(n) 
f.readline() 
f.readlines() 
f.write(line) 
f.writelines()

# modulo urllib

import urllib.request
try:
    with urllib.request.urlopen("http://www.networksciencelab.com") as doc:
        html = doc.read()
except: 
    print("No se puede abrir el archivo %s" % doc, file=sys.err)
	
import urllib.parse
URL = "http://networksciencelab.com/index.html;param?foo=bar#content"
urllib.parse.urlparse(URL)
