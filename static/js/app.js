// app.js
var meteoriteApp = angular.module('meteoriteApp', ['ui.router']);

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
          //controller: 'meteoritesController'
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
      .state('H6', {
          url: "/H6",
          templateUrl: "static/partials/H6.html"
      })
      .state('L5', {
          url: "/L5",
          templateUrl: "static/partials/L5.html"
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
          templateUrl: 'static/partials/about.html',
          controller: 'aboutController'
      });


  $locationProvider.html5Mode(true);
});

meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});
