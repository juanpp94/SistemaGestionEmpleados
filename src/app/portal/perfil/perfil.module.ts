import { NgModule } from '@angular/core';

import { SharedModule } from '../../shared/shared.module';
import { PerfilComponent } from './perfil.component';
import { PerfilService } from './perfil.service';

@NgModule({
  declarations: [
    PerfilComponent
  ],
  imports: [
    SharedModule
  ],
  exports: [
  ],
  providers: [
    PerfilService
  ]
})
export class PerfilModule { }