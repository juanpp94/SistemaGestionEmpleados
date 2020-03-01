import { Component } from '@angular/core';
import { PerfectScrollbarConfigInterface } from 'ngx-perfect-scrollbar';
import { AuthService } from '../../auth/auth.service';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: []
})
export class AppHeaderComponent {
  public config: PerfectScrollbarConfigInterface = {};
  public username: string;

  constructor(
    private authService: AuthService,
  ) {
    this.username = this.authService.getSessionInfo().username;
  }

  onLogout() {
    this.authService.logoutWithSesionActive(false);
  }
}
