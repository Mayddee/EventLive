export interface User {
    id: number;
    username: string;
    email: string;
    password: string;
  }
  
export interface Eventi {

    id: number;
    name?: string;
    category: string;
    description?: string;
    location?: string;
    ticket_cost?: number;
    participants?: User[];
    date?: string;
    seats: number;
    available_seats: number;
    created?: string;
    updated?: string;
}

export interface Booking {
    id: number;
    participants: User[];
    events: Eventi[];
    details: string;
}
