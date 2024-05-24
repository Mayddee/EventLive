import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { Emitters } from '../emitters/emitters';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { EventsService } from '../services/events.service';

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [CommonModule, RouterModule, HttpClientModule],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent implements OnInit{
  authenticated = false;
  // categories: any[] = [];
  categories = this.service.getCategories();


  constructor(private http: HttpClient, private service:EventsService){
  }

  ngOnInit(): void {
    Emitters.authEmitter.subscribe((auth: boolean) =>{
      this.authenticated = auth;
    });
  }

  logout(): void {
    this.http.post('http://localhost:8000/api/logout', {}, {withCredentials: true}).subscribe(() => this.authenticated = false);
  }

  // getEventCategories(): void {
  //   this.http.get<string[]>('http://localhost:8000/api/categories/')
  //     .subscribe(categories => this.categories = categories);
  // }

  // getEventCategories(): void {
  //   this.http.get<any[]>('http://localhost:8000/api/categories/')
  //     .subscribe(categories => this.categories = categories);
  // }

}
