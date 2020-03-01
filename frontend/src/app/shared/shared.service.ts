import { Injectable } from "@angular/core";
import { DatePipe } from "@angular/common";

@Injectable()
export class SharedService {

	private states: Map<string, any> = new Map<string, any>();

	constructor(
		private datePipe: DatePipe,
	) { }

	loadState(key: string): any {
		return this.states.get(key);
	}

	saveState(key: string, state: any): void {
		this.states.set(key, state);
	}

}