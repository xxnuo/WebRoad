//内置模块示例

const process = require('process');
const path = require('path');

console.log(process.version);
console.log(path.resolve('../'));
console.log('-----------');

//文件读取示例
const fs1 = require('fs');

fs1.readFile('README.md', 'utf8', (err, data) => {
	if(err) {
		console.log(err)
	}else{
		console.log('异步读取数据：'+ data)
		console.log('-----------');
	}
})


//Promise 封装fs.redaFile()
const fs2 = require('fs');

function fsRead(path) {
	return new Promise((resolve, reject) => {
		fs2.readFile(path,{ flag:'r', encoding:'utf-8'}, (err,data) => {
			if(err) {
				reject(err);
			} else {
				resolve(data);
			}
		})
	})
};

var promise1 = fsRead('file1.txt');
promise1.then(res1 => {
	console.log(res1);
	return fsRead('file2.txt');
}).then(res2 => {
	console.log(res2);
	return fsRead('file3.txt');
}).then(res3 => {
	console.log(res3);
	console.log('-----------');
});

