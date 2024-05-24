import { Emitters } from '../emitters/emitters';

import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { Eventi } from '../models';
import { EventsService } from '../services/events.service';
@Component({
  selector: 'app-event-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, HttpClientModule, ],
  templateUrl: './event-detail.component.html',
  styleUrl: './event-detail.component.css'
})
// export class EventDetailComponent implements OnInit {
//   event!: Eventi;
//   eventId!: number;


//   constructor(
//     private http: HttpClient,
//     private service: EventsService,
//     private route: ActivatedRoute
//   ){}

//   ngOnInit(): void {
//     this.route.paramMap.subscribe(params => {
//       this.eventId = +params.get('eventId')!;
//       if (this.eventId) {
//         this.getEventDetails(this.eventId);
//       } else {
//         console.error('event id is null');
//       }
//     });
//   }

//   getEventDetails(eventId: number): void {
//     this.service.getEventDetails(eventId).subscribe(event => {
//       this.event = event;
//       this.eventId = eventId;
//     });
//   } 

  
// }


export class EventDetailComponent implements OnInit {
  event!: Eventi;
  eventId!: number;
  authenticated = true;
  constructor(
    private route: ActivatedRoute,
    private service: EventsService,
    private http: HttpClient
  ) { }

  ngOnInit(): void {
    
    this.route.paramMap.subscribe(params => {
      this.eventId = +params.get('eventId')!;
      // if(this.eventId) {
        this.getEventDetails(this.eventId);
      // }
    });
   

    Emitters.authEmitter.subscribe((auth: boolean) =>{
      console.log('Authentication status:', auth);
      this.authenticated = auth;
    });
    
  }

  getEventDetails(eventId: number): void {
    this.service.getEventDetails(eventId).subscribe(event => {
      this.event = event;
    });
  }

  bookEvent(eventId: number): void {
    
    if (this.authenticated == false) {
      console.error('User not authenticated. Please register first.');
      // You can display a message to the user to register first
      return;
    }
    this.service.bookEvent(eventId).subscribe(
      response => {
        // Handle successful booking
        console.log('Event booked successfully:', response);
      },
      error => {
        console.error('Error booking event:', error);
      }
    );
  }

  
}
