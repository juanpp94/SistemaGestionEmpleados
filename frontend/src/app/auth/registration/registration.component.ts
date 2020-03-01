import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-activation',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {

  public form: FormGroup;
  public message: string;

  public uuid: string;
  public username: string;

  public loading: boolean = false;

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

    this.form = this.formBuilder.group({
      username: [null, Validators.compose([Validators.required])],
      position: [null, Validators.compose([Validators.required])],
      password: [null, Validators.compose([Validators.required])],
      confirmation: [null, Validators.compose([Validators.required])]
    });
    
  }

  findActivation() {
    this.loading = true;

    // this.authService.findActivation(this.uuid)
    // .finally(() => this.loading = false)
    // .subscribe(
    //   response => {
    //     this.username = response.username;
    //   },
    //   error => {
    //     if (error.error.message) {
    //       this.message = error.error.message;
    //     } else {
    //       this.message = 'Your account cannot be activated at this time, please retry later';
    //     }
    //   }
    // );
  }

  onActivate() {
    if (this.form.controls['password'].value != this.form.controls['confirmation'].value) {
      this.message = 'Su confirmación no coincide';
      return;
    }

    this.loading = true;
    this.message = null;

    this.authService.registrarUsuario(this.form.value.username, this.form.value.password, this.form.value.position)
    .finally( () => this.loading = false)
    .subscribe( response => {
      console.log(response)
      this.router.navigate(['/login']);
    })
  //   this.authService.activate(this.uuid, this.username, this.form.controls['password'].value)
  //   .finally(() => this.loading = false)
  //   .subscribe(
  //     response => {
  //         this.router.navigate(['/login']);
  //     },
  //     error => {
  //       if (error.error.message) {
  //         this.message = error.error.message;
  //       } else {
  //         this.message = 'Your account could not be activated';
  //       }
  //     }
  //   );
  }

}