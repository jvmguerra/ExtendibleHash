#coding=utf-8
from math import sqrt
import copy

BUCKET_SIZE = 4
LOCAL_DEPTH_INIT = 2
GLOBAL_DEPTH_INIT = 2
CURRENT_KEY_VALUE = -1

class Hash(object):
	def __init__(self,num_buckets,profundidade_global):
		self.ponteiros_buckets = [] # LISTA QUE TEM OS MEUS BUCKETS
		self.num_buckets_anterior = num_buckets
		self.num_buckets = num_buckets ##ISSO AKI É A CHAVE DO MEU HASH
		self.profundidade_global = profundidade_global
		
		for i in range(self.num_buckets):
			bucket = Buckets()
			self.ponteiros_buckets.append(bucket)
		# for i in range(self.num_buckets):
		# 	print self.ponteiros_buckets[i].lista
		

	def Main(self):
		h.inserirElemento()
		h.printHash()

	def calcHash(self,num): ## O calculo da chave sempre é no numero de buckets 2,4,8,16 .....
		print str(num)+"%"+str(self.num_buckets) +" = "+str(num % self.num_buckets)
		return int(num) % int(self.num_buckets)

	def calcHash2(self,num): ## O calculo da chave sempre é no numero de buckets 2,4,8,16 .....
		print str(num)+"%"+str(self.num_buckets_anterior) +" = "+str(num % self.num_buckets_anterior)
		return int(num) % int(self.num_buckets_anterior)

	def bucketCheio(self,chave):
		if len(self.ponteiros_buckets[chave].lista) == BUCKET_SIZE:
			return True
		else:
			return False

	def dobraTamanho(self):    ####AKI Ó  OOOOOOO A;LSDKFJ;ALSKDJF;LASDJF;LASKDJF;LKASDFJ QUANDO DOBRA DE NOVO A PROFUNDIDADE DE TUDO VOLTA PRA 2
		
		backup = self.num_buckets
		hash_aux = Hash(self.num_buckets*2,self.profundidade_global+1)
		#print "Hash aux "+str(hash_aux.printHash())
		
		for i in range(self.num_buckets):
			hash_aux.ponteiros_buckets[i].lista = self.ponteiros_buckets[i].lista
			hash_aux.ponteiros_buckets[i].profundidade_local = self.ponteiros_buckets[i].profundidade_local


		self = copy.deepcopy(hash_aux)

		self.num_buckets_anterior = backup
		return self

	def recalcularHash3(self,bucket):

		lista_aux = []
		key_list = []
		precisaDobrar = False
		
		for i in range(len(self.ponteiros_buckets[bucket].lista)):
			lista_aux.append(self.ponteiros_buckets[bucket].lista[i])

		self.ponteiros_buckets[bucket].lista = []

		for i in range(len(lista_aux)):
			key = self.calcHash(lista_aux[i])
			#print key 
			self.ponteiros_buckets[key].lista.append(lista_aux[i])	

			if not key_list or not repetido(key,key_list):
				key_list.append(key)	

		k= self.num_buckets_anterior
		while k < self.num_buckets:
			#print ""
			#print self.ponteiros_buckets[k].lista
			
			if len(self.ponteiros_buckets[k].lista) == 0:
			#	print "entrou no if"
				self.ponteiros_buckets[k].lista = self.ponteiros_buckets[k-self.num_buckets_anterior].lista
				self.ponteiros_buckets[k].profundidade_local = self.ponteiros_buckets[k-self.num_buckets_anterior].profundidade_local
			k+=1
			#print "Depois de alterar"
			self.printHash()
		
		return self

	def recalcularHash(self,bucket):

		lista_aux = []
		key_list = []
		precisaDobrar = False
		
		for i in range(len(self.ponteiros_buckets[bucket].lista)):
			lista_aux.append(self.ponteiros_buckets[bucket].lista[i])

		self.ponteiros_buckets[bucket].lista = []

		for i in range(len(lista_aux)):
			key = self.calcHash(lista_aux[i])
			#print key 
			self.ponteiros_buckets[key].lista.append(lista_aux[i])	

			if not key_list or not repetido(key,key_list):
				key_list.append(key)	

		k= self.num_buckets_anterior
		while k < self.num_buckets:
			#print ""
			#print self.ponteiros_buckets[k].lista
			
			if len(self.ponteiros_buckets[k].lista) == 0:
			#	print "entrou no if"
				self.ponteiros_buckets[k].lista = self.ponteiros_buckets[k-self.num_buckets_anterior].lista
				self.ponteiros_buckets[k].profundidade_local = self.ponteiros_buckets[k-self.num_buckets_anterior].profundidade_local
			k+=1
			#print "Depois de alterar"
			self.printHash()
		

		print "KEY_LIST:  "+str(key_list)

		prof = self.ponteiros_buckets[bucket].profundidade_local
		prof+=1

		self.ponteiros_buckets[key_list[0]].profundidade_local = prof
		self.ponteiros_buckets[key_list[1]].profundidade_local = prof
		return self
	
	def recalcularHash2(self,bucket):

		lista_aux = []
		key_list = []
		
		lista_aux= self.ponteiros_buckets[bucket].lista[:]

		for i in range(bucket % self.num_buckets_anterior,self.num_buckets,4):
			if self.ponteiros_buckets[i] and  self.ponteiros_buckets[i].profundidade_local != self.profundidade_global:
				self.ponteiros_buckets[i].lista = []
		
	
			
		for i in range(bucket % self.num_buckets_anterior,self.num_buckets,4):
			if not self.ponteiros_buckets[i]:
				new_bucket = Buckets()
				new_bucket.atualiza(BUCKET_SIZE, self.ponteiros_buckets[bucket].profundidade_local)
				self.ponteiros_buckets[i] = new_bucket


		#print "RESULTADO DO SEGUNDO HASH: "+str(self.calcHash(bucket))+" VALOR DO BUCKET: "+str(bucket)

		for i in range(len(lista_aux)):
			key = self.calcHash(lista_aux[i])
			print "KEY = "+str(key) 
			self.ponteiros_buckets[key].lista.append(lista_aux[i])	

			if not key_list or not repetido(key,key_list):
				key_list.append(key)	



		k= self.num_buckets_anterior
		while k < self.num_buckets:
			print ""
			print "Lista do bucket que eu to: "+str(self.ponteiros_buckets[k].lista)
			raw_input()
			if len(self.ponteiros_buckets[k].lista) == 0:
				print "entrou no if"
				self.ponteiros_buckets[k].lista = self.ponteiros_buckets[k-self.num_buckets_anterior].lista
				self.ponteiros_buckets[k].profundidade_local = self.ponteiros_buckets[k-self.num_buckets_anterior].profundidade_local
			k+=1
			print "Depois de alterar"
			self.printHash()
		
		
		
		
		prof = self.ponteiros_buckets[bucket].profundidade_local
		prof+=1
		
		self.ponteiros_buckets[key_list[0]].profundidade_local = prof
		self.ponteiros_buckets[key_list[1]].profundidade_local = prof
		

		print "KEY LIST:"+str(key_list)
		
		return self
	

	def printHash(self):
		print "Profundidade Global: "+str(self.profundidade_global)
		for i in range(self.num_buckets):
		 	print "Bucket "+str(i)+": "+str(self.ponteiros_buckets[i].lista)+"Profundidade Local: "+str(self.ponteiros_buckets[i].profundidade_local)

	def precisaDobrar(self,chave):
		
		prof_loc  = self.ponteiros_buckets[chave].profundidade_local +1
		if self.profundidade_global < prof_loc:	
			return True
		else:
			return False

	def primaryKey(self,elem):
		for i in range(len(self.ponteiros_buckets)):
			for j in range(len(self.ponteiros_buckets[i].lista)):
				if self.ponteiros_buckets[i].lista[j] == elem:
					return False
		return True

	def restoIgual(self,bucket,elem):
		print "Entrou ni mim"
		try:
			primeiro = self.calcHash(self.ponteiros_buckets[bucket].lista[0])
		except(IndexError):
			return False
		
		if len(self.ponteiros_buckets[bucket].lista) <4:
			return False
		else:
			for i in range(len(self.ponteiros_buckets[bucket].lista)):
				if self.calcHash(self.ponteiros_buckets[bucket].lista[i]) != primeiro:
					return False
		print "retornou True"
		return True


	def inserirElemento(self):
		flag =False
		print "Digite q para sair"
		while(True):
			
			print "Digite um elemento para inserir:"
			while(True):
				try:
					elem = raw_input()
					if elem == 'q':
						return
					elem = int(elem)	
					flag = self.primaryKey(elem)
					elem2 = Elemento(elem,"joaozinho","maria")

					if flag == True:
						break
					else:
						print "Valor ja inserido"
				except ValueError :
					print "Digite um elemento valido!"

			

			chave = self.calcHash(elem)
			while True:
				if self.restoIgual(chave,elem):
					print "if"
					self = self.dobraTamanho()
					self = self.recalcularHash3(chave)
					chave = self.calcHash(elem)
					
					
					self.printHash()
				else:
					break

			if ((self.bucketCheio(chave) and self.precisaDobrar(chave))):
				print "if"
				self = self.dobraTamanho()
				self = self.recalcularHash(chave)
				chave = self.calcHash(elem)
				self.ponteiros_buckets[chave].lista.append(elem)
				
				self.printHash()
			
			elif self.bucketCheio(chave) and not self.precisaDobrar(chave):
				print "elif"
				#if self.ponteiros_buckets[chave].lista == self.ponteiros_buckets[self.calcHash(chave)].lista:
					#print "entrou no if dentro do elif"
				self = self.recalcularHash2(chave)
				self.ponteiros_buckets[chave].lista.append(elem)
				#else:
				#	print "entrou no else dentro do elif"
				#	pass
				
				self.printHash()
			
			else:
				print "else"
				self.ponteiros_buckets[chave].lista.append(elem)
				self.printHash()
		return self


class Buckets(object):
	def __init__(self):
		self.tamanho = BUCKET_SIZE
		self.profundidade_local = LOCAL_DEPTH_INIT
		self.lista = []

	def atualiza(self,tam_bucket,profundidade):
		self.tamanho = tam_bucket
		self.profundidade_local = profundidade
		self.lista = []
		


	
def repetido(chave,lista_chave):
		flag = False
		for i in range(len(lista_chave)):
			if lista_chave[i] == chave:
				return True
		return False

class Elemento(object):
	def __init__(self,chave,pid,sid):

		self.key =  chave  #CURRENT_KEY_VALUE +1
		self.elemento = [(chave),[(pid),(sid)]]
		

	
	

h = Hash(4,GLOBAL_DEPTH_INIT)
h.Main()








