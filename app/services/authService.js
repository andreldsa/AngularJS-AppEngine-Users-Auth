var app = angular.module("app");

app.service("AuthService", function AuthService($http) {
    var service = this;

    var LOGIN_URI = "/api/auth/login";

    var LOGOUT_URI = "/api/auth/logout";

    var _user;

    Object.defineProperty(service, 'user', {
        get: function get() {
            return _user;
        },
        set: function set(newValue) {
            _user = newValue;
        }
    });

    service.login = function login() {
        window.location.replace(LOGIN_URI);
    };

    service.logout = function logout() {
        window.location.replace(LOGOUT_URI);
    };

    service.load = function load() {
        $http.get('/api').then(function loadUser(info) {
            service.user = info.data;
        });
    };

    service.load();
});