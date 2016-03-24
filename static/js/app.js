// app.js
var meteoriteApp = angular.module('meteoriteApp', ['ui.router', 'controllers']);

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
      .state('locations', {
          url: "/locations",
          templateUrl: "static/partials/locations.html",
          controller: 'locationsController'
      })
      .state('classifications', {
          url: "/classifications",
          templateUrl: "static/partials/classifications.html",
          controller: 'classificationsController'
      })
      .state('about', {
          url: "/about",
          templateUrl: 'static/partials/about.html',
          controller: 'aboutController'
      });

  $locationProvider.html5Mode(true);
});
