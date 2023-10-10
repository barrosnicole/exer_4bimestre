altura=float(input('digite uma altura'))
largura=float(input('digite uma largura'))
area=altura*largura
print('a área da sua parede é {}m²'.format(area))
tinta=area/2
print('é necessário {}l de tinta para pintua {}m²'.format(tinta,area))