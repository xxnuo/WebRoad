function roles() {
	this.programmer = function(data) {
		if (data > 10000) {
			return data * 0.05;
		} else if (data >= 2000) {
			return 50;
		} else {
			return 0;
		}
	}
	this.manager = function(data) {
		if (data > 20000) {
			return data * 0.2;
		} else {
			return data * 0.1;
		}
	}
	this.salesman = function(data) {
		if (data > 100000) {
			return data * 0.3;
		} else if (data >= 50000) {
			return data * 0.2;
		} else {
			return data * 0.05;
		}
	}
}

function bonus() {
	this.benefit = 0;
}

bonus.prototype.setBenefit = function(data) {
	this.benefit = data;
}

bonus.__proto__ = new roles()

bonus.prototype.getBonus = function(role) {
	return role(this.benefit);
}

var bonusCount = new bonus();

var strategies = {
	"1": function() {
		return bonusCount.getBonus(bonus.programmer);
	},
	"2": function() {
		return bonusCount.getBonus(bonus.manager);
	},
	"3": function() {
		return bonusCount.getBonus(bonus.salesman);
	}
}

function countFun() {
	var benefit = document.getElementById("benefit").value;
	var role = document.getElementById("roles").value;
	bonusCount.setBenefit(benefit);
	document.getElementById("bonus").value = strategies[role]();
}
