class Slot(object):
	"""Docstring for Slot """

	def __init__(self):
		self.state = "."
	def PlaySlot(self, symbol):
		if self.state == ".":
			self.state = symbol
		else:
			print("sorry, it's already occupied by", self.state)

class Game(object):

	def __init__(self):
		self.turn = 1
		self.field = []
		for i in range(3):
			self.field.append([])
		for l in self.field:
			for i in range(3):
				l.append(Slot())
	def Play(self):
		if self.turn == 1:
			self.turn += 1
			symbol = "O"
		else:
			self.turn -= 1
			symbol = "X"
		slot = input("where do you want to play ?")
		slot = slot.split()
		for i,k in enumerate(slot):
			slot[i] = int(k)
		slot = self.field[slot[0]][slot[1]]
		slot.PlaySlot(symbol)
	def PrintGame(self):
		rapr = ""
		for i in self.field:
			for l in i:
				rapr += l.state
			rapr += "\n"
		print(rapr)
	def Winer(self):
		flag = False
		for i, k in enumerate(self.field):
			if self.field[i][0].state == self.field[i][1].state == self.field[i][2].state != ".":
				flag = True
		for i in range(0,3):
			if self.field[0][i].state == self.field[1][i].state == self.field[2][i].state != ".":
				flag = True
		if self.field[0][0].state == self.field[1][1].state == self.field[2][2].state != ".":
			flag = True
		if self.field[2][0].state == self.field[1][1].state == self.field[0][2].state != ".":
			flag = True
		if flag:
			print("congrats, player {0} won".format(self.turn))
		return flag
def main():
	game = Game()
	while not game.Winer():
		game.Play()
		game.PrintGame()
main()

