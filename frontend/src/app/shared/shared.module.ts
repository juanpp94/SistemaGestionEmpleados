import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FlexModule } from '@angular/flex-layout';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { MaterialModule } from './material/material.module';
import { SpinnerComponent } from './spinner/spinner.component';
import { MenuItems } from './menu-items/menu-items';
import { ConfirmationDialogComponent } from './dialogs/confirmation-dialog.component';
import { SharedService } from './shared.service';
import { CompletedDialogComponent } from './dialogs/completed-dialog.component';

@NgModule({
  declarations: [
    SpinnerComponent,
    ConfirmationDialogComponent,
    CompletedDialogComponent,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    FormsModule,
    FlexModule,
    ReactiveFormsModule,
  ],
  exports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialModule,
    FlexModule,
    SpinnerComponent,
    CompletedDialogComponent,
    RouterModule,
  ],
  providers: [MenuItems, SharedService ]
})
export class SharedModule {}
