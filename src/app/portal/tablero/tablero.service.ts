import { Injectable } from "@angular/core";
import { HttpClient, HttpParams } from "@angular/common/http";

import { environment } from "../../../environments/environment";
  
@Injectable()
export class TableroService {
    constructor (private http: HttpClient) { }


}