import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MatToolbarModule, MatButtonModule } from '@angular/material';
import { FlexLayoutModule } from '@angular/flex-layout';
import {HttpClientModule} from '@angular/common/http';
import { TypingModule } from 'ng-typing';
import 'hammerjs';
import { DropzoneModule } from 'ngx-dropzone-wrapper';
import { DROPZONE_CONFIG } from 'ngx-dropzone-wrapper';
import { DropzoneConfigInterface } from 'ngx-dropzone-wrapper';

import { ShellComponent } from './shell/shell.component';
import { HeaderComponent } from './shell/header/header.component';
import { MainComponent } from './shell/main/main.component';
import { TwitDropzoneComponent } from './shell/main/twit-dropzone/twit-dropzone.component';
import { TwitService } from './services/twit.service';

const DEFAULT_DROPZONE_CONFIG: DropzoneConfigInterface = {
   maxFilesize: 50,
   acceptedFiles: 'image/*'
 };

@NgModule({
  declarations: [
    ShellComponent,
    HeaderComponent,
    MainComponent,
    TwitDropzoneComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatToolbarModule,
    FlexLayoutModule,
    HttpClientModule,
    TypingModule,
    DropzoneModule
  ],
  bootstrap: [ShellComponent],
  providers: [TwitService, 
  {
    provide: DROPZONE_CONFIG,
    useValue: DEFAULT_DROPZONE_CONFIG
  }]
})
export class AppModule { }
