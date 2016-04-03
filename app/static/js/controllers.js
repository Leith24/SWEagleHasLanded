

meteoriteApp.controller('meteoritesController', function($scope) {

    $scope.message = 'Everyone come and see how good I look!';

    //Make call to API and get_meteorites


});

meteoriteApp.controller('meteoriteIdController', function($scope, $state, $stateParams) {
    // create a message to display in our view
    $scope.message = 'meteroite ID controller';

    $scope.params = $stateParams;
    console.log($scope.params);
    //Make call to API and get_meteorite/{id}


});