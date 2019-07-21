const remote = require('electron').remote;
const $ = require('jquery');

function create_button(id, text) {
	let button = $("<button>");
	button.attr("id", id);
	button.attr("class", "btn");
	button.text(text);
	return button;
}

function init() {
	const container = $(".container:first");
	const bar = $("<div></div>");
	bar.attr("class", "row justify-content-end");
	bar.attr("style", "-webkit-app-region: drag");

	bar.append(create_button("min-btn", "-"));
	bar.append(create_button("max-btn", "o"));
	bar.append(create_button("close-btn", "x"));
	container.prepend(bar);

	$("#min-btn").click(function (e) {
		const window = remote.getCurrentWindow();
		window.minimize();
	});

	$("#max-btn").click(function (e) {
		const window = remote.getCurrentWindow();
		if (!window.isMaximized()) {
			window.maximize();
		} else {
			window.unmaximize();
		}
	});

	$("#close-btn").click(function (e) {
		const window = remote.getCurrentWindow();
		window.close();
	});
}

function getUrlVars() {
	const vars = [];
	let hash;
	const hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
	for (let i = 0; i < hashes.length; i++) {
		hash = hashes[i].split('=');
		vars.push(hash[0]);
		vars[hash[0]] = hash[1];
	}
	return vars;
}

$(window).on("load", init);