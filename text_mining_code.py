import gzip

class TextMinning:
	def __init__(self, fileName):
		self.fileName = fileName

	def read_gz_file_in_chunks(self, chunk_size=1024):
		'''Lazy function to read a gz file piece by piece
		Default chunck size: 1K.'''
		while True:
			data = file_object.read(chunk_size)
			if not data:
				break
			yield data

	def create_subsetted_version(self):
		f = gzip.open(fileName, 'wb')
		for piece in read_gz_file_in_chunks(f):
			process_data(piece)
		fieldnames = ['entrez_id', 'word', 'average_count']

def main():
	fileName = "/Users/mtchavez/Downloads/gene_word_matrix_2011.gz"
	tm = TextMinning(fileName)
	tm.read_gz_file_in_chunks()
	tm.create_subsetted_version()
