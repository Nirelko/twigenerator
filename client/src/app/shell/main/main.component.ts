import {Component, EventEmitter, OnInit} from '@angular/core';
import { TwitService } from '../../services/twit.service';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  showDropZone: boolean;
  image: string;
  sentence: string;

  ngOnInit(): void {
    this.showDropZone = true;
  }

  toggleLoading() {
    this.showDropZone = false;
    delete this.sentence;
    delete this.image;
  }

  showSentence({image, sentence}) {
    this.sentence = sentence;
    this.image = image;
  }
}

export default  MainComponent;
