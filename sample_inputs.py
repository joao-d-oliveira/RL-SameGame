def sample_input1():
    txt = """20 10 2
BRBBBBRRBB
RBRBBRRRRR
BRBBRRRBBB
BRRRBBBRBR
BBBBRBRRBR
BRBRRBRRRB
BBRBRBRBBB
RBRBRBRRBR
BRRRRRBBRB
RRRRBRRRRB
BRRRBBBRBR
RRBRRBBBRB
RBBBBBBBBB
BRBBRBRBBR
RBRBBBRRRB
RBRBRBRBBB
BRRRBRBRRR
RRBRBBBBBR
RBBRBBRBRB
BBBBRRBBRB"""

    txt = txt.split('\n')
    x, y, k = map(int, txt[0].split())
    board = [[j for j in txt[i].strip()] for i in range(1, x + 1)]
    return x, y, k, board


def sample_input2():
    txt = """20 10 3
BBRBYBBRRB
YBYBYBRRBB
YYRRYYYBBB
YRRRYRBBBB
RRRYYBYYYR
YBBYYRYYBB
RRYRYYBRBY
RRRRYRYYRY
BRRYYRRYYB
RRYRBBBRRY
RBYBYRYYRR
BYBYYBRYBY
BRRBRYRYRB
RBYRRYBYYY
BRYYRYRRBY
BRRYYBYRBY
YBYYBYBBYB
RBYYRRYBRB
BYYBYYRBYB
YBRBYYRRRR"""

    txt = txt.split('\n')
    x, y, k = map(int, txt[0].split())
    board = [[j for j in txt[i].strip()] for i in range(1, x + 1)]
    return x, y, k, board


def sample_input3():

    txt = """20 10 6
BGOBVBGROB
YBYBVGRRGG
VYOOYYYBBB
VRRRVOBGBG
OOOVYBYYVR
VGBYYOYYGB
OOYOYVGOBV
ROROYOYYOY
BRRYYROVYB
RRYRBGGRRV
OGYGVOVYOR
GYBYYBOVGV
GOOBOVOVOB
OGVORVGVVY
GOYVOVRRGV
GORVYBYOBV
VGYYBYBGYG
RGVYOOVBOG
GVVGVVRBYB
VBOBYYOORO"""

    txt = txt.split('\n')
    x, y, k = map(int, txt[0].split())
    board = [[j for j in txt[i].strip()] for i in range(1, x + 1)]
    return x, y, k, board


def sample_input4():
    txt = """20 10 5
OBYRORBYGB
YYRGOBRBYB
BOYGYRYOYR
GYYOGYOBBY
GOBGGYOGRR
OBBRBOYRBB
RRGYBRBGOY
GRYRGYGGOR
YOBOOGOBGG
YRBOGYBBGG
RRGOYBYYYY
YBBRBBRGGG
RGBYYBBRGY
YBYOBRBOGG
OBYGOGROOR
RGBOORBBBR
GOGOBRORGG
GGYBOBYRGB
YBYORYGBOR
GYROOOOBOG"""

    txt = txt.split('\n')
    x, y, k = map(int, txt[0].split())
    board = [[j for j in txt[i].strip()] for i in range(1, x + 1)]
    return x, y, k, board


def input_stdin():
    x, y, k = map(int, input().strip().split())
    board = [[j for j in input().strip()] for _ in range(x)]

    return x, y, k, board
