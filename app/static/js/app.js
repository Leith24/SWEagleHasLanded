// app.js'use strict';

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
          //controller: 'meteoritesController'
      })
      .state('meteorite', {
          url: "/meteorite/{id}",
          templateUrl: "static/partials/meteorite.html",
          //controller: 'meteoritesIdController'
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
      });



  $locationProvider.html5Mode(true);
});

meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});