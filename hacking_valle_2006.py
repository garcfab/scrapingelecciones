#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' 
'''

# Vector de Amazonas
amazonas = ["001", "004", "007", "010", "013", "016", "019", "022", "025", "028", "031", "034", "037", "040", "043", "046", "049", "052", "055", "058", "061", "064", "067", "070", "073", "076", "079", "082", "085", "088", "091", "094", "097", "100", "103", "106", "109", "112", "115", "118", "121", "124"]
munpos =  ["CALI", "ALCALA", "ANDALUCIA", "ANSERMANUEVO", "ARGELIA", "BOLIVAR", "BUENAVENTURA", "BUGA", "BUGALAGRANDE", "CAICEDONIA", "CANDELARIA", "CARTAGO", "DAGUA", "CALIMA (DARIEN)", "EL AGUILA", "EL CAIRO", "EL CERRITO", "EL DOVIO", "FLORIDA", "GINEBRA", "GUACARI", "JAMUNDI", "LA CUMBRE", "LA UNION", "LA VICTORIA", "OBANDO", "PALMIRA", "PRADERA", "RESTREPO", "RIOFRIO", "ROLDANILLO", "SAN PEDRO", "SEVILLA", "TORO", "TRUJILLO", "TULUA", "ULLOA", "VERSALLES", "VIJES", "YOTOCO", "YUMBO", "ZARZAL"]
DANE = ["76001", "76020", "76036", "76041", "76054", "76100", "76109", "76111", "76113", "76122", "76130", "76147", "76233", "76126", "76243", "76246", "76248", "76250", "76275", "76306", "76318", "76364", "76377", "76400", "76403", "76497", "76520", "76563", "50606", "76616", "76622", "76606", "76736", "76823", "76828", "76834", "76845", "76863", "76869", "76890", "76892", "76895"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Valle_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=31&cod_mpio="+amazonas[munpo]
		

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