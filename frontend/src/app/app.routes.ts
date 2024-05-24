import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { EventListComponent } from './event-list/event-list.component';
import { EventDetailComponent } from './event-detail/event-detail.component';
import { CategoryEventsComponent } from './category-events/category-events.component';

export const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent},
    {path: 'events', component: EventListComponent},
    {path: 'events/:eventId', component: EventDetailComponent },
    // { path: 'events/CON', component: CategoryEventsComponent, data: { code: 'CON' } }, // Define route for Concert category
    // { path: 'events/MOV', component: CategoryEventsComponent, data: { code: 'MOV' } }, // Define route for Movie Premiere category
    // { path: 'events/THTR', component: CategoryEventsComponent, data: { code: 'THTR' } }, // Define route for Theatre category
    // { path: 'events/TOUR', component: CategoryEventsComponent, data: { code: 'TOUR' } }, // Define route for Tour category
    // { path: 'events/SHOW', component: CategoryEventsComponent, data: { code: 'SHOW' } }, // Define route for Show category
  
    {path: 'category-events/:category', component: CategoryEventsComponent },
    {path: 'login', component: LoginComponent},
    {path: 'register', component: RegisterComponent},
];