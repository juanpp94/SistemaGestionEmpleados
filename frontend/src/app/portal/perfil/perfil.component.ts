import { Component, OnInit } from '@angular/core';
import { Location } from "@angular/common";
import { Subscription } from 'rxjs';

import { Message, MessageService } from '../../shared/message/message.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {

	public message: Message;
	public messageSubscription: Subscription;

	public loading: boolean = false;

	public id: number = 0
	public username: string;
	public fullName: string;
	public position: number;
	public phone: string;
	public address: string;
  public status: string;
  public image: string;
	public created: Date;
	public updated: Date;

	constructor(
		private locationRef: Location,
		private messageService: MessageService,
	) { }

	ngOnInit() {
		this.messageSubscription = this.messageService.message.subscribe(data => this.message = data);
	}

	ngOnDestroy() {
		this.messageSubscription.unsubscribe();
	}

	navigateBack(): void {
		this.locationRef.back();
	}

}
