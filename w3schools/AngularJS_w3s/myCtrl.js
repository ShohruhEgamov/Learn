var app = angular.module('myApp', []);

// app.controller("myCtrl", function ($scope) {
// 	$scope.firstName = "Shohruh";
// 	$scope.lastName = "EGAMOV";
// });

// app.controller("myCtrl1", function ($scope) {
// 	$scope.firstName = "Farrux";
// 	$scope.lastName = "EGAMOV";
// });

// --------------------------------------------------------------------------------------------
// app.directive("shohTestDirective", function () {
// 	return {
// 		template: "<p>Made by a directive!</p>"
// 	};
// });

// app.directive("hoverData", function () {
// 	return {
// 		template: "<p>29.10.2024</p>"
// 	}
// })

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl2', function ($scope) {
// 	$scope.name = "Shohruh EGAMOV";
// });

// app.controller('myCtrl2', function ($scope) {
// 	$scope.name = "Shohruh EGAMOV";
// });


// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.firstname = 'Shohruh';
// 	$scope.lastname = 'EGAMOV';
// 	$scope.ismUzgarishi = function () {
// 		$scope.firstname = 'Farrux';
// 	}
// })



// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.firstName = '';
// 	$scope.lastName = '';
// 	$scope.fullName = function () {
// 		if ($scope.firstName.length < 5) {
// 			return 'Ismingiz qabul qilinmadi'
// 		} else { return `Bu yerda to'liq ism ${$scope.firstName} ${$scope.lastName} ism uzunligi ${$scope.firstName.length} familya uzinligi ${$scope.lastName.length}`; }

// 	};
// });

// angular.module('myApp', []).controller('namesCtrl', function ($scope) {
// 	$scope.names = [
// 		{ name: 'Shohruh', country: 'Kanada' },
// 		{ name: 'Farrux', country: 'Korea' },
// 		{ name: 'Diyorbek', country: 'Rassiya' }
// 	];
// });

// --------------------------------------------------------------------------------------------

// angular.module('myApp', []).controller('myCtrl', function ($scope) {
// 	$scope.carname = 'Lasetti';
// 	$scope.nomUzgarishi = function () {
// 		$scope.carname = 'Chevralett'
// 	}
// });


// angular.module('myApp', []).controller('myCtrl', function ($scope) {
// 	$scope.names = ['Shohruh', 'Diyorbek', 'Bekmirza', 'Farrux'];
// });

// app.run(function ($rootScope) {
// 	$rootScope.color = 'yellow';
// });
// app.controller('myCtrl', function ($scope) {
// 	$scope.color = "black";
// });


// --------------------------------------------------------------------------------------------

// angular.module('myApp', []).controller('personCtrl', function ($scope) {
// 	$scope.firstName = 'shohruh';
// 	$scope.lastName = 'egamov';
// });


// Capitalize filtrini yarating
// app.filter('capitalize', function () {
// 	return function (input) {
// 		if (!input) return '';
// 		return input.charAt(0).toUpperCase() + input.slice(1).toLowerCase();
// 	};
// });

// angular.module('myApp', []).controller('namesCtrl', function ($scope) {
// 	$scope.names = [
// 		{ name: 'Jani', country: 'Norway' },
// 		{ name: 'Carl', country: 'Sweden' },
// 		{ name: 'Margareth', country: 'England' },
// 		{ name: 'Hege', country: 'Norway' },
// 		{ name: 'Joe', country: 'Denmark' },
// 		{ name: 'Gustav', country: 'Sweden' },
// 		{ name: 'Birgit', country: 'Denmark' },
// 		{ name: 'Mary', country: 'England' },
// 		{ name: 'Kai', country: 'Norway' }
// 	];
// });

// app.controller('costCtrl', function ($scope) {
// 	$scope.price = 58;
// });


// angular.module('myApp', []).controller('namesCtrl', function ($scope) {
// 	$scope.names = [
// 		'Jani',
// 		'Carl',
// 		'Margareth',
// 		'Hege',
// 		'Joe',
// 		'Gustav',
// 		'Birgit',
// 		'Mary',
// 		'Kai'
// 	];
// });


// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $timeout) {
// 	$scope.myHeader = "Hello World!";
// 	$timeout(function () {
// 		$scope.myHeader = "How are you today?";
// 	}, 2000);
// });


// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $interval) {
// 	$scope.theTime = new Date().toLocaleTimeString();
// 	$interval(function () {
// 		$scope.theTime = new Date().toLocaleTimeString();
// 	}, 1000);
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $http) {
// 	$http.get("welcome.htm")
// 		.then(function (response) {
// 			$scope.myWelcome = response.data;
// 		});
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $http) {
// 	// Birinchi fayl - welcome.txt
// 	$http({
// 		method: "GET",
// 		url: "welcome.txt"
// 	}).then(function mySuccess(response) {
// 		$scope.myWelcome = response.data;
// 	}, function myError(response) {
// 		$scope.myWelcome = response.statusText;
// 	});

// 	// Ikkinchi fayl - goodbye.txt
// 	$http({
// 		method: "GET",
// 		url: "goodbye.txt"
// 	}).then(function mySuccess(response) {
// 		$scope.myGoodBye = response.data;
// 	}, function myError(response) {
// 		$scope.myGoodBye = response.statusText;
// 	});
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $http) {
// 	$http.get("welcome.txt")
// 		.then(function (response) {
// 			$scope.content = response.data;
// 			$scope.statuscode = response.status;
// 			$scope.statustext = response.statusText;
// 		})
// 		.catch(function (error) {
// 			$scope.content = "Xato yuz berdi.";
// 			$scope.statuscode = error.status || "No status";
// 			$scope.statustext = error.statusText || "Xato matni mavjud emas";
// 		});
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope, $http) {
// 	$http.get('wecome.txt')
// 		.then(function (res) {
// 			$scope.content = res.data;
// 		})
// 		.catch(function (res) {
// 			$scope.content = 'Something went wrong';
// 		})
// });


// --------------------------------------------------------------------------------------------
// app.controller('customersCtrl', function ($scope, $http) {
// 	$http.get("customer.php")
// 		.then(function (response) {
// 			$scope.myData = response.data.records;
// 		})
// 		.catch(function (res) {
// 			$scope.myData = 'Bu yerda xatolik bor'
// 		})
// });

// --------------------------------------------------------------------------------------------
// app.controller('customersCtrl', function ($scope, $http) {
// 	$http.get("customer.php")
// 		.then(function (res) { $scope.names = res.data.records; });
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.names = ["Emil", "Tobias", "Linus"];
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.names = ["Emil", "Tobias", "Linus"];
// 	$scope.cars = [
// 		{ model: "Ford Mustang", color: "red" },
// 		{ model: "Fiat 500", color: "white" },
// 		{ model: "Volvo XC90", color: "black" }
// 	];
// });

// app.controller('myCtrl', function ($scope) {
// 	$scope.cars = [
// 		{ model: "Brabus", color: "red" },
// 		{ model: "Lasetti", color: "white" },
// 		{ model: "BMW", color: "black" }
// 	];
// });

// app.controller('myCtrl', function ($scope) {
// 	$scope.cars = [
// 		{ model: "Ford Mustang", color: "red" },
// 		{ model: "Fiat 500", color: "white" },
// 		{ model: "Volvo XC90", color: "black" }];
// });


// app.controller('myCtrl', function ($scope) {
// 	$scope.cars = {
// 		car01: "Ford",
// 		car02: "Fiat",
// 		car03: "Volvo"
// 	}
// });


// app.controller('myCtrl', function ($scope) {
// 	$scope.cars = {
// 		car01: {
// 			brand: "Ford",
// 			model: "Mustang",
// 			color: "red"
// 		},
// 		car02: {
// 			brand: "Fiat",
// 			model: "500",
// 			color: "white"
// 		},
// 		car03: {
// 			brand: "Volvo",
// 			model: "XC90",
// 			color: "black"
// 		}
// 	}
// });

// --------------------------------------------------------------------------------------------
// app.controller('customersCtrl', function ($scope, $http) {
// 	$http.get("customer.php")
// 		.then(function (response) {
// 			$scope.names = response.data.royhatlar;
// 		});
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.count = ''
// });


// app.controller('myCtrl', function ($scope) {
// 	// Fibonachchi ketma-ketligini hosil qilish uchun funksiya
// 	$scope.generateFibonacci = function () {
// 		const n = $scope.numTerms || 10; // Foydalanuvchi kiritgan sonni olish yoki default 10
// 		let fibSequence = [0, 1];

// 		for (let i = 2; i < n; i++) {
// 			fibSequence[i] = fibSequence[i - 1] + fibSequence[i - 2];
// 		}

// 		$scope.fibonacciSequence = fibSequence;
// 	};

// 	// Boshlang‘ich qiymat
// 	$scope.numTerms = 10;
// 	$scope.fibonacciSequence = [];
// });


// app.controller('myCtrl', function ($scope) {
// 	// Fibonachchi ketma-ketligi uchun boshlang‘ich qiymatlar
// 	$scope.fibonacciSequence = [0, 1]; // Dastlabki ikki son
// 	$scope.index = 2; // Keyingi sonning indeksi

// 	// Fibonachchi ketma-ketligida navbatdagi sonni hosil qilish
// 	$scope.generateNext = function () {
// 		// Keyingi sonni hisoblash: oxirgi ikki sondan
// 		let nextNumber = $scope.fibonacciSequence[$scope.index - 1] + $scope.fibonacciSequence[$scope.index - 2];

// 		// Ketma-ketlikka qo'shish
// 		$scope.fibonacciSequence.push(nextNumber);

// 		// Indeksni yangilash
// 		$scope.index++;
// 	};
// });

// --------------------------------------------------------------------------------------------
// app.controller('myCtrl', function ($scope) {
// 	$scope.showMe = false;
// 	$scope.myFunc = function () {
// 		$scope.showMe = !$scope.showMe;
// 	}
// });

