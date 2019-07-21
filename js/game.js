const spawn = require('child_process').spawn;

BLACK = 0;
WHITE = 1;
MARKED = 2;
WRONG = 3;

const myPythonScript = "./python/game.py";
const pythonExecutable = "python";

const uint8arrayToString = function (data) {
	return String.fromCharCode.apply(null, data);
};

let game;

const stoi = function (str) {
	return parseInt(str, 10)
};

function start() {
	const params = getUrlVars();
	console.log(params);
	let r;
	const scriptExecution = spawn(pythonExecutable, [myPythonScript, params["file"], params["row"], params["col"]]);
	scriptExecution.stdout.on('data', (data) => {
		const str = uint8arrayToString(data);
		r = str.split('|');
		console.log(r)
	});
	scriptExecution.stderr.on('data', (data) => {
		// As said before, convert the Uint8Array to a readable string.
		console.log(uint8arrayToString(data));
	});
	scriptExecution.on('exit', (code) => {
		game = new Game(r[0], r[1], stoi(r[2]), stoi(r[3]), r[4])
	});
}

const make_guess = function (row, col, val) {
	game.make_guess(row, col, val)
};

const mark_board = function (row, col) {
	game.mark_board(row, col)
};


function createSpan() {
	let span = $("<span></span>");
	span.attr("style", "background-color: white;");
	return span
}

function createArray(length) {
	const arr = new Array(length || 0);
	let i = length;
	for (let l = 0; l < i; l++) {
		arr[l] = 1;
	}

	if (arguments.length > 1) {
		const args = Array.prototype.slice.call(arguments, 1);
		while (i--) arr[length - 1 - i] = createArray.apply(this, args);
	}

	return arr;
}

class Game {
	constructor(chints, rhints, rows, cols, board) {
		this.won = false;
		this.board = JSON.parse(board);
		this.pboard = createArray(rows, cols);
		this.rows = rows;
		this.cols = cols;

		this.chints = JSON.parse(chints);
		this.rhints = JSON.parse(rhints);
		this.addBoard()
	}

	addBoard() {
		let grid = $('#grid');

		let colhints = $("<tr></tr>");
		let padding = $("<td></td>");
		padding.append(createSpan());
		colhints.append(padding);

		for (let i = 0; i < this.cols; i++) {
			let col = $("<td></td>");
			let hint = createSpan();
			hint.html(hint.html() + this.chints[i].reverse().toString().replace(/,/g, "<br>"));
			col.append(hint);
			colhints.append(col)
		}
		grid.append(colhints);

		for (let i = 0; i < this.rows; i++) {
			let row = $("<tr></tr>");
			row.attr("class", 'row' + i);

			let row_hint = $("<td></td>");
			let hint = createSpan();
			hint.text(this.rhints[i].reverse().toString().replace(/,/g, " "));
			row_hint.append(hint);
			row.append(row_hint);

			for (let j = 0; j < this.cols; j++) {
				let col = $("<td></td>");
				let button = createSpan();
				button.attr("class", "btn-sml col square" + j);
				button.attr("id", "row" + i + "col" + j);
				button.attr("onclick", "make_guess(" + i + "," + j + "," + BLACK + ")");
				button.attr("oncontextmenu", "mark_board("+ i + "," + j + ")");
				col.append(button);
				row.append(col)
			}
			grid.append(row);
		}
	}

	mark_board(row, col) {
		if (this.pboard[row][col] === WRONG || this.pboard[row][col] === BLACK) return;

		let markedTile = $("#row" + row + "col" + col);

		if (this.pboard[row][col] === MARKED) {
			this.pboard[row][col] = WHITE;
			markedTile.attr("style", "background-color: white;")
		}
		else {
			this.pboard[row][col] = MARKED;
			markedTile.attr("style", "background-color: gray;")
		}
	}

	make_guess(row, col, val) {
		let guessTile;
		const actual = this.board[row][col];
		const players = this.pboard[row][col];

		if (players === MARKED) return;

		if (actual !== val) {
			guessTile = $("#row" + row + "col" + col);
			guessTile.attr("style", "background-color: red;");
			this.pboard[row][col] = WRONG;
			return;
		}

		this.pboard[row][col] = val;

		if (val === BLACK) {
			guessTile = $("#row" + row + "col" + col);
			guessTile.attr("style", "background-color: black;")
		}

		if (this.win()) {
			console.log("You Win");
			window.location.href = "./result.html";
			this.won = true
		}
	}

	win() {
		for (let i = 0; i < this.rows; i++) {
			for (let j = 0; j < this.cols; j++) {
				if (this.board[i][j] === BLACK && this.pboard[i][j] !== BLACK) {
					return false;
				}
			}
		}
		return true;
	}

	toString() {
		let result = '';
		for (let i = 0; i < this.rows; i++) {
			for (let j = 0; j < this.cols; j++) {
				result += (this.board[i][j] === 0 ? '||' : '  ') + ' '
			}
			result += '\n'
		}
		return result
	}
}

$(document).ready(start);