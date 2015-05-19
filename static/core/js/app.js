(function(){
var app = angular.module('Library', [
	'ngRoute',
	'libraryCtrls']);
app.config(['$routeProvider', '$interpolateProvider',
  function($routeProvider, $interpolateProvider) {
    $routeProvider.
		when('/library/', {
			templateUrl: '/partials/home.html',
		}).
		when('/library/books/', {
			templateUrl: '/partials/book-list.html',
			controller: 'BookListCtrl'
		}).
		when('/library/books/:bookId/', {
			templateUrl: '/partials/book-info.html',
			controller: 'BookCtrl'
		}).
		otherwise({
			redirectTo: '/library/'
		});
}]);

})();