ORADEA = 'Oradea'
ZERIND = 'Zerind'
SIBIU = 'Sibiu'
ARAD = 'Arad'
TIMISORA = 'Timisora'
LUGOJ = 'Lugoj'
MEHADIA = 'Mehadia'
DROBETA = 'Drobeta'
CRAVIOVA = 'Craviova'
RIMMICU VILCEA = 'Rimmicu Vilcea'
FAGARAS = 'Fagaras'
PITESTI = 'Pitesti'
BUCHAREST = 'Bucharest'
GIURGIU = 'Giurgiu'
URZICENI = 'Urziceni'
EFORIE = 'Eforie'
NEAMT = 'Neamt'
IASI = 'Iasi'
VASLUI = 'Vaslui'
HIRSOVA = 'Hirsova'
URZICENI = 'Urziceni'

graph = [
    [ORADEA, [[ZERIND, 71], [SIBIU, 151]]],
    [ZERIND, [[ARAD, 75], [ORADEA, 71]]],
    [ARAD, [[SIBIU, 140], [TIMISORA, 118],[ZERIND, 75]]],
    [SIBIU, [[ORADEA, 151], [ARAD, 140],[FAGARAS, 99], [RIMMICU VILCEA, 80]]],
    [FAGARAS, [[BUCHAREST, 211], [SIBIU, 99]]],
    [TIMISORA, [[ARAD, 118], [LUGOJ, 111]]],
    [LUGOJ, [[MEHADIA, 70], [TIMISORA, 111]]],
    [MEHADIA, [[LUGOJ, 70], [DROBETA, 75]]],
    [DROBETA, [[CRAVIOVA, 120], [MEHADIA, 75]]],
    [CRAVIOVA, [[DROBETA, 120], [PITESTI, 138], [RIMMICU VILCEA, 146]]],
    [RIMMICU VILCEA, [[SIBIU, 80], [PITESTI, 97], [CRAVIOVA, 146]]],
    [PITESTI, [[BUCHAREST, 101], [RIMMICU VILCEA, 97], [CRAVIOVA, 138]]],
    [BUCHAREST, [[PITESTI, 101], [FAGARAS, 211], [GIURGIU, 90], [URZICENI, 85]]],
    [URZICENI, [[VASLUI, 142], [HIRSOVA, 98], [BUCHAREST, 85]]],
    [HIRSOVA, [[EFORIE, 86], [URZICENI, 98]]],
    [VASLUI, [[URZICENI, 142], [IASI, 92]]],
    [IASI, [[NEAMT, 87], [VASLUI, 92]]],
    [GIURGIU, [[BUCHAREST, 90]]],
    [NEAMT, [[IASI, 87]]],
    [EFORIE, [[HIRSOVA, 86]]],
]

