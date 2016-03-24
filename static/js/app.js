// app.js
var meteoriteApp = angular.module('meteoriteApp', ['ui.router']);

meteoriteApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/");
  //
  // Now set up the states
  $stateProvider
      .state('splash', {
          url: '/',
          templateUrl: "static/partials/splash.html"
      })
      .state('meteorites', {
        url: "/meteorites",
        templateUrl: "static/partials/meteorites.html",
        controller: 'meteoritesController'
      })
      .state('locations', {
        url: "/locations",
        templateUrl: "static/partials/locations.html",
        controller: 'locationsController'
      })
      .state('about', {
          url: "/about",
          templateUrl: 'static/partials/about.html',
          controller: 'aboutController'
      })
      .state('classifications', {
        url: "/classifications",
        templateUrl: "static/partials/classifications.html",
        controller: 'classificationsController'
      });
  //$locationProvider.html5Mode(true);
});
meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

// create the controller and inject Angular's $scope
//
//meteoriteApp.controller('mainController', function($scope) {
//    // create a message to display in our view
//    $scope.message = 'Everyone come and see how good I look!';
//});
//
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
