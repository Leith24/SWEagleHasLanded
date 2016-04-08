'use strict';

var meteoriteApp = angular.module('meteoriteApp', ['ui.router', 'angularUtils.directives.dirPagination']);

meteoriteApp.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
  //
  // For any unmatched url, redirect to /state1
    $urlRouterProvider.otherwise('/');
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
            resolve: {
                meteoritesObj: ['$http', function ($http){
                    return $http({
                        method: 'GET',
                        url: '/api/get_meteorites'
                    });
                }]
            },
            controller: 'meteoritesController'
        })
        .state('meteorite', {
            url: "/meteorite/:name",
            templateUrl: "../static/partials/meteorite.html",
            resolve: {
                meteoriteObj:['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method:'GET',
                        url:'/api/get_meteorite/' + $stateParams.name
                    });
                }]
            },
            controller: 'meteoriteController'
        })
        .state('countries', {
            url: "/countries",
            templateUrl: "static/partials/countries.html",
            resolve: {
                countriesObj:['$http', '$stateParams', function ($http){
                    return $http({
                        method:'GET',
                        url:'/api/get_country/'
                    });
                }]
            },
            controller: 'countriesController'
        })
        .state('country', {
            url: "/country/:id",
            templateUrl: "static/partials/country.html",
            resolve: {
                countryObj:['$http', '$stateParams', function ($http){
                    return $http({
                        method:'GET',
                        url:'/api/get_country/' + $stateParams.id
                    });
                }]
            },
            controller: 'countriesController'
        })
        .state('classifications', {
            url: "/classifications",
            templateUrl: "static/partials/classifications.html",
            resolve: {
                classificationsObj:['$http', '$stateParams', function ($http){
                    return $http({
                        method:'GET',
                        url:'/api/get_classifications'
                    });
                }]
            },
            controller: 'classificationsController'
        })
        .state('classification', {
            url: "/classification/:name",
            templateUrl: "../static/partials/classification.html",
            resolve: {
                classificationObj:['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method:'GET',
                        url:'/api/get_classification/' + $stateParams.name
                    });
                }]
            },
            controller: 'classificationController'
        })
        .state('about', {
            url: "/about",
            controller: "aboutController",
            templateUrl: "static/partials/about.html"
        });
    $locationProvider.html5Mode(true);


});

