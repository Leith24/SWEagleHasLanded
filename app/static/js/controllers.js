meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

meteoriteApp.controller('meteoritesController', function($scope, meteoritesObj) {
    $scope.message = 'meteoritesObj';
    console.log(meteoritesObj);
    $scope.meteorites = meteoritesObj.data;
});

meteoriteApp.controller('meteoriteController', function($scope, $stateParams, meteoriteObj) {
    $scope.meteorite = meteoriteObj;
    $scope.message = $stateParams;

});