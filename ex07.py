#!/usr/bin/env python
# -*- coding: utf-8 -*-


#=================================  HEADER  ====================================

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


#-------------------------------------------------------------------------------



#================================  TELEGRAM  ===================================

class TelegramCtrl:
	def __init__(self,token):
		print("aaa")
		self.bot = telegram.Bot(token)
		try:
			self.update_id = self.bot.get_updates()[0].update_id
		except IndexError:
			self.update_id = None
		print("bbbb")
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.buffer = []

	def next(self):
		if len(self.buffer) > 0:
			return self.buffer.pop(0)
		while len(self.buffer) == 0:
			try:
				for task_conn in self.bot.get_updates(offset=self.update_id, timeout=10):
					self.update_id = task_conn.update_id + 1
					self.buffer.append( TelegramTask(task_conn) )
			except NetworkError:
				sleep(1)
		return self.buffer.pop(0)


class TelegramTask:
	def __init__(self,request):
		self.request = request
		self.out_raw = ""

	def __del__(self):
		self.flush()

	def input(self):
		if self.request.message:
			return self.request.message.text
		return ""

	def output(self,value):
		self.out_raw += value
		self.flush()

	def flush(self):
		if self.out_raw != "":
			self.request.message.reply_text(self.out_raw)
		self.out_raw = ""


#-------------------------------------------------------------------------------





#==================================  MAIN  =====================================

class FPU:


	def calc(self,raw):
		print(raw)
		words = raw.split(' ')
		print(words)

		for item in words:
			print(item)
			print(self.pilha)
			if item == '+':
				self.sum()

			elif item == '-':
				self.sub()	
			else:
				num = int(item)
				self.push(num)	


	def __init__(self):
		self.pilha = []	

	def push(self,val):
		self.pilha.append(val)
	
	def pop(self):
		num = self.pilha.pop()
		return num

	def sum(self):
		a = self.pop()
		b = self.pop()

		self.push(a+b)

	def sub(self):
		b = self.pop()
		a = self.pop()

		self.push(a-b)	





def main_tty():
	calculator = FPU()
	
	while True:

		texto = input()
		calculator.calc(texto)

		print("Resultado(s): ", calculator.pilha)	


#-------------------------------------------------------------------------------



#==================================  MAIN  =====================================

def main():
	print("aqui")
	client = TelegramCtrl('729071996:AAHkhte8uYNM_1YwO-rbItsheGmKGm6Kl88')
	print("opa")
	while True:
		task = client.next()
		raw = task.input()

		calculator = FPU()
		calculator.calc(raw)




		task.output( str(calculator.pilha) )





#if __name__ == '__main__':

try:
	main()
except (KeyboardInterrupt):
	print("saindo")


#-------------------------------------------------------------------------------
