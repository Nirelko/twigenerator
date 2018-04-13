import { Component, OnInit, EventEmitter, Output, ViewChild } from '@angular/core';
import { DropzoneConfigInterface, DropzoneComponent } from 'ngx-dropzone-wrapper';

@Component({
  selector: 'twit-dropzone',
  templateUrl: './twit-dropzone.component.html',
  styleUrls: ['./twit-dropzone.component.scss']
})
export class TwitDropzoneComponent implements OnInit {
  dropzoneConfig: DropzoneConfigInterface;
  @Output() onImageSelected: EventEmitter<void>;
  @Output() finishedCalcualting: EventEmitter<object>;

  @ViewChild(DropzoneComponent) dropzone: DropzoneComponent;

  constructor() {
    this.onImageSelected = new EventEmitter<void>();
    this.finishedCalcualting = new EventEmitter<object>();
  }

  ngOnInit(): void {
    this.dropzoneConfig = {
      url(): string {
        return '/api/generator';
      }
    };
  }

  onFileAdded() {
    this.onImageSelected.emit();
  }

  onFinishedCalcualting([{dataURL: image}, {sentence}, progress]) {
    this.finishedCalcualting.emit({image, sentence});
  }
}

export default TwitDropzoneComponent;
