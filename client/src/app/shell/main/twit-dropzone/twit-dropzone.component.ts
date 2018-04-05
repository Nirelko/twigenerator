import { Component, OnInit } from '@angular/core';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';

@Component({
  selector: 'twit-dropzone',
  templateUrl: './twit-dropzone.component.html',
  styleUrls: ['./twit-dropzone.component.scss']
})
export class TwitDropzoneComponent implements OnInit {
  dropzoneConfig: DropzoneConfigInterface;

  ngOnInit(): void {
    this.dropzoneConfig = {
      url() : string {
        console.log(arguments);

        return '';
      }
    };
  }
}

export default TwitDropzoneComponent;
