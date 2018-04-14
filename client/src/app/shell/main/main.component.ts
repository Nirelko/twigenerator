import { Component, EventEmitter, OnInit, ViewChild } from '@angular/core';
import { TwitService } from '../../services/twit.service';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';
import { trigger, state, style, transition, animate } from '@angular/animations';
import { TwitDropzoneComponent } from './twit-dropzone/twit-dropzone.component';

@Component({
  selector: 'main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  showDropZone: boolean;
  image: any;
  sentence: string;

  @ViewChild('twitDropzone') twitDropzone: TwitDropzoneComponent;

  constructor(private twitService: TwitService) {

  }

  ngOnInit(): void {
    this.showDropZone = true;
  }

  toggleLoading() {
    this.showDropZone = false;
    delete this.sentence;
    delete this.image;
  }

  showSentence({ image, sentence }) {
    this.sentence = sentence;
    this.image = image;
  }

  onUploadNew() {
    this.showDropZone = true;
    this.twitDropzone.reset();
    delete this.sentence;
    delete this.image;
  }

  regenerate() {
    delete this.sentence;
    this.twitService.generateTwit(this.image)
      .then(({ sentence }) => {
        this.sentence = sentence;
      })
  }

  postTweet() {
    setTimeout(() => window.open(`https://twitter.com/intent/tweet?screen_name=Post Tweet&text=${this.sentence}`, 'post tweet', 'height=250,width=600'), 0)
  }
}

export default MainComponent;
