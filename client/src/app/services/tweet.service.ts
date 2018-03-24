import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class TweetService {
  baseRoute: string = '/api/tweet';

  constructor(private httpClient: HttpClient) {
  }

  generateTweet(image) {
    return this.httpClient.post(`${this.baseRoute}`, { image }).toPromise();
  }
}


