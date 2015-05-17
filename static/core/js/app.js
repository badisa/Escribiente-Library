(function(){
var app = angular.module('library', []);
app.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]')
});

app.controller('BookController', ['$http', function($http){
	var bookCtrl = this;
	bookCtrl.books = [];
	bookCtrl.book = {};

	bookCtrl.getBooks = function(){
		$http.get('/books/').success(function(data){
			bookCtrl.book = {};
			bookCtrl.books = data;
		});
	};
	bookCtrl.getBook = function(bookId){
		bookUrl = '/books/' + bookId;
		$http.get(bookUrl).success(function(data){
			bookCtrl.book = data;
			bookCtrl.books = [];
			bookCtrl.book.amazonLink = 'http://amazon.com/dp/' + bookCtrl.book.isbn_10;
		});
	};
}]);

app.directive('bookList', function(){
	return {
		restrict: 'E',
		templateUrl: '/partials/book-list.html'
	};
});

app.directive('bookInfo', function(){
	return {
		restrict: 'E',
		templateUrl: '/partials/book-info.html'
	};
});

})();