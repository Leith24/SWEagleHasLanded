'use strict';

var meteoriteApp = angular.module('meteoriteApp', ['ui.router', 'angularUtils.directives.dirPagination']);

meteoriteApp.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
  //
  // For any unmatched url, redirect to /state1
    $urlRouterProvider
        .otherwise('/');
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
                        url: '/api/meteorites'
                    });
                }]
            },
            controller: 'meteoritesController',
            css: 'static/css/custom.css'
        })
        .state('meteorite', {
            url: "/meteorites/:id",
            templateUrl: "../static/partials/meteorite.html",
            resolve: {
                meteoriteObj:['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method:'GET',
                        url:'/api/meteorites/' + $stateParams.id
                    });
                }]
            },
            controller: 'meteoriteController'
        })
        .state('countries', {
            url: "/countries",
            templateUrl: "static/partials/countries.html",
            resolve: {
                countriesObj:['$http', function ($http){
                    return $http({
                        method:'GET',
                        url:'/api/countries'
                    });
                }]
            },
            controller: 'countriesController',
            css: 'static/css/custom.css'
        })
        .state('country', {
            url: "/countries/:id",
            templateUrl: "../static/partials/country.html",
            resolve: {
                countryObj:['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method:'GET',
                        url:'/api/countries/' + $stateParams.id
                    });
                }]
            },
            controller: 'countryController',
            css: '../static/css/custom.css'
        })
        .state('classifications', {
            url: "/classifications",
            templateUrl: "static/partials/classifications.html",
            resolve: {
                classificationsObj:['$http', function ($http){
                    return $http({
                        method:'GET',
                        url:'/api/classifications'
                    });
                }]
            },
            controller: 'classificationsController',
            css: 'static/css/custom.css'
        })
        .state('classification', {
            url: "/classifications/:id",
            templateUrl: "../static/partials/classification.html",
            resolve: {
                classificationObj:['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method:'GET',
                        url:'/api/classifications/' + $stateParams.id
                    });
                }]
            },
            controller: 'classificationController',
            css: '../static/css/custom.css'
        })
        .state('about', {
            url: "/about",
            templateUrl: "static/partials/about.html",
            resolve: {
                unitTestData: ['$http', function ($http){
                    return $http({
                        method: 'GET',
                        url: '/run_unit_tests'
                    });
                }]
            },
            controller: "aboutController"
        })
        .state('search', {
            url: "/search/:query",
            templateUrl: "../static/partials/search_results.html",
            resolve: {
                searchResult: ['$http', '$stateParams', function ($http, $stateParams){
                    return $http({
                        method: 'GET',
                        url: '/search/' + $stateParams.query
                    });
                }]
            },
            controller: "searchController"
        });
    $locationProvider.html5Mode(true);


});


