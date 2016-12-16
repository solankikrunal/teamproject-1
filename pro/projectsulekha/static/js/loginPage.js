sulekha.controller('loginCtrl', function($scope){
$scope.registerDiv = false;
$scope.loginDiv = true;
    $scope.register = function(){
    	$scope.registerDiv = true;
    	$scope.loginDiv = false;
    }

     $scope.login1 = function(){
     	
    	$scope.registerDiv = false;
    	$scope.loginDiv = true;
    }


 });
