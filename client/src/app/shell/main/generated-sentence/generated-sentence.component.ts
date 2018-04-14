import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'generated-sentence',
  templateUrl: './generated-sentence.component.html',
  styleUrls: ['./generated-sentence.component.scss']
})
export class GeneratedSentenceComponent {
  @Input() sentence: string;
  @Input() image: string;
  @Output() onUploadNew: EventEmitter<void>;
  @Output() onRegnerate: EventEmitter<void>;
  @Output() onPostTweet: EventEmitter<void>;

  constructor () {
    this.onUploadNew = new EventEmitter<void>();
    this.onRegnerate = new EventEmitter<void>();
    this.onPostTweet = new EventEmitter<void>();
  }

  uploadNew () {
    this.onUploadNew.emit();
  }

  regnerate () {
    this.onRegnerate.emit();
  }

  postTweet() {
    this.onPostTweet.emit();
  }
}

export default GeneratedSentenceComponent;
  