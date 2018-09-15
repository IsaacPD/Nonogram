const {app, BrowserWindow} = require('electron') 
const url = require('url') 
const path = require('path')  

let win

function createWindow() { 
   win  = new BrowserWindow({ frame: false, width: 640, height: 480, backgroundColor: '#305426'})  
   win.loadFile('./src/index.html')
}  

app.on('ready', createWindow) 
