var request = require('request');

request.get('https://cnodejs.org/api/v1/topics?page=1&limit=10', (err,response,body) => {
	console.log(body);
})