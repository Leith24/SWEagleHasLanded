meteoriteApp.controller('mainController', function($scope) {

});
//DATA TABLE SORTING WILL BE BROKEN ON INTEGERS NEED TO FIX IN DATABASE
meteoriteApp.controller('meteoritesController', function($scope, meteoritesObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.meteorites = meteoritesObj.data;
});

meteoriteApp.controller('meteoriteController', function($scope, $stateParams, meteoriteObj) {
    $scope.meteorite = meteoriteObj.data;
    //TODO: Get country from geolocation
    //$scope.country = geolocation bs
    $scope.message = $stateParams;

});
meteoriteApp.controller('classificationsController', function($scope, classificationsObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchClassifications   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.classifications = classificationsObj.data;
});

meteoriteApp.controller('classificationController', function($scope, $stateParams, classificationObj) {
    $scope.classification = classificationObj.data;
    //TODO: Get country from geolocation
    //$scope.country = geolocation b

});

meteoriteApp.controller('countriesController', function($scope, countriesObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.countries = countryObj.data;
});

meteoriteApp.controller('countryController', function($scope, $stateParams, countryObj) {
    $scope.meteorite = countryObj.data;
    //TODO: Get country from geolocation
    //$scope.country = geolocation bs
    $scope.message = $stateParams;

});