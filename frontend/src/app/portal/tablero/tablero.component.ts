import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { Message, MessageService } from '../../shared/message/message.service';

@Component({
  selector: 'app-tablero',
  templateUrl: './tablero.component.html',
  styleUrls: ['./tablero.component.css']
})
export class TableroComponent implements OnInit, OnDestroy {
  public loading: boolean;
  public message: Message;
  public messageSubscription: Subscription

  constructor(
    private messageService: MessageService,
  ) { }

  ngOnInit() {
    this.messageSubscription = this.messageService.message.subscribe(data => this.message = data);
  }

  ngOnDestroy() {
    this.messageSubscription.unsubscribe();
  }

  messageTest() {
    this.messageService.updateMessage({ class: 'alert-success', text: 'Prueba de Mensaje' })
  }

}
