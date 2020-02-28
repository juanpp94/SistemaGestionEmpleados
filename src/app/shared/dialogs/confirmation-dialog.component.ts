import { Component, Inject } from "@angular/core";
import { MAT_DIALOG_DATA, MatDialogRef } from "@angular/material";

@Component({
	selector: 'app-confirmation-dialog',
	templateUrl: 'confirmation-dialog.component.html',
})
export class ConfirmationDialogComponent {

	public title: string;
	public message: string;

	constructor(
		@Inject(MAT_DIALOG_DATA) public data: any,
		public dialogRef: MatDialogRef<ConfirmationDialogComponent>
	) {
		this.title = data.title;
		this.message = data.message;
	}

	onClick(option: string) {
		this.dialogRef.close(option);
	}

}