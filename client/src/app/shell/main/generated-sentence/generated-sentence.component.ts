import { Component, Input } from '@angular/core';

@Component({
  selector: 'generated-sentence',
  templateUrl: './generated-sentence.component.html',
  styleUrls: ['./generated-sentence.component.scss']
})
export class GeneratedSentenceComponent {
  @Input() sentence: string;
  @Input() image: string;
}

export default GeneratedSentenceComponent;
  