import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { EventsService } from '../services/events.service';
import { Eventi } from '../models';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';

@Component({
  selector: 'app-category-events',
  standalone: true,
  imports: [CommonModule, RouterModule, HttpClientModule],
  templateUrl: './category-events.component.html',
  styleUrl: './category-events.component.css'
})
export class CategoryEventsComponent {
  category: string = '';
  events!: Eventi[];
  // events$!: Observable<Eventi[]>;

  constructor(
    private route: ActivatedRoute,
    private service: EventsService
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.category = params.get('category')!; // Retrieve category code from route parameters
      console.log('Category code:', this.category);
      this.getEventsByCategory(this.category); // Call getEventsByCategory function
    });
    // this.category = this.route.snapshot.params['category'];
    // this.getEventsByCategory(this.category)
  }

  getEventsByCategory(category: string): void {
    this.service.getEventsByCategory(category)
      .subscribe(events => {
        this.events = events; // Assign the retrieved events to the component property
      });
  }

}
