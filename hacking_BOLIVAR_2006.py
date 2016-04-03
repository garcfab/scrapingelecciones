#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' Pilas que me toco borrar NOROSI
'''

# Vector de Amazonas
amazonas = ["001", "004", "005", "006", "007", "009", "010", "013", "014", "015", "016", "018", "022", "025", "026", "027", "028", "031", "037", "040", "041", "043", "044", "059", "063", "065", "070", "072", "073", "076", "078", "079", "082", "084", "091", "094", "095", "097", "106", "110", "113", "118", "121", "124", "127"]
munpos =  ["CARTAGENA", "ACHI", "ARENAL", "ALTOS DEL ROSARIO", "ARJONA", "ARROYO HONDO", "BARRANCO DE LOBA", "CALAMAR", "CANTAGALLO", "CICUCO", "CORDOBA", "CLEMENCIA", "EL CARMEN DE BOLIVAR", "EL GUAMO", "HATILLO DE LOBA", "EL PEN0N", "MAGANGUE", "MAHATES", "MARGARITA", "MARIA LA BAJA", "MONTECRISTO", "MOMPOS", "MORALES", "PINILLOS", "REGIDOR", "RIOVIEJO", "SAN ESTANISLAO", "SAN CRISTOBAL", "SAN FERNANDO", "SAN JACINTO", "SAN JACINTO DEL CAUCA", "SAN JUAN NEPOMUCENO", "SAN MARTIN DE LOBA", "SAN PABLO", "SANTA CATALINA", "SANTA ROSA", "SANTA ROSA DEL SUR", "SIMITI", "SOPLAVIENTO", "TALAIGUA NUEVO", "TIQUISIO (PTO. RICO)", "TURBACO", "TURBANA", "VILLANUEVA", "ZAMBRANO"]
DANE = ["13001", "13006", "13042", "13030", "13052", "13062", "13074", "13140", "13160", "13188", "13212", "13222", "13244", "13248", "13300", "13268", "13430", "13433", "13440", "13442", "13458", "13468", "13473", "13490", "13549", "13580", "13600", "13647", "13620", "13654", "13655", "13657", "13667", "13670", "13673", "13683", "13688", "13744", "13760", "13780", "13810", "13836", "13838", "13873", "13894"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Bolivar_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=05&cod_mpio="+amazonas[munpo]
	

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