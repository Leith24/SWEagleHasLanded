meteoriteApp.controller('mainController', function($scope) {

});
//DATA TABLE SORTING WILL BE BROKEN ON INTEGERS NEED TO FIX IN DATABASE
meteoriteApp.controller('meteoritesController', function($scope, meteoritesObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.meteorites = meteoritesObj.data.objects;
    console.log(meteoritesObj.data);
});

meteoriteApp.controller('meteoriteController', function($scope, $stateParams, meteoriteObj) {
    $scope.meteorite = meteoriteObj.data;
    console.log(meteoriteObj);
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
    console.log(classificationsObj.data);
    $scope.classifications = classificationsObj.data.objects;
});

meteoriteApp.controller('classificationController', function($scope, $stateParams, classificationObj) {
    $scope.classification = classificationObj.data;
    //TODO: Get country from geolocation
    //console.log(classificationObj.data);

});

meteoriteApp.controller('countriesController', function($scope, countriesObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.countries = countriesObj.data.objects;
    console.log(countriesObj.data);
});

meteoriteApp.controller('countryController', function($scope, $stateParams, countryObj) {
    //TODO: Get country from geolocation
    //$scope.country = geolocation bs
    $scope.country = countryObj.data;
    console.log($stateParams);

    $scope.message = $stateParams;

});
meteoriteApp.controller('aboutController', function ( $scope, unitTestData) {

    $scope.run_tests = function() {
        $scope.test_output = "Tests are running...";
        $scope.test_output = unitTestData.data;

    }
});