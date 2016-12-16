
sulekha.config(function($stateProvider,$urlRouterProvider){
		$urlRouterProvider.otherwise('/index');
		$stateProvider
			.state('index', {			//By default Home page
				url:'/index',
				templateUrl:'index.html'
				
			})

			.state('login', {		//Navigate to login page
				url:'/login',
				templateUrl: 'loginPage.html',
				controller: 'loginCtrl'
			})

			.state('post', {		//Navigate to login page
				url:'/post',
				templateUrl: 'post.html'
			})
			
		});
