(function() {
	var app = angular.module("app", ["ngMaterial", "ui.router"]);

	app.config(function() {
	});

	app.controller("AppController", function AppController(AuthService) {
		var ctrl = this;

		Object.defineProperty(ctrl, 'user', {
			get: function() {
				return AuthService.user;
			}
		});

		ctrl.login = function login() {
			AuthService.login();
		};

		ctrl.logout = function logout() {
			AuthService.logout();
		};
	});
})();