meteoriteApp.controller('mainController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

// create the controller and inject Angular's $scope
//
//meteoriteApp.controller('mainController', function($scope) {
//    // create a message to display in our view
//    $scope.message = 'Everyone come and see how good I look!';
//});
//
meteoriteApp.controller('splashController', function($scope) {
    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
});

meteoriteApp.controller('meteoritesController', function($scope) {
    $scope.message = 'Look! I am an meteorites controller.';
});


meteoriteApp.controller('classificationsController', function($scope) {
    $scope.message = 'classifications controller';
});

meteoriteApp.controller('locationsController', function($scope) {
    $scope.message = 'classifications controller';
});

meteoriteApp.controller('aboutController', function($scope) {
    $scope.message = 'Look! I am an about page.';
});
