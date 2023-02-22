
from telethon import TelegramClient, utils
import asyncio
from pyrogram import Client
import csv
import os
from licensing.models import *
from licensing.methods import Key, Helpers
from key import keys
THANOS='https://t.me/THANOS_PRO'
from colorama import init, Fore
import asyncio
from rich.console import Console
from telethon.errors import *
import time
from telethon import functions, types
from rich.table import Table
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
numbers=[]
import itertools
with open('phone.txt') as phonefile:
	numbersphonefile=phonefile.readlines()
	for num in numbersphonefile:
		numbers.append(num.strip())
print(numbers) 
	
	

async def scrap():
	num=numbers[0]
	sum=0
	user=TelegramClient (f'sessions/{utils.parse_phone(num) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775') 
	await user.connect() 
	if not await user.is_user_authorized() :
		await user.start(phone=utils.parse_phone(num)) 
	users=[]
	entity=input("Eɴᴛᴇʀ ᴛᴇʀɢᴇᴛ ɢʀᴏᴜᴘ ᴜʀʟ")
	query=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	print("Fᴇᴛᴄʜɪɴɢ ᴍᴇᴍʙᴇʀs ") 
	for key in query:
		
		offset=0
		while True:
			print(f"  \r {sum} ",end="\r") 
			try :
				part=await user(functions.channels.GetParticipantsRequest(entity ,types.ChannelParticipantsSearch(key),offset,limit=100,hash=0))
			except Exception as e:
				print(e) 
			else:
				if not part.users:
					break
				if part.users:
					for participant in part.users:
						if participant.username:
							
							users.append([participant.username])
					offset+=len(part.users)
					sum+=len(part.users)
						
	user.disconnect()
	#saving to csv
	with open('users.csv','a') as t:
		t.truncate(0) 
		writer=csv.writer(t, delimiter="," , lineterminator='\n')
		writer.writerows(users) 
		print('members saved successfully')
		
RSAPubKey = "<RSAKeyValue><Modulus>zCezMYuC95elPWOAz/wApF/OKRRTEr0NI+cPiyTb6ev3hsY75cxQ424OkQvPelA47CeQdjONCP9J1O79qOT2+b0pQJ6KksjJGqawRIsyG50WzAgwER/lbKC6/Dmy+V58nkJQO5VnUqaK6+8M28uiz21LjGfh9IGAecUYLl0bOtKqu6hFUYxMBN97pqQAB0qg6UyEohc73MEJWtKDW/d8mWaBaJxUTh20Pxpa2zVqDbyhXlF2nejrthqiFtAKY849H9vxNAWrqyrtBKw4nug5Gu+wbV8fgNCsZBkIs/3FZZG8bw07jtLwH3KkdEJKGDtY9cQvpZWbOsbNes0Ul7/ubw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"# ENTER RSAKEY
auth = "WyIzODc1ODUzMiIsIlFtOWZEVU83U3RjRUV3WGtWRFZWcW1WRFZjUTFaTUVodzl6VSt6N0kiXQ==" ## AUTHKEY WITH ACTIVATE !
#api = requests.get('https://raw.githubusercontent.com/thanosv4/blob/main/version.txt')
def Authkey():
    key = keys #str(input(" Enter Auth Key :-"))
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id='18387', \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
    else:
    # everything went fine if we are here!
        print("The license is valid!")
        pass

async def adder() :
	entity_to_add=input('Eɴᴛᴇʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴜʀsername with @ ') 
	
	starting_user=int(input('Eɴᴛᴇʀ ᴛʜᴇ sᴛᴀʀᴛɪɴɢ ᴜsᴇʀ ')) 
	#entity_to_target=input('Enter target group url') 
	for num in numbers:
		
		users=[]
		user=Client (f'sessionss/{utils.parse_phone(num) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775') 
		await user.connect() 
		print("ᴡᴀɪᴛ ᴊᴏɪɴ ᴜʀ ɢʀᴏᴜᴘ ")
		user.join_chat(entity_to_add)
		print("ᴊᴏɪɴ ᴅᴏɴᴇ ")
		time.sleep(3)       #user(JoinChannelRequest(entity_to_add))
        #time.sleep(4)
		#print("join done")
		#if not await user.is_user_authorized() :
			#user.start(phone=utils.parse_phone(num)) 
		with open('users.csv') as t:
			for username in itertools.islice(t, starting_user, starting_user+50) :
				users.append(username) 
		num_of_users_added=1
		if not users:
			print("All users Added") 
			break
		try:
			await user.join_chat(entity_to_add)
		except Exception as e :
			print (e) 
		for user_to_add in users:
			print(f' {num_of_users_added} :- {user_to_add}') 
			try:
				await user.add_chat_members(entity_to_add, [user_to_add])
				time.sleep(5) 
				print('Dᴏɴᴇ') 
			except Exception as e :
				print(e) 
				time.sleep(10) 
				try:
					if e.seconds:
						time.sleep(e.seconds) 
				except:
					pass
			num_of_users_added+=1
		starting_user+=num_of_users_added
		user.disconnect() 
async def add_account():
	number=input('Eɴᴛᴇʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ') 
	client=TelegramClient (f'sessions/{utils.parse_phone(number) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775') 
	await client.connect() 
	if not await client.is_user_authorized():
		await client.start(phone=utils.parse_phone(number)) 
	with open('phones.text', 'a') as phonew:
		phonew.writelines("\n")
		phonew.writelines(number)
		phonew.close() 
	value=int(input('Eɴᴛᴇʀ 1 ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴏʀᴇ ᴀᴄᴄᴏᴜɴᴛ ᴇʟsᴇ ᴇɴᴛᴇʀ ᴀɴʏ ᴋᴇʏ ᴛᴏ ᴏ̨ᴜɪᴛ:-')) 
	if value==1:
		await add_account()
	else:
		quit() 
async def make_admin() :
	admin_number=int(input('Enter the index of admin number')) 
	num_admin=numbers[admin_number]
	admin_client=TelegramClient(f'sessions/{utils.parse_phone(num_admin) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775')
	if not admin_client.is_user_authorized():
		admin_client.start(phone=utils.parse_phone(number)) 
	for num in numbers:
		client=TelegramClient (f'sessions/{utils.parse_phone(num) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775') 
		await client.connect() 
		if not client.is_user_authorized():
			client.start(phone=utils.parse_phone(number)) 
		admin_rights=types.ChatAdminRights(change_info=True, delete_messages=True, ban_users=True, invite_users=True,pin_messages=True, add_admins=True, anonymous=False,other=True) 
		try:
			results=admin(functions.channels.EditAdminRequest(channel=channel, user_id=me.id, admin_rights=admin_rights, rank='TeleX') ) 
			print("admin approved") 
			time.sleep(3) 
		except Exception as e:
			print(e) 
			time.sleep(1)
		client.disconnect() 
	admin_client.disconnect() 
	
async def tlogins():
	i=1
	for num in numbers:
		number=utils.parse_phone(num) 
		print(f" {i} --{number}") 
		client=TelegramClient(f'sessions/{utils.parse_phone(number) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775')
		try:
			await client.connect() 
		except  Exception as e:
			print(e) 
		if not await client.is_user_authorized() :
			await client.start(phone=number) 
		try:
			await client.get_me()
			print("logged_in") 
			await client(JoinChannelRequest(THANOS))
		except  Exception as e:
			print(e) 
		await client.disconnect() 
		i+=1
		
async def join():
	i=1
	for num in numbers:
		number=utils.parse_phone(num) 
		print(f" {i} --{number}") 
		joining=input("ENTER GROUP URL")
		client=TelegramClient(f'sessions/{utils.parse_phone(number) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775')
		try:
			await client.connect() 
		except  Exception as e:
			print(e) 
		if not await client.is_user_authorized() :
			await client.start(phone=number) 
		try:
			await client.get_me()
			print("logged_in")
			await client(JoinChannelRequest(joining))
		except  Exception as e:
			print(e) 
		await client.disconnect() 
		i+=1
	
def updates():
	print('checking updates ')
	try:
	    version = requests.get(' ')
	except:
		print("network error")
		exit()
	if float(version.txt) > 2.0:
		r = str(input("update available [version {version.text}]. download?[y/n] "))
		if r in {'y', 'yes', 'Y'}:
			print(" downloading updates wait ")
			if os.name == 'nt':
				os.system('del pyro.py')
			else:
				os.system('rm pyro.py')
		os.system('curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/add.py')
		print('updated')
		input('enter ')
		exit()
	else:
		print(" update aborted")
		input('enter ')
   
	
	
async def logins():
	i=1
	for num in numbers:
		number=utils.parse_phone(num) 
		print(f" {i} --{number}") 
		async with Client(f'sessionss/{utils.parse_phone(number) }', api_id='26094266', api_hash='4e1b477203976969b56ef26477afe775') as app:
			await app.send_message("me", "Greetings from **Pyrogram**!")
        #await app.send_message("me", "Greetings from **Pyrogram**!")
		#try:
		app.connect() 
		app.disconnect()
		#except  Exception as e:
			#print(e) 
		#if not await app.is_user_authorized() :
			#await app.start(phone=number) 
		#try:
		#await app.get_me()
		print("logged_in") 
			#await client(JoinChannelRequest(THANOS))
		#except  Exception as e:
			#print(e) 
		#await app.disconnect() 
		i+=1
def remove_account() :
	index= int(input('ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴀᴄᴄᴏᴜɴᴛ ɪɴᴅᴇx ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ'))
	num_to_remove=numbers[num_to_remove]
	with open('phone.txt', 'a') as t:
		t.truncate(0) 
		for num in number:
			if num != num_to_remove:
				t.writelines(num) 
		t.close() 
		print("account removed successfully ")
#def main() :
#def main():
	#print("1add account")
	#print("2add members")
	#a=int(input("enter "))
	#if a ==1:
		#asyncio.run(add_account())
	#if a ==2:
		#asyncio.run(adder())
	#if a ==3:
		#asyncio.run(scrap())
		
	#pass
#asyncio.run(adder()) 

#main()
class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]
		
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def banner():
    import random
    # fancy logo
    b = [
    
' ╔══╦╗╔╦══╦═╦╦═╦══╗',
' ╚╗╔╣╚╝║╔╗║║║║║║══╣',
'─ ║║║╔╗║╠╣║║║║║╠══║',
'─ ╚╝╚╝╚╩╝╚╩╩═╩═╩══╝',
    ]
    
    
rishau = "OWNER┈˃̶ HARSHIT \nDEVELOPER┈˃̶ HARSHIT AND RISHABH\n FOR ANY SUPPORT message @thanosceo"
    
rhs = color.Red+"             ▒█▀▀▄ ▀█▀ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀█ ▒█▄░▒█ "
rhh = color.Red+"             ▒█░▒█ ▒█░ ▒█▄▄█ ▒█▒█▒█ ▒█░░▒█ ▒█▒█▒█ "
rhr = color.Red+"             ▒█▄▄▀ ▄█▄ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄█ ▒█░░▀█"
#rhks = color.Red+"                ─ ╚╝╚╝╚╩╝╚╩╩═╩═╩══╝"

def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()
#time.sleep(0.5)
print("hello")
time.sleep(0.1)
def bars():
	
    clr()
    banner()
   # time.sleep(sleep)
   # time.sleep(0.5)
    slowprint(rhs,0.01)
    slowprint(rhh,0.01)
    slowprint(rhr,0.01)
    #slowprint(rhks,0.01)
    print(" ")
    slowprint(rishau,0.01)
    print(" ")
    slowprint(lg+'╭────⇌ᴅɪᴀᴍᴏɴ⇋────'+n,0.01)
    slowprint(lg+'◈┈˃̶ <1> LOGIN ᴀᴄᴄᴏᴜɴᴛꜱ Pyrogram '+n,0.01)
    slowprint(lg+'◈┈˃̶ <2> LOGIN ᴀᴄᴄᴏᴜɴᴛꜱ telethon '+n,0.01)
    slowprint(lg+'◈┈˃̶ <3> ꜱᴄʀᴀᴘᴇʀ'+n,0.01)
    slowprint(lg+'◈┈˃̶ <4> ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ pyrogram'+n,0.01)
    slowprint(lg+'◈┈˃̶ <5> join group telethon '+n,0.01)
    slowprint(lg+'◈┈˃̶ <6> update ur pyropremium  '+n,0.01)
    slowprint(lg+'◈┈˃̶ <7> ѕнυт∂σωη'+n,0.01)
    slowprint(lg+'╰────⇌ᴅɪᴀᴍᴏɴ⇋────'+n,0.01)
    a = int(input(color.Red+'\nEɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ: '))
    if a==1:
    	asyncio.run(logins())
    if a==2:
    	asyncio.run(tlogins())
    if a==3:
    	asyncio.run(scrap())
    if a==4:
    	asyncio.run(adder())
    if a==5:
    	asyncio.run(join())
    if a==7:
    	exit()
    	
    	
def Authkeys():
    key = keys #str(input(" Enter Auth Key :-"))
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id='18921', \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
    else:
    # everything went fine if we are here!
        print("The license is valid!")
        time.sleep(4)
        pass
        bars()
        
#Authkeys()



def veryfy():
        
    if keys == "":
        key = input('enter ur activation key ')
        if key == "":
            print('wrong key contact rishabh')
        else:
            file = open('key.py', 'w')
            file.write('keys='+'"'+key+'"')
            file.close
            Authkeys()
            
    else:
            Authkeys()
            
veryfy()
            
            

