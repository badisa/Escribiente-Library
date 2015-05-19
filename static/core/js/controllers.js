(function(){
var app = angular.module('libraryCtrls', []);

app.controller('BookCtrl', ['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http){
		$http.get('/books/' + $routeParams.bookId).success(function(data){
			$scope.book = data;
			$scope.book.amazonLink = 'http://amazon.com/dp/' + $scope.book.isbn_10;
		});
}]);

app.controller('BookListCtrl', ['$scope','$http',
	function($scope, $http){
		$http.get('/books/').success(function(data){
			$scope.books = data;
		});
}]);

})();