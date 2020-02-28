import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";

import { PortalComponent } from "./portal.component";
import { TableroComponent } from "./tablero/tablero.component";
import { PerfilComponent } from "./perfil/perfil.component";

const routes: Routes = [
    {
        path: '',
        component: PortalComponent,
        children: [
            {
                path: '',
                redirectTo: 'tablero'
            },
            {
                path: 'tablero',
                component: TableroComponent,
                data: {title: 'Ubicutus - Tablero',   // se muestra en el tab del navegador
                urls: [
                    {title: 'Portal'},              // se muestran en el breadcrumb si tiene url se hace el link
                    {title: 'Tablero'},
                ]}
            },
            {
                path: 'perfil',
                component: PerfilComponent,
                data: {title: 'Ubicutus - Perfil',   // se muestra en el tab del navegador
                urls: [
                    {title: 'Portal', url: 'tablero'},              // se muestran en el breadcrumb si tiene url se hace el link
                    {title: 'Perfil'},
                ]}
            },
            {   path: '**', redirectTo: 'tablero'}, // error, ruta no encontrada
        ],
    }
];

@NgModule({
	imports: [RouterModule.forChild(routes)],
	exports: [RouterModule]
})
export class PortalRoutingModule { }