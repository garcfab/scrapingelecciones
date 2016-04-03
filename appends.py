# usr/bin

file = [ 'Antioquia_2006.txt', 'Arauca_2006.txt', 'Atlantico_2006.txt', 'Bolivar_2006.txt', 'Boyaca_2006.txt', 'Caldas_2006.txt', 'Caqueta_2006.txt', 'Casanare_2006.txt', 'Cauca_2006.txt', 'Cesar_2006.txt', 'Choco_2006.txt', 'Cordoba_2006.txt', 'Cundinamarca_2006.txt', 'Guainia_2006.txt', 'Guajira_2006.txt', 'Guaviare_2006.txt', 'HUILA_2006.txt', 'Magdalena_2006.txt', 'Meta_2006.txt', 'Narino_2006.txt', 'NteSantander_2006.txt', 'Putumayo_2006.txt', 'Quindio_2006.txt', 'Risaralda_2006.txt', 'SanAndres_2006.txt', 'Sucre_2006.txt', 'Tolima_2006.txt', 'Valle_2006.txt', 'Vaupes_2006.txt', 'Vichada_2006.txt']
fout=open("Base/out.tsv","a")

cont = 0
for line in open('Amazonas_2006.txt'):
	fout.write(file[0])
	fout.write('\t')
	fout.write(line)

for l in file:
	f = open(l)
	f.next()
	for line in f:
		fout.write(line)
	f.close()

fout.close()
