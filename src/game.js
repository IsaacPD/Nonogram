import {PythonShell} from 'python-shell'
let $ = require('jquery')

function start(){
	grid = $('#grid')
}

while not game.won:
		print(game)
		guess = [int(x) for x in input('Guess: ').split(' ')]
		game.make_guess(guess[0], guess[1], guess[2])

$(document).ready(start)