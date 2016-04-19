//Need to declare a mainController for Angular but it doesn't do anything
meteoriteApp.controller('mainController', function($scope) {

});

meteoriteApp.controller('meteoritesController', function($scope, meteoritesObj) {
     //Parameters for pagination
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.meteorites = meteoritesObj.data.objects;

});

meteoriteApp.controller('meteoriteController', function($scope, $sce, $stateParams, meteoriteObj) {
    $scope.meteorite = meteoriteObj.data;

    $scope.message = $stateParams;
    //Google Maps embedding
    $scope.urlString = "https://www.google.com/maps/embed/v1/place?key=AIzaSyBMRg5inrD7lBnA8EivUn1k-TuOlBhdNMw"
                                    + "&q=" + ($scope.meteorite).geolocation
                                    + "&zoom=6";
    $scope.mapURL = $sce.trustAsResourceUrl($scope.urlString);
});

meteoriteApp.controller('classificationsController', function($scope, classificationsObj) {
    //Parameters for pagination
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchClassifications   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.classifications = classificationsObj.data.objects;
});

meteoriteApp.controller('classificationController', function($scope, $stateParams, classificationObj) {
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    $scope.classification = classificationObj.data;
    $scope.meteorites = classificationObj.data.meteorites;
    console.log(classificationObj.data.meteorites);


});

meteoriteApp.controller('countriesController', function($scope, countriesObj) {
    //Parameters for pagination
    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;

    //Generate meteorite ID for 'Last Found' so we can link to individual meteorites
    var numResults = countriesObj.data.num_results;
    for(var i=0; i < numResults; i++){
        if(countriesObj.data.objects[i].meteorites.length != 0){
            countriesObj.data.objects[i].meteoriteID = countriesObj.data.objects[i].meteorites[0].id;
        }
    }
    $scope.countries = countriesObj.data.objects;
});

meteoriteApp.controller('countryController', function($scope, $sce, $stateParams, countryObj) {
    //Table of meteorites that have landed in the country

    $scope.country = countryObj.data;
    $scope.meteorites = countryObj.data.meteorites;
    $scope.cname = capFirstLetter(countryObj.data.name);

    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchMeteorites   = '';     // set the default search/filter term
    $scope.currentPage = 1;
    $scope.pageSize = 15;





    //Google Maps embedding
    $scope.urlString = "https://www.google.com/maps/embed/v1/place?key=AIzaSyBMRg5inrD7lBnA8EivUn1k-TuOlBhdNMw"
                                    + "&q=" + ($scope.country).centroid
                                    + "&zoom=6";
    $scope.mapURL = $sce.trustAsResourceUrl($scope.urlString);

});
meteoriteApp.controller('aboutController', function ( $scope, unitTestData) {

    $scope.run_tests = function() {
        $scope.test_output = "Tests are running...";
        $scope.test_output = unitTestData.data;

    }
});

function capFirstLetter(string){
     return string.charAt(0).toUpperCase() + string.slice(1);
}