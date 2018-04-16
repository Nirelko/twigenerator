import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import { BaseService } from './base-service';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class TwitService extends BaseService {
  constructor(private httpClient: HttpClient) {
    super('twit')
  }

  generateTwit : any = image => {
    const formData = new FormData();
    formData.append('file', image, 'userfile');

    return this.httpClient.post(`${this.baseAddress}/generator`, formData).toPromise()
  }
}


