import { environment } from '../../environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from "@angular/core";
import { Observable } from "rxjs/Rx";
import { Router } from '@angular/router';

import 'rxjs/Rx'; //NO QUITAR

export class SessionInfo {
    token: string;
    username: string;
    // fullname: string;
    // role: string;
}

@Injectable()
export class AuthService {

    constructor(
        private http: HttpClient,
        private router: Router
    ) { }

    login(username: string, password: string): Observable<any> {
        let headers = new HttpHeaders();
        headers = headers.set('Authorization', 'Basic ' + btoa(username + ':' + password))
                         .set('Content-Type', 'application/json');
        return this.http.post(environment.apiUrl.concat('/').concat(username).concat('/inicio-sesion'), null,
            {
                headers: headers,
                observe: 'response'
            });
    }

    logout(sessionExpired: boolean) {
        if (this.isLoggedIn()) {
            // ya no se llama a cerrar sesion 
            this.destroySession();
            this.router.navigate(['/login'], {queryParams: {expired: sessionExpired}});
                // this.logoutWithSesionActive Antes el codigo que tiene esta funcion
        } else {
            this.router.navigate(['/login'], {queryParams: {expired: sessionExpired}});
        }
    }

    logoutWithSesionActive(sessionExpired: boolean) {
        let endPoint = environment.apiUrl.concat('/').concat(localStorage.getItem('username')).concat('/cierre-sesion');
        let headers = new HttpHeaders({'X-Auth-Token': localStorage.getItem('token')});
        this.http.post(endPoint, null, {headers: headers}).subscribe(
            data => {
                this.destroySession();
                this.router.navigate(['/login'], {queryParams: {expired: sessionExpired}});
            },
            error => {
                this.destroySession();
                this.router.navigate(['/login'], {queryParams: {expired: sessionExpired}});
            }
        );
    }

    // activate(uuid: string, username: string, password: string): Observable<any> {
    //     let body = {
    //         uuid: uuid,
    //         password: password
    //     };

    //     return this.http.post(environment.apiUrl.concat('/users/').concat(username).concat('/activate'), body,
    //         {
    //             observe: 'response'
    //         });
    // }

    // findActivation(uuid: string): Observable<any> {
    //     return this.http.get(environment.apiUrl.concat('/user-activations/').concat(uuid));
    // }

    initSession(sessionInfo: SessionInfo) {
        localStorage.setItem("token", sessionInfo.token);
        localStorage.setItem("username", sessionInfo.username);
        // localStorage.setItem("fullname", sessionInfo.fullname);
        // localStorage.setItem("role", sessionInfo.role);
    }

    destroySession() {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        // localStorage.removeItem('fullname');
        // localStorage.removeItem('role');
    }

    getSessionInfo(): SessionInfo {
        return {
            token: localStorage.getItem('token'),
            username: localStorage.getItem('username'),
            // fullname: localStorage.getItem('fullname'),
            // role: localStorage.getItem('role')
        }
    }

    isLoggedIn(): boolean {
        if (localStorage.getItem('token')) {
            return true;
        } else {
            return false;
        }
    }

    getUsuarios(): Observable<any> {
        let headers = new HttpHeaders();
        headers = headers.set('Content-Type', 'application/json');
        return this.http.get(environment.apiUrl.concat('/usuarios'), 
            { headers: headers });
    }

    registrarUsuario(username, password, position) {
        let headers = new HttpHeaders();
        headers = headers.set('Content-Type', 'application/json');
        let body = {
            email: username,
            password: password,
            position: position
        }
        return this.http.post(environment.apiUrl.concat('/usuarios/'), body, 
            { headers: headers });
    }

}