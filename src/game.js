import {PythonShell} from 'python-shell'
let $ = require('jquery')

BLACK = 0
WHITE = 1

var game

let options = {
	mode: 'text',
	pythonOptions: ['-u'],
	args: ['python/dribbble-1.png']
}

function start(){
	grid = $('#grid')
	var r
	PythonShell.run('game.py', options, function(err, results){
		if (err) throw err
		r = results
		console.log('results: %j', results)
	})
	game = new Game(r[0], r[1], r[2], r[3])
}

class BitVector2D {
	constructor(rows, cols, vector) {
		this.r = rows
		this.c = cols
		this.vector = vector
	}

	get(row, col){
		pos = row * this.c + col
		return (this.vector >> pos) & 1
	}

	set(row, col , val){
		pos = row * this.c + col
		mask = 1 << pos

		if (val === WHITE)
			this.vector |= mask
		else if (val == BLACK){
			mask = ~mask
			this.vector &= mask
		}
	}	

	toString(){
		result = ''
		copy = this.vector
		for (var i = 0; i < this.r; i++){
			for(var j = 0; j < this.c; j++){
				result += (copy & 1) + ' '
				copy = copy >> 1
			}
			result += '\n'
		}
		return result
	}

	equals(other){
		if (!(other instanceof BitVector2D))
			return false
		return this.vector == other.vector && this.c == other.c && this.r == other.r
	}
}

class Game{
	constructor(chints, rhints, rows, cols, board){
		this.won = false
		this.board = new BitVector2D(rows, cols, board)
		this.pboard = new BitVector2D(rows, cols, (1 << (rows * cols)) - 1)

		this.init(rhints, chints)
	}

	init(rhints, chints){

	}

	win(){
		return this.board.equals(this.pboard)
	}

	toString(){
		return this.board.toString()
	}
}

$(document).ready(start)