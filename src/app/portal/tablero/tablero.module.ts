import { NgModule } from '@angular/core';

import { TableroService } from './tablero.service';
import { TableroComponent } from './tablero.component';
import { SharedModule } from '../../shared/shared.module';

@NgModule({
  declarations: [
    TableroComponent
  ],
  imports: [
    SharedModule
  ],
  exports: [
  ],
  providers: [
    TableroService
  ]
})
export class TableroModule { }