const {app, BrowserWindow} = require('electron');

let win;

function createWindow() { 
   win  = new BrowserWindow({ frame: false, width: 1080, height: 720, backgroundColor: '#305426'});
   win.loadFile('./src/index.html')
}  

app.on('ready', createWindow);
