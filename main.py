from lib.Machine.machine import Machine

game = Machine()
game.start()

while True:
    game.showWord()
    game.updateWord()