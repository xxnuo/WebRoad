var numberClick = function(value) {
	var val = document.getElementById("output").value;
	// 0
	if (value == "0" && val == "0")
		return;
	// 0 -> value
	if (val == "0") {
		document.getElementById("output").value = value;
	} else {
		document.getElementById("output").value = val + value;
	}
}

var operatorClick = function(value) {
	var val = document.getElementById("output").value;
	//ignore double click
	if (val[val.length - 1] == " ")
		return;
	document.getElementById("output").value = val + " " + value + " ";
}

var cleanClick = function() {
	document.getElementById("output").value = "0";
}

var equalClick = function() {
	num = document.getElementById("output").value.split(" ");
	// * /
	for (var index = 0; index < num.length; index++) {
		if (num[index] == "*" || num[index] == "/") {
			if (num[index + 1] == "") {
				num[index + 1] = 1;
			}
			if (num[index] == "*") {
				var index_num = Number(index);
				var firstNum = Number(num[index_num - 1]);
				var secondNum = Number(num[index_num + 1]);
				var result = firstNum * secondNum;
				num.splice(index_num - 1, 3, result);
			} else if (num[index] == "/") {
				var index_num = Number(index);
				var firstNum = Number(num[index_num - 1]);
				var secondNum = Number(num[index_num + 1]);
				var result = firstNum / secondNum;
				num.splice(index_num - 1, 3, result);
			}
			index--;
		}
	}
	for (var index = 0; index < num.length; index++) {
		if (num[index] == "+" || num[index] == "-") {
			if (num[index + 1] == "") {
				num[index + 1] = 1;
			}
			if (num[index] == "+") {
				var index_num = Number(index);
				var firstNum = Number(num[index_num - 1]);
				var secondNum = Number(num[index_num + 1]);
				var result = firstNum + secondNum;
				num.splice(index_num - 1, 3, result);
			} else if (num[index] == "-") {
				var index_num = Number(index);
				var firstNum = Number(num[index_num - 1]);
				var secondNum = Number(num[index_num + 1]);
				var result = firstNum - secondNum;
				num.splice(index_num - 1, 3, result);
			}
			index--;
		}
	}
	document.getElementById("output").value = num[0];

}

var fn = function() {
	var val = document.getElementById("output").value;
	var reg = new RegExp("^\\d+([+*/-]\\d+)+$");
	var isNumber = new RegExp("^[0-9]*$");
	if (!isNumber.test(val)) {
		if (!reg.test(val)) {
			alert("error");
			cleanClick();
		}
	} else {
		//get operator
		var reg1 = /[+*/-]/g;
		var str = (val.match(reg1));
		if (str == null)
			return;
		//get number
		var reg2 = /\d+/g;
		var str2 = (val.match(reg2));
		var str1 = [];
		var res = "";
		//add space
		for (var i = 0; i < str.length; i++) {
			str1[i] = " " + str[i] + " ";
			res += str2[i] + str1[i];
		}
		var res1 = res + str2[str2.length - 1];
		document.getElementById("output").value = res1;
	}
}
