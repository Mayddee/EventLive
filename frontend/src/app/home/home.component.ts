import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Emitters } from '../emitters/emitters';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit{
  message = '';
  constructor(
    private http: HttpClient
  ){

  }

  ngOnInit(): void{
    this.http.get('http://localhost:8000/api/user', { withCredentials: true }).subscribe( (res: any) => {
      this.message = `Hi ${res.name}`;
      //to logout check
      Emitters.authEmitter.emit(true);
    },
    err => {
      this.message = 'You are not logged in!';
      Emitters.authEmitter.emit(false);
    });
  }
}
