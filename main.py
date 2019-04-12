class Moves():
	def Pawn(table, x, y):
		pass

class Black():

				
	def Pawn(place, x , y):
		x-=1
		y-=1
		place[y].pop(x)
		place[y].insert(x,"♟")
		return place

class White():
	def Pawn(place, x , y):
		x-=1
		y-=1
		place[y].pop(x)
		place[y].insert(x,"♙")
		return place

class board():
	"""docstring for board"""
	def table():
		x = 8
		old_table= [[""]*x for y in range(8)]
		end_table = board.AddPions(old_table)
	
		for a in end_table:
			for b in a:
				print(b, end = "  ")
			print("\n")

	def AddPions(place):
		for N in range(9):
			resutlat = Black.Pawn(place,N,2)
		for N in range(9):
			resutlat = White.Pawn(resutlat, N , 7)
		return resutlat
	def update_table(before):
		for a in (before):
			for b in a:
				print(b, end = "  ")
			print("\n")


def main():
	board.table()






if __name__ == '__main__':
	main()