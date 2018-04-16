import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import { BaseService } from './base-service';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class TwitterService extends BaseService {
    twitterClient: any;
    constructor (private httpClient: HttpClient) {
        super('twitter');
    }

    postTweet : any = (status, image) => {
        const formData = new FormData();
        formData.append('image', this.formatImageData(image));
        formData.append('imageName', image.name);
        formData.append('status', status);
    
        return this.httpClient.post(`${this.baseAddress}/tweet`, formData).toPromise();
    }

    formatImageData({dataURL}) {
        return dataURL.substring(dataURL.indexOf('base64,') + 'base64,'.length);
    }
}


