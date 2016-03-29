// app.js
var meteoriteApp = angular.module('meteoriteApp', ['ui.router', 'datatables']);

meteoriteApp.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
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
      .state('countries', {
          url: "/countries",
          templateUrl: "static/partials/countries.html",
          //controller: 'countriesController'
      })
      .state('classifications', {
          url: "/classifications",
          templateUrl: "static/partials/classifications.html",
          //controller: 'classificationsController'
      })
      .state('alby', {
          url: "/alby",
          templateUrl: "static/partials/alby.html"
      })
      .state('bunburra_rockhole', {
          url: "/bunburra_rockhole",
          templateUrl: "static/partials/bunburra_rockhole.html"
      })
      .state('EUC', {
          url: "/EUC",
          templateUrl: "static/partials/EUC.html"
      })
      .state('L6', {
          url: "/L6",
          templateUrl: "static/partials/L6.html"
      })
      .state('LL6', {
          url: "/LL6",
          templateUrl: "static/partials/LL6.html"
      })
      .state('thika', {
          url: "/thika",
          templateUrl: "static/partials/thika.html"
      })
      .state('australia', {
          url: "/australia",
          templateUrl: "static/partials/australia.html"
      })
      .state('france', {
          url: "/france",
          templateUrl: "static/partials/france.html"
      })
      .state('kenya', {
          url: "/kenya",
          templateUrl: "static/partials/kenya.html"
      })
      .state('ensisheim', {
          url: "/ensisheim",
          templateUrl: "static/partials/ensisheim.html"
      })
      .state('about', {
          url: "/about",
          templateUrl: 'static/partials/about.html'
      })
      .state('2007', {
          url: "/2007",
          templateUrl: 'static/partials/2007.html'
      })
      .state('1492', {
          url: "/1492",
          templateUrl: 'static/partials/1492.html'
      })
      .state('2011', {
          url: "/2011",
          templateUrl: 'static/partials/2011.html'
      });


  $locationProvider.html5Mode(true);
});

meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

meteoriteApp.controller('meteoritesController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});
