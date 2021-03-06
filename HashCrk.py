# -*- coding: utf-8 -*-

# Python 2.x y 3.X
# Windows

# HashCrk.py
# By: LawlietJH
# v1.0.4

import hashlib
import time
import sys
import os

PythonVer = sys.version[0]
Version = "v.1.0.4"



def Tiempo(Funcion):
	
	def Envolver(*args):
		
		T1 = time.time()
		Ret = Funcion(*args)
		T2 = time.time()
		#~ print(u'\n\n\n\t [~] Función: {}'.format(Funcion.func_name))
		print('\n\n\n\t [+] Tiempo: {:0.3f} s'.format(float(T2-T1)))
		
		return Ret
		
	return Envolver


@Tiempo
def HashCrk(HASH, Tipo):
	
	if   len(HASH) == 32  and Tipo != "md5":    return "El HASH Es MD5"
	elif len(HASH) == 40  and Tipo != "sha1":   return "El HASH Es SHA1"
	elif len(HASH) == 56  and Tipo != "sha224": return "El HASH Es SHA224"
	elif len(HASH) == 64  and Tipo != "sha256": return "El HASH Es SHA256"
	elif len(HASH) == 96  and Tipo != "sha384": return "El HASH Es SHA384"
	elif len(HASH) == 128 and Tipo != "sha512": return "El HASH Es SHA512"
	
	TI = time.time()
	TF = TI
	Cont = 0
	L = []
	L.append(32)
	H = None
	
	while True:
		
		Cont += 1
		
		if   Tipo == "md5":    H = hashlib.md5()		# len(32)
		elif Tipo == "sha1":   H = hashlib.sha1()		# len(40)
		elif Tipo == "sha224": H = hashlib.sha224()		# len(56)
		elif Tipo == "sha256": H = hashlib.sha256()		# len(64)
		elif Tipo == "sha384": H = hashlib.sha384()		# len(96)
		elif Tipo == "sha512": H = hashlib.sha512()		# len(128)
		#~ elif Tipo == "ripemd160": H = hashlib.new('ripemd160')
		
		
		if PythonVer == '2':
			for C in L: H.update(chr(C))
		if PythonVer == '3':
			for C in L: H.update(chr(C).encode('UTF-8'))
		
		hash = H.hexdigest()
		
		#~ if Cont % 12000 == 0: sys.stdout.writelines("\r  >  " + ''.join([chr(C) for C in L]) + " <- # " + str(Cont))
		if Cont % 12000 == 0:
			
			TF = time.time()
			sys.stdout.writelines("\r  >  " + hash[:30] + " <- Tiempo: {:0.3f} s".format(float(TF-TI)))
		
		if hash == HASH:
			
			sys.stdout.writelines("\r  >  " + hash + "                            ")
			return ''.join([chr(C) for C in L])
		
		Envuelto = True
		
		for x in range(0, len(L)):
			
			L[x] = ((L[x] + 1) % 127)
			
			if L[x] != 0:
				Envuelto = False
				break
			else: L[x] = 32
			
		if Envuelto: L.append(32)



def GetHASH(Tipo, Cadena):
	
	Tipo = Tipo.lower()
	
	if PythonVer == '2':
		
		for Algoritmo in hashlib.algorithms:
			
			H = getattr(hashlib, Algoritmo)()
			H.update(Cadena)
			
			if   Algoritmo == "md5"    and Tipo == "md5":	 return str(H.hexdigest())
			elif Algoritmo == "sha1"   and Tipo == "sha1":	 return str(H.hexdigest())
			elif Algoritmo == "sha224" and Tipo == "sha224": return str(H.hexdigest())
			elif Algoritmo == "sha256" and Tipo == "sha256": return str(H.hexdigest())
			elif Algoritmo == "sha384" and Tipo == "sha384": return str(H.hexdigest())
			elif Algoritmo == "sha512" and Tipo == "sha512": return str(H.hexdigest())
			#~ elif Algoritmo == "ripemd160" and Tipo == "ripemd160": return str(H.hexdigest())
	
	elif PythonVer == '3':
		
		for Algoritmo in hashlib.algorithms_guaranteed:
			
			H = getattr(hashlib, Algoritmo)()
			H.update(Cadena.encode('UTF-8'))
			
			if   Algoritmo == "md5"    and Tipo == "md5":	 return str(H.hexdigest())
			elif Algoritmo == "sha1"   and Tipo == "sha1":	 return str(H.hexdigest())
			elif Algoritmo == "sha224" and Tipo == "sha224": return str(H.hexdigest())
			elif Algoritmo == "sha256" and Tipo == "sha256": return str(H.hexdigest())
			elif Algoritmo == "sha384" and Tipo == "sha384": return str(H.hexdigest())
			elif Algoritmo == "sha512" and Tipo == "sha512": return str(H.hexdigest())



def SetTipoHASH(Cadena):
	
	if   Cadena.lower().startswith("md5"   ):	return "md5"
	elif Cadena.lower().endswith(  "md5"   ):	return "md5"
	elif Cadena.lower().startswith("sha1"  ):	return "sha1"
	elif Cadena.lower().endswith(  "sha1"  ):	return "sha1"
	elif Cadena.lower().startswith("sha224"):	return "sha224"
	elif Cadena.lower().endswith(  "sha224"):	return "sha224"
	elif Cadena.lower().startswith("sha256"):	return "sha256"
	elif Cadena.lower().endswith(  "sha256"):	return "sha256"
	elif Cadena.lower().startswith("sha384"):	return "sha384"
	elif Cadena.lower().endswith(  "sha384"):	return "sha384"
	elif Cadena.lower().startswith("sha512"):	return "sha512"
	elif Cadena.lower().endswith(  "sha512"):	return "sha512"
	#~ elif Cadena.lower().startswith("ripemd160"):	return "ripemd160"
	#~ elif Cadena.lower().endswith(  "ripemd160"):	return "ripemd160"
	else:
		
		print("\n\n\n\n [!] Indica El Tipo De HASH Al Principio o Al Final:")
		print("\n\t [~] md5\n\t [~] sha1\n\t [~] sha224\n\t [~] sha256\n\t [~] sha384\n\t [~] sha512")
		print("\n [-] Ejemplos:\n\n\t md5 Hola Soy Una Cadena\t\t <- Cifrar")
		print("\n\t md5 ce52790629679d930ca16c39a4f619c3\t <- Descifrar")
		
	return None



def SetCadena(Cadena):
	
	if   Cadena.lower().startswith("md5"   ):	return Cadena.split("md5 ")[1]
	elif Cadena.lower().endswith(  "md5"   ):	return Cadena.split(" md5")[0]
	elif Cadena.lower().startswith("sha1"  ):	return Cadena.split("sha1 ")[1]
	elif Cadena.lower().endswith(  "sha1"  ):	return Cadena.split(" sha1")[0]
	elif Cadena.lower().startswith("sha224"):	return Cadena.split("sha224 ")[1]
	elif Cadena.lower().endswith(  "sha224"):	return Cadena.split(" sha224")[0]
	elif Cadena.lower().startswith("sha256"):	return Cadena.split("sha256 ")[1]
	elif Cadena.lower().endswith(  "sha256"):	return Cadena.split(" sha256")[0]
	elif Cadena.lower().startswith("sha384"):	return Cadena.split("sha384 ")[1]
	elif Cadena.lower().endswith(  "sha384"):	return Cadena.split(" sha384")[0]
	elif Cadena.lower().startswith("sha512"):	return Cadena.split("sha512 ")[1]
	elif Cadena.lower().endswith(  "sha512"):	return Cadena.split(" sha512")[0]
	#~ elif Cadena.lower().startswith("ripemd160"):	return Cadena.split("ripemd160 ")[1]
	#~ elif Cadena.lower().endswith(  "ripemd160"):	return Cadena.split(" ripemd160")[0]
	
	return None



def EsHASH(Cadena):
	
	if not " " in Cadena.strip() and len(Cadena) >= 32:
		return True
	else:
		return False



if __name__ == "__main__":
	
	os.system("Cls")
	
	#~ print(hashlib.algorithms_guaranteed)
	#~ os.system("Pause")
	
	while True:
		
		if PythonVer == '2': Cadena = raw_input("\n\n\n\t [+] HASH: ")
		elif PythonVer == '3': Cadena = input("\n\n\n\t [+] HASH: ")
		
		Tipo = SetTipoHASH(Cadena)
		
		if Tipo == None:
			
			os.system("Pause > Nul && Cls")
			continue
		
		Cadena = SetCadena(Cadena)
		
		HASH = GetHASH(Tipo, Cadena)
		
		if EsHASH(Cadena):
			
			HASH = Cadena
			
			print("\n\n [+] Buscando Coincidencias Y Mostrando cada 12 mil Hashes Probados:\n\n")
			print("\n\n\t [+] Descifrado " + Tipo.upper() + ": " + HashCrk(HASH, Tipo))
			os.system("Pause > Nul && Cls")
		
		else:
			
			print("\n\n\t [+] HASH " + Tipo.upper() + ": " + str(HASH) + "\n\n")


