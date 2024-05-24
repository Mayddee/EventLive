import { Component, OnInit } from '@angular/core';
import { Eventi } from '../models';
import { EventsService } from '../services/events.service';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-event-list',
  standalone: true,
  imports: [CommonModule, HttpClientModule, RouterModule ],
  templateUrl: './event-list.component.html',
  styleUrl: './event-list.component.css'
})
export class EventListComponent implements OnInit{
  events: Eventi[] = []

  constructor(
    private http: HttpClient,
    private service: EventsService,
  ){}

  ngOnInit(): void {
      this.getEventList();
  }

  getEventList(){
    this.service.getEventList().subscribe((events: Eventi[])=>{
      console.log(events);
      this.events = events;
      this.service.setEvents(this.events)
    })
  }
}
