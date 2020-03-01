import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { AuthService } from "./auth.service";

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private authService: AuthService) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (request.url.endsWith('/login') || request.url.endsWith('/logout')) {
      return next.handle(request);
    }

    if (this.authService.isLoggedIn()) {
      request = request.clone({
        setHeaders: {
          'X-Auth-Token': this.authService.getSessionInfo().token
        }
      });
    }

    return next.handle(request).catch(error => this.handleError(error));
  }

  handleError(error: HttpErrorResponse): Observable<any> {
    if (error.status === 401 || error.status === 403) {
      this.authService.logout(true);
      return Observable.of(error.message);
    }

    return Observable.throw(error);
  }

}