import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { MatDatepickerModule } from '@angular/material/datepicker';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DatepickerFilterExample } from './datepicker-filter-example';

@NgModule({
  declarations: [
    AppComponent,
    DatepickerFilterExample,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDatepickerModule 
  ],
  providers: [],
  bootstrap: [AppComponent, DatepickerFilterExample]
})
export class AppModule { }
