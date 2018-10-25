def BlackPawn(place, x , y):
	x-=1
	y-=1
	place[y].pop(x)
	place[y].insert(x,"♟")
	return place

def WhitePawn(place, x , y):
	x-=1
	y-=1
	place[y].pop(x)
	place[y].insert(x,"♙")
	return place


def table():
	x = 8
	old_table= [["."]*x for y in range(8)]
	end_table = AddPions(old_table)
	
	for a in end_table:
		print(a,'\n')

def AddPions(place):
	for N in range(9):
		resutlat = BlackPawn(place,N,2)
	for N in range(9):
		resutlat = WhitePawn(resutlat, N , 7)



	return resutlat

def main():
	table()






if __name__ == '__main__':
	main()