let $ = require('jquery')  // jQuery now loaded and assigned to $
let count = 0

const {dialog} = require('electron').remote;

document.queryselector('#start').addEventListener('click', function (event) {
    dialog.showOpenDialog({
        properties: ['openFile', 'singleSelection']
    }, function (files) {
        if (files !== undefined) {
            // handle files

        }
    })
})