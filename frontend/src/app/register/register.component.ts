import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, HttpClientModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent implements OnInit{
  form: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router
  ){
    this.form = this.formBuilder.group({
      name: '',
      email: '',
      password: ''
    });
  }

  ngOnInit(): void{
    
  }

  submit(): void{
    // console.log(this.form.getRawValue());
    this.http.post('http://localhost:8000/api/register', this.form.getRawValue()).subscribe(res => {
      this.router.navigate(['/login'])});
  }
}
