import {Component, EventEmitter, OnInit} from '@angular/core';
import { TwitService } from '../../services/twit.service';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';

@Component({
  selector: 'main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  backgroundImage: any;

  ngOnInit(): void {
  }
}

export default  MainComponent;
