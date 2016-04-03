#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' Borre Guachene. No existe
'''

# Vector de Amazonas
amazonas = ["001", "004", "005", "006", "007", "010", "013", "016", "019", "022", "025", "027", "028", "031", "034", "037", "040", "043", "046", "049", "052", "053", "055", "058", "060", "061", "064", "067", "070", "073", "076", "079", "082", "085", "086", "087", "088", "091", "094", "097", "098"]
munpos =  ["POPAYAN", "ALMAGUER", "ARGELIA", "BALBOA", "BOLIVAR", "BUENOS AIRES", "CAJIBIO", "CALDONO", "CALOTO", "CORINTO", "EL TAMBO", "FLORENCIA", "GUAPI", "INZA", "JAMBALO", "LA SIERRA", "LA VEGA", "LOPEZ (MICAY)", "MERCADERES", "MIRANDA", "MORALES", "PADILLA", "PAEZ (BELALCAZAR)", "PATIA (EL BORDO)", "PIAMONTE", "PIENDAMO", "PUERTO TEJADA", "PURACE (COCONUCO)", "ROSAS", "SAN SEBASTIAN", "SANTANDER DE QUILICHAO", "SANTA ROSA", "SILVIA", "SOTARA (PAISPAMBA)", "SUCRE", "SUAREZ", "TIMBIO", "TIMBIQUI", "TORIBIO", "TOTORO", "VILLA RICA"]
DANE = ["19001", "19022", "19050", "19075", "19100", "19110", "19130", "19137", "19142", "19212", "19256", "18001", "19318", "19355", "19364", "19392", "19397", "19418", "19450", "19455", "13473", "19513", "19517", "19532", "19533", "19548", "19573", "19585", "19622", "19693", "19698", "13683", "19743", "19760", "19785", "19780", "19807", "19809", "19821", "19824", "19845"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Cauca_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=11&cod_mpio="+amazonas[munpo]
	

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