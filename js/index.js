const {dialog} = require('electron').remote;

function start() {
	const create = $("#input");

	create.click(function () {
		dialog.showOpenDialog((filenames) => {
			if (filenames === undefined || filenames.length > 1) {
				console.log("Invalid selection")
			}
			console.log(filenames);
			window.location.href = "dimension.html?file=" + filenames[0];
		});
	});
}

$(window).on("load", start);