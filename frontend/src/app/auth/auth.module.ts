import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';

import { AuthService } from './auth.service';
import { RegistrationComponent } from './registration/registration.component';
import { LoginComponent } from './login/login.component';

@NgModule({
  declarations: [
    RegistrationComponent,
    LoginComponent
  ],
  entryComponents : [ ], 
  imports: [
    SharedModule
  ],
  exports: [
    LoginComponent
  ],
  providers: [
    AuthService
  ]
})
export class AuthModule { }