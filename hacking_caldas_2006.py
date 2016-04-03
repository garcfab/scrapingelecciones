#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "013", "022", "034", "037", "049", "052", "055", "058", "061", "067", "076", "078", "079", "082", "085", "103", "106", "109", "115", "120", "124", "127", "130", "133"]
munpos =  ["MANIZALES", "AGUADAS", "ANSERMA", "ARANZAZU", "BELALCAZAR", "CHINCHINA", "FILADELFIA", "LA DORADA", "LA MERCED", "MANZANARES", "MARMATO", "MARQUETALIA", "MARULANDA", "NEIRA", "NORCASIA", "PACORA", "PALESTINA", "PENSILVANIA", "RIOSUCIO", "RISARALDA", "SALAMINA", "SAMANA", "SAN JOSE", "SUPIA", "VICTORIA", "VILLAMARIA", "VITERBO"]
DANE = ["17001", "17013", "17042", "17050", "17088", "17174", "17272", "17380", "17388", "17433", "17442", "17444", "17446", "17486", "17495", "17513", "17524", "17541", "17614", "17616", "17653", "17662", "17665", "17777", "17867", "17873", "17877"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Caldas_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=09&cod_mpio="+amazonas[munpo]
	

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