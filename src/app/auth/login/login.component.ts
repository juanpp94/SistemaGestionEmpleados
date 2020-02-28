import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: []
})
export class LoginComponent implements OnInit {

  public form: FormGroup;
  public message: string;

  public loggingIn: boolean = false;

  constructor(
    private activatedRoute: ActivatedRoute,
    private formBuilder: FormBuilder, 
    private router: Router, 
    private authService: AuthService
  ) { }

  ngOnInit() {
    // if (this.authService.isLoggedIn()) {
    //   this.router.navigate(['/portal']);
    // }
    
    // this.activatedRoute.queryParams.subscribe(params => {
    //   if (params['expired'] == 'true') {
    //     this.message = 'Su sesión ha expirado';
    //   }
    // });
    
    this.form = this.formBuilder.group({
      username: [null, Validators.compose([Validators.required])],
      password: [null, Validators.compose([Validators.required])]
    });
  }

  onLogin() {
    this.loggingIn = true;
    this.message = null;
    this.router.navigate(['/portal']);
    // this.authService.login(this.form.controls['username'].value, this.form.controls['password'].value)
    // .finally(() => this.loggingIn = false)
    // .subscribe(
    //   response => {
    //     let token = response.headers.get('X-Auth-Token');

    //     if (token) {
    //       this.authService.initSession({
    //         token: token,
    //         username: this.form.controls['username'].value.toString().toLowerCase(),
    //         // fullname: response.body['fullname'],
    //         // role: response.body['role']
    //       });
  
    //       this.router.navigate(['/portal']);
    //     } else {

    //     }
    //   },
    //   error => {
    //     if (error.error.message) {
    //       this.message = error.error.message;
    //     } else {
    //       this.message = "Error al Iniciar Sesión ";
    //     }
    //   }
    // );
  }

}