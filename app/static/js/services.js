'use strict';
angular.module('services',[])
    .factory('unit_test_service', function($http) {
        return {
            run_unit_tests : function() {
                return $http.get('/run_unit_tests').then(function(result){
                    return result.data;
                });
            }
        }
    });