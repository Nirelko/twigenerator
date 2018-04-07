import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';

@Component({
  selector: 'twit-dropzone',
  templateUrl: './twit-dropzone.component.html',
  styleUrls: ['./twit-dropzone.component.scss']
})
export class TwitDropzoneComponent implements OnInit {
  dropzoneConfig: DropzoneConfigInterface;
  @Output() onImageSelected: EventEmitter<void>;

  constructor() {
    this.onImageSelected = new EventEmitter<void>();
  }

  ngOnInit(): void {
    this.dropzoneConfig = {
      url(): string {
        console.log(arguments);

        return '/api/generator';
      }
    };
  }

  onFileAdded() {
    this.onImageSelected.emit();
  }
}

export default TwitDropzoneComponent;
