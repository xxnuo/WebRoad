const http = require("http");

http.createServer(function(request, response) {
	response.write("Helloq");
	response.end();
}).listen(8080);

console.log("http://localhost:8080/");