var sulekha=angular.module('prosulekha',['ui.router']);

sulekha.controller('homeCtrl', function($scope, $location){

    $scope.login = function(){
    	$location.path('/login');
    }

     $scope.post = function(){
    	$location.path('/post');
    }

 });

