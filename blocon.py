bloco = open('infos.txt','r')


for p in bloco:
    p = p.rstrip()
    if 'emails' in p:
        email = p[8:]
    if 'senha1' in p:
        senha = p[8:]
    if 'rp' in p:
        rp = p[4:]
    if 'par' in p:
        par = p[5:]
    if 'entrada' in p:
        entrada = p[9:]
    if 'direcao' in p:
        direcao = p[9:]
    if 'timef' in p:
        timef = p[7:]
    if 'gales' in p:
        gale = p[7:]
    if 'tempo' in p:
        tempo = p[7:]





        