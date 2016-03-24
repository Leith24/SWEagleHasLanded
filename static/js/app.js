// app.js
var meteoriteApp = angular.module('meteoriteApp', ['ngRoute']);

meteoriteApp.config(function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
            templateUrl : 'static/partials/splash.html',
            controller: 'splashController'
        })
        .when('/locations', {
            templateUrl : 'static/partials/locations.html',
            controller  : 'locationsController'
        })
        .when('/meteorites', {
            templateUrl : 'static/partials/meteorites.html',
            controller  : 'meteoritesController'
        })
        .when('/classifications', {
            templateUrl : 'static/partials/classifications.html',
            controller  : 'classificationsController'
        })
        .when('/about', {
            templateUrl : 'static/partials/about.html',
            controller  : 'aboutController'
        });

    $locationProvider.html5Mode(true);
});

// create the controller and inject Angular's $scope

meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

meteoriteApp.controller('splashController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

meteoriteApp.controller('meteoritesController', function($scope) {
    $scope.message = 'Look! I am an meteorites controller.';
});


meteoriteApp.controller('classificationsController', function($scope) {
    $scope.message = 'classifications controller';
});

meteoriteApp.controller('locationsController', function($scope) {
    $scope.message = 'classifications controller';
});

meteoriteApp.controller('aboutController', function($scope) {
    $scope.message = 'Look! I am an about page.';
});
