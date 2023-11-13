'''
CONSTANTE = "Variáveis" que não vao mudar
Muitas condições ao mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade do carro atual
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1: 
    print('A velocidade do carro passou do radar 1!')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('O carro foi multado no radar 1')
