uri = "Venezuela_cleaned_words.dot"
tw_file = open('../re   sults/tweets_depurated.csv', 'w')
archivo = open(uri,"r+")
nodos = open("nodos.csv","a+")
nodos.write("Id"+","+"Label"+","+"Weigth"+","+"cons"+","+"Size"+"\n")
aristas = open("aristas.csv","a+")
aristas.write("Source,Target,Type,Weight\n")
for linea in archivo:
	#"ven" ["weight"=130,"ui.label"="ven","cons"=39,"ui.size"=66.0];
	if(linea.find("ui.label")!= -1):
		separado = linea.split(" ")
		p = separado[0]
		palabra = p[1:-1]
		r=separado[1].split(",")
		
		contenedor = r[0].split("=")
		cons = r[2].split("=")[1]
		size = r[3].split("=")[1][:-2]
		peso = contenedor[1]
		escribir=(palabra+","+palabra+","+peso+","+cons+","+size)
		nodos.write(escribir+"\n")
	else:
            print(linea)
            separado=linea.split(" -- ")
            ini = separado[0][1:-1]
            procesar = separado[1].split(" ")
            fin = procesar[0][1:-1]
            procesar = procesar[1].split("=")
            procesar = procesar[1].split("]")
            peso = procesar[0]
            escribir=(ini+","+fin+","+"Directed"+","+peso)
            aristas.write(escribir+"\n")

#https://drive.google.com/drive/u/1/folders/0B-ojOIQhNk41MWxtZFljZkdjY00
		