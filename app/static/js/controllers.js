meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});
//DATA TABLE SORTING WILL BE BROKEN ON INTEGERS NEED TO FIX IN DATABASE
meteoriteApp.controller('meteoritesController', function($scope, meteoritesObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term

    $scope.meteorites = meteoritesObj.data;
});

meteoriteApp.controller('meteoriteController', function($scope, $stateParams, meteoriteObj) {
    $scope.meteorite = meteoriteObj.data;
    //TODO: Get country from geolocation
    //$scope.country = geolocation bs
    $scope.message = $stateParams;

});