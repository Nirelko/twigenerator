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
  isImageSelected: boolean;

  ngOnInit(): void {
  }

  toggleLoading() {
    this.isImageSelected = true;
  }
}

export default  MainComponent;
