from iqoptionapi.stable_api import IQ_Option
import time,json
from backports import configparser
import os
from datetime import datetime
from dateutil import tz

def GetConfig():
    global email, password, accountType, otc, primaryType, multipleType, priceType, priceValue,timeStamp, delay,minimumPayout, management_type, takeProfit, stopLoss, martingGaleQuantify, factor             
    config = configparser.ConfigParser()
    diretorio = os.path.join(os.getcwd(), "config.ini")
    config.read(diretorio)

    email               = config.get("login", 'email')
    password            = config.get("login", 'password')
    accountType         = config.get("trade", 'account_type')
    otc                 = config.get("trade", 'otc')
    primaryType         = config.get("trade", 'primary_type')
    multipleType        = config.get("trade", 'multiple_type')
    priceType           = config.get("trade", 'price_type')
    priceValue          = config.get("trade", 'price_value')
    timeStamp           = config.get("trade", 'time_stamp')
    delay               = config.get("trade", 'delay')
    minimumPayout       = config.get("trade", 'minimum_payout')
    management_type     = config.get("management", 'management_type')
    takeProfit          = config.get("management", 'take_profit')
    stopLoss            = config.get("management", 'stop_loss')
    martingGaleQuantify = config.get("martingale", 'maximum_amount')
    factor              = config.get("martingale", 'factor')

def perfil(): 
    global API
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))
	
    return perfil
	
'''
	name
	first_name
	last_name
	email
	city
	nickname
	currency
	currency_char 
	address
	created
	postal_index
	gender
	birthdate
	balance		
	'''

def timestamp_converter(x): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora)[:-6]
	

'''
	Para pegar somente a quantia da sua banca utilize: banca = API.get_balance()
'''

GetConfig()
# Abaixo deve ser inserido o login e senha
API = IQ_Option(email, password)
# Responsavel por fazer a primeira conexao
API.connect()
# Responsavel por alterar o modo da conta entre TREINAMENTO e REAL
API.change_balance('PRACTICE') # PRACTICE / REAL
# Looping para realizar a verificação se a API se conectou corretamente ou se deve tentar se conectar novamente

while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		API.connect()
	else:
		print('Conectado com sucesso')
		break
	time.sleep(1)
print(perfil)