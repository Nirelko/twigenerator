import { Component, OnInit, EventEmitter, Output, ViewChild } from '@angular/core';
import { DropzoneConfigInterface, DropzoneComponent } from 'ngx-dropzone-wrapper';
import { TwitService } from '../../../services/twit.service';

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

  constructor(private twitService: TwitService) {
    this.onImageSelected = new EventEmitter<void>();
    this.finishedCalcualting = new EventEmitter<object>();
  }

  ngOnInit(): void {
    const url = () => <string> `${this.twitService.baseRoute}/generator`;
    url.bind(this);

    this.dropzoneConfig = {
      url
    };
  }

  onFileAdded() {
    this.onImageSelected.emit();
  }

  onFinishedCalcualting([image, {sentence}, progress]) {
    this.finishedCalcualting.emit({image, sentence});
  }

  reset() {
    this.dropzone.directiveRef.reset();
  }
}

export default TwitDropzoneComponent;
