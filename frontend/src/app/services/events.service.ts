import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { Eventi } from '../models';
import { Emitters } from '../emitters/emitters';

@Injectable({
  providedIn: 'root'
})
export class EventsService {
  events: Eventi[] = [];
  categories = [
    'CON', 'MOV', 'THTR', 'TOUR', 'SHOW'
  ];

  private authenticated = false;


  BASE_URL = "http://localhost:8000"

  constructor(private http: HttpClient) { 
    // Emitters.authEmitter.subscribe((authenticated: boolean) => {
    //   this.authenticated = authenticated;
    // });
  }

  getEventList(): Observable<Eventi[]>{
    return this.http.get<Eventi[]>(
      `${this.BASE_URL}/api/events/`
    )
  }

  getEventDetails(eventId: number): Observable<Eventi> {
    return this.http.get<Eventi>(`${this.BASE_URL}/api/events/${eventId}`);
  }

  bookEvent(eventId: number): Observable<any> {
    const url = `${this.BASE_URL}/api/events/${eventId}/book/`;
    return this.http.post<any>(url, {});
  }

  // setAuthenticated(authenticated: boolean): void {
  //   this.authenticated = authenticated;
  //   Emitters.authEmitter.emit(authenticated);
  // }

  // getAuthenticated(): boolean {
  //   return this.authenticated;
  // }

  setEvents(events: Eventi[]): void {
    this.events = events;
    
  }

  getCategories(): any[] {
    return this.categories;
  }

  

  getEvents(): Eventi[] {
    return this.events;
  }

  getEventsByCategory(code: string) {
    return this.http.get<Eventi[]>(`${this.BASE_URL}/api/events/${code}`);
  }
  // getEventsByCategory(code: string): Observable<any[]> {
  //   return this.getEventList().pipe(
  //     map(events => events.filter(event => event.category === code))
  //   );  
  // }

}
