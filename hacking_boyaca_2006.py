#usr/bin/python
# -*- coding: utf-8 -*- 
import urllib2
from BeautifulSoup import BeautifulSoup


''' Me faltó un municipio
'''

# Vector de Amazonas
amazonas = ["001", "007", "008", "010", "013", "016", "019", "022", "025", "028", "031", "034", "037", "040", "043", "046", "049", "052", "055", "058", "059", "060", "061", "064", "067", "068", "070", "073", "076", "077", "078", "079", "082", "085", "088", "091", "094", "097", "100", "103", "106", "109", "112", "118", "121", "124", "127", "130", "136", "137", "139", "142", "148", "151", "154", "157", "160", "161", "163", "166", "169", "173", "176", "178", "179", "181", "184", "187", "190", "193", "199", "202", "205", "214", "215", "217", "220", "223", "226", "232", "235", "237", "238", "241", "247", "248", "249", "250", "251", "253", "256", "259", "262", "265", "268", "271", "274", "277", "280", "281", "282", "283", "286", "289", "292", "298", "301", "304", "307", "310", "311", "313", "316", "319", "322", "324", "325", "328", "331", "334", "337", "340", "346"]
munpos =  ["TUNJA", "ALMEIDA", "AQUITANIA (PUEBLOVIEJO)", "ARCABUCO", "BELEN", "BERBEO", "BETEITIVA", "BOAVITA", "BOYACA", "BRICENO", "BUENAVISTA", "BUSBANZA", "CALDAS", "CAMPOHERMOSO", "CERINZA", "CIENEGA", "COMBITA", "COPER", "CORRALES", "COVARACHIA", "CUBARA", "CUCAITA", "CUITIVA", "CHINAVITA", "CHIQUINQUIRA", "CHIQUIZA", "CHISCAS", "CHITA", "CHITARAQUE", "CHIVATA", "CHIVOR", "DUITAMA", "EL COCUY", "EL ESPINO", "FIRAVITOBA", "FLORESTA", "GACHANTIVA", "GAMEZA", "GARAGOA", "GUACAMAYAS", "GUATEQUE", "GUAYATA", "GUICAN", "IZA", "JENESANO", "JERICO", "LABRANZAGRANDE", "LA CAPILLA", "LA UVITA", "LA VICTORIA", "VILLA DE LEIVA", "MACANAL", "MARIPI", "MIRAFLORES", "MONGUA", "MONGUI", "MONIQUIRA", "MOTAVITA", "MUZO", "NOBSA", "NUEVO COLON", "OICATA", "OTANCHE", "PACHAVITA", "PAEZ", "PAIPA", "PAJARITO", "PANQUEBA", "PAUNA", "PAYA", "PAZ DE RIO", "PESCA", "PISBA", "PUERTO BOYACA", "QUIPAMA", "RAMIRIQUI", "RAQUIRA", "RONDON", "SABOYA", "SACHICA", "SAMACA", "SAN EDUARDO", "SAN JOSE DE PARE", "SAN LUIS DE GACENO", "SAN MATEO", "SAN MIGUEL DE SEMA", "SAN PABLO DE BORBUR", "SANTANA", "SANTA MARIA", "SANTA ROSA DE VITERBO", "SANTA SOFIA", "SATIVANORTE", "SATIVASUR", "SIACHOQUE", "SOATA", "SOCOTA", "SOCHA", "SOGAMOSO", "SOMONDOCO", "SORA", "SORACA", "SOTAQUIRA", "SUSACON", "SUTAMARCHAN", "SUTATENZA", "TASCO", "TENZA", "TIBANA", "TIBASOSA", "TINJACA", "TIPACOQUE", "TOCA", "TOGUI", "TOPAGA", "TOTA", "TUNUNGUA", "TURMEQUE", "TUTA", "TUTAZA", "UMBITA", "VENTAQUEMADA", "VIRACACHA", "ZETAQUIRA"]
DANE = ["15001", "15022", "15047", "15051", "15087", "15090", "15092", "15097", "15104", "15001", "15109", "15114", "15131", "15135", "15162", "15189", "15204", "15212", "15215", "15218", "15223", "15224", "15226", "15172", "15176", "15232", "15180", "15183", "15185", "15187", "15236", "15238", "15244", "15248", "15272", "15276", "15293", "15296", "15299", "15317", "15322", "15325", "15332", "15362", "15367", "15368", "15377", "15380", "15403", "15401", "15407", "15425", "15442", "15455", "15464", "15466", "15469", "15476", "15480", "15491", "15494", "15500", "15507", "15511", "19517", "15516", "15518", "15522", "15531", "15533", "15537", "15542", "15550", "15572", "15580", "15599", "15600", "15621", "15632", "15638", "15646", "15660", "15664", "15667", "15673", "15676", "15681", "15686", "15690", "15693", "15696", "15720", "15723", "15740", "15753", "15755", "15757", "15759", "15761", "15762", "15764", "15763", "15774", "15776", "15778", "15790", "15798", "15804", "15806", "15808", "15810", "15814", "15816", "15820", "15822", "15832", "15835", "15837", "15839", "15842", "15861", "15879", "15897"]

campos = [6, 8, 10, 12, 14, 20, 22, 24, 26, 28, 30, 32]

# Creamos archivo plano con info de las elecciones de Amazonas
f = open('Boyaca_2006.txt', 'w')
f.write
for munpo in range(len(amazonas)):
	# Consolido el Linl
	url = "http://web.registraduria.gov.co/eleccionesPresidente/votacionPartidosMunicipios.jsp?cod_corpo=PR&cod_visibilidad=2&num_com=99&cod_depto=07&cod_mpio="+amazonas[munpo]
	

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