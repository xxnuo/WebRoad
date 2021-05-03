var fs = require('fs');
try {
	var data = fs.readFileSync('./s2-8.txt', 'utf8');
	console.log(data);
	var adjData = data.replace(/[A|a]pple/g, 'orange');
	fs.writeFileSync('./s2-8.motified.txt', adjData);
} catch (err) {
	console.log(err);
}

//异步版本

var fs = require('fs');
fs.readFile('./s2-8.txt', 'utf8', function(err, data) {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
		var adjData = data.replace(/apple/g, 'sync-orange');
		fs.writeFile('./s2-8.sync.motified.txt', adjData, function(err) {
			if (err) console.error(err);
		});
	}
});
