import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class TwitService {
  baseRoute: string = '/api/twit';

  constructor(private httpClient: HttpClient) {
  }

  generateTwit : any = file => {
    const formData = new FormData();
    formData.append('file', file, 'userfile');

    return this.httpClient.post(`${this.baseRoute}/generator`, formData).toPromise()
  }
}


