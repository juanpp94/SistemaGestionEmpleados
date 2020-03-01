import { NgModule } from '@angular/core';
import { PerfectScrollbarModule } from 'ngx-perfect-scrollbar';

import { AppHeaderComponent } from './header/header.component';
import { PortalComponent } from './portal.component';
import { PortalRoutingModule } from './portal-routing.module';
import { MenuItems } from './menu-items/menu-items';
import { SharedModule } from '../shared/shared.module';
import { AppBreadcrumbComponent } from './breadcrumb/breadcrumb.component';
import { TableroModule } from './tablero/tablero.module';
import { PerfilModule } from './perfil/perfil.module';

@NgModule({
  declarations: [
    AppHeaderComponent,
    AppBreadcrumbComponent,
    PortalComponent,
  ],
  entryComponents: [
  ],
  imports: [
    PortalRoutingModule,
    SharedModule,
    PerfectScrollbarModule,
    TableroModule,
    PerfilModule
  ],
  providers: [
    MenuItems
  ]
})
export class PortalModule { }