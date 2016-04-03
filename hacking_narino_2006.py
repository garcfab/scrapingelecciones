#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "017", "019", "022", "025", "028", "031", "034", "037", "038", "039", "040", "041", "043", "044", "046", "047", "049", "052", "055", "058", "061", "064", "067", "073", "076", "077", "078", "079", "080", "082", "085", "088", "091", "094", "095", "096", "097", "098", "100", "101", "103", "106", "109", "112", "115", "118", "120", "121", "123", "124", "125", "127", "130", "133", "136", "139", "142", "145"]
munpos =  ["PASTO", "ALBAN (SAN JOSE)", "ALDANA", "ANCUYA", "ARBOLEDA (BERRUECOS)", "BARBACOAS", "BELEN", "BUESACO", "COLON (GENOVA)", "CONSACA", "CONTADERO", "CORDOBA", "CUASPUD (CARLOSAMA)", "CUMBAL", "CHACHAGUI", "CUMBITARA", "EL ROSARIO", "EL CHARCO", "EL TABLON", "EL PENOL", "EL TAMBO", "FRANCISCO PIZARRO (SALAHONDA)", "FUNES", "GUACHUCAL", "GUAITARILLA", "GUALMATAN", "ILES", "IMUES", "IPIALES", "LA CRUZ", "LA FLORIDA", "LA LLANADA", "LA TOLA", "LA UNION", "LEIVA", "LINARES", "LOS ANDES (SOTOMAYOR)", "MAGUI (PAYAN)", "MALLAMA (PIEDRANCHA)", "MOSQUERA", "OLAYA HERRERA", "NARINO", "OSPINA", "POLICARPA", "POTOSI", "PROVIDENCIA", "PUERRES", "PUPIALES", "RICAURTE", "ROBERTO PAYAN (SAN JOSE)", "SAMANIEGO", "SANDONA", "SAN BERNARDO", "SAN LORENZO", "SAN PEDRO DE CARTAGO", "SAN PABLO", "SANTA BARBARA (ISCUANDE)", "SANTACRUZ (GUACHAVES)", "SAPUYES", "TAMINANGO", "TANGUA", "TUMACO", "TUQUERRES", "YACUANQUER"]
DANE = ["52001", "52019", "52022", "52036", "52051", "52079", "15087", "52110", "52203", "52207", "52210", "52215", "52224", "52227", "52240", "52233", "52256", "52250", "52258", "52254", "52260", "52520", "52287", "52317", "52320", "52323", "52352", "52354", "52356", "52378", "52381", "52385", "52390", "52399", "52405", "52411", "52418", "52427", "52435", "52473", "52490", "52480", "52506", "52540", "52560", "52565", "52573", "52585", "52612", "52621", "52678", "52683", "52685", "52687", "52694", "52693", "52696", "52699", "52720", "52786", "52788", "52835", "52838", "52885"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Narino_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=23&cod_mpio="+amazonas[munpo]
		

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