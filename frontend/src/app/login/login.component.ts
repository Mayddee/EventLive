import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit{
  form: FormGroup;
  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ){
    this.form = this.formBuilder.group({
      email: '',
      password: ''
    });
  }

  ngOnInit(){

  }

  submit(): void {
    this.http.post('http://localhost:8000/api/login', this.form.getRawValue(), {
      // required to get cookies from backend to login check
      withCredentials: true
    }).subscribe(() => this.router.navigate(['/'])); //navigates to main page
  }
}
