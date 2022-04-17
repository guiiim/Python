import sys

from pyspark import SparkContext, SparkConf


if __name__ == "__main__":

	#SparkContext
	conf = SparkConf().setAppName("Conta Palavras").set("master", "local")
	sc = SparkContext(conf = conf)

	#Carrega o arquivo
	palavras = sc.textFile("/home/hadoop/input.txt").flarMap(lambda line: line.split(" "))

	#Conta ocorrência 
	contagem = palavras.map(lambda palavra: (palavra, 1)).reduceByKey(lambda a,b: a + b)

	#Salvar resultado
	contagem.saveAsTextFile("/home/hadoop/saida")



###########################################################################################
#
# As próximas instruções devem ser executadas no Hadoop
#
###########################################################################################
#	getid app.py 		#Carregar o código python no arquivo
#	spark-submit app.py #Executar o código
#	cd saida/			#Direciona para o local onde foi salvo o arquivo
#	ls -la				#Mostra todos os arquivos do diretório
#	getid part-0000		#Abre o arquivo gerado pelo código
###########################################################################################
