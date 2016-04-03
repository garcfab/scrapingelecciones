#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "008", "010", "012", "013", "015", "016", "020", "025", "028", "030", "031", "040", "042", "046", "048", "049", "052", "055", "058", "060", "067", "070", "073", "076", "078", "079", "085", "090", "095"]
munpos =  ["SANTA MARTA", "ALGARROBO", "ARACATACA", "ARIGUANI (EL DIFICIL)", "CERRO DE SAN ANTONIO", "CHIVOLO", "CIENAGA", "CONCORDIA", "EL BANCO", "EL PINON", "EL RETEN", "FUNDACION", "GUAMAL", "NUEVA GRANADA", "PEDRAZA", "PIJINO DEL CARMEN", "PIVIJAY", "PLATO", "PUEBLOVIEJO", "REMOLINO", "SABANAS DE SAN ANGEL", "SALAMINA", "SAN SEBASTIAN DE BUENAVISTA", "SAN ZENON", "SANTA ANA", "SANTA BARBARA DE PINTO", "SITIONUEVO", "TENERIFE", "ZAPAYAN", "ZONA BANANERA (SEVILLA)"]
DANE = ["47001", "47030", "47053", "47058", "47161", "47170", "47189", "47205", "47245", "47258", "47268", "47288", "47318", "47460", "47541", "47545", "47551", "47555", "47570", "47605", "47660", "47675", "47692", "47703", "47707", "47720", "47745", "47798", "47960", "47980"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Magdalena_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=21&cod_mpio="+amazonas[munpo]
	

	# Parsing link
	page = urllib2.urlopen(url)

	# Hacienda la Sopa
	soup = BeautifulSoup(page,convertEntities=BeautifulSoup.HTML_ENTITIES)
	# soup2 = soup.prettify(formatter=None)
	# print soup2.contents
	# print soup
	# print 'vamos'

	# Orden de grabacion. 
	'''
	1. Votos en Blanco (6)
	2. Potencial de votacion (8)
	3. Votos Validos (10)
	4. Votos Totales (12)
	5. Votos Nulos (14)
	6. Uribe (20)
	7. Carlos Gaviria (22)
	8. Horacio Serpa (24)
	9. Mockus (26)
	10. Enrique Parejo Gonzalez (28)
	11. Alvaro Leyva (30)
	12. Carlos Arturo Rincón Barreto (32)
	'''

	# Celdas es lo que tiene el dato de interes
	valores=soup.findAll('td',{'class':'valor_contenido'})

	# Valores es lo que tiene el rotulo de cada dato
	rotulo=soup.findAll('td',{'class':'datos_contenido'})
	print "Grabando municipio", munpos[munpo]

	f.write(munpos[munpo]+ '\t'+str(DANE[munpo]) + '\t'+ valores[6].text+ '\t' + valores[8].text + '\t' + valores[10].text + '\t' + valores[12].text + '\t' +\
		     valores[14].text + '\t' + valores[20].text+ '\t' + valores[22].text + '\t' + valores[24].text + '\t' + valores[26].text + \
		    '\t' + valores[28].text + '\t' + valores[30].text+ '\t' + valores[32].text+'\n')

f.close()