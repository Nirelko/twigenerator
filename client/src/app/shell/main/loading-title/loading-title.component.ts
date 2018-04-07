import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'loading-title',
  templateUrl: './loading-title.component.html',
  styleUrls: ['./loading-title.component.scss']
})
export class LoadingTitleComponent implements OnInit {
  isShown: boolean;

  ngOnInit(): void {
    setTimeout(() => this.isShown = true, 0);
  }
}

export default LoadingTitleComponent;
  